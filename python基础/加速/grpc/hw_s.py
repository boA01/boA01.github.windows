import time
import grpc
from concurrent import futures
from proto import helloWorld_pb2, helloWorld_pb2_grpc

class Hello(helloWorld_pb2_grpc.HelloServicer):
    def SayHello(self, request, context):
        msg = ""
        time.sleep(5)
        # 获取元数据
        md = dict(context.invocation_metadata())
        if md.get("pwd") == "123456":
            context.set_code(grpc.StatusCode.OK)
            msg = f"你好，{request.name}"
        else:
            # 返回状态码
            context.set_code(grpc.StatusCode.FAILED_PRECONDITION)
            # 返回错误信息
            context.set_details("验证失败")
        return helloWorld_pb2.HelloResponse(message = msg)

# 中间件
class LogInterceptor(grpc.ServerInterceptor):
    def intercept_service(self, continuation, handler_call_details):
        print("进入中间件~~~")
        rsp = continuation(handler_call_details)
        print("退出中间件~~~")
        return rsp

if __name__ == "__main__":
    # 实例化server
    server = grpc.server(
        # 设置线程池大小
        futures.ThreadPoolExecutor(max_workers=10),
        # 添加中间件
        interceptors=(LogInterceptor(),)
    )
    # 注册逻辑到server
    helloWorld_pb2_grpc.add_HelloServicer_to_server(Hello(), server)
    # 启动server
    server.add_insecure_port('[::]:9091')
    server.start()
    server.wait_for_termination()