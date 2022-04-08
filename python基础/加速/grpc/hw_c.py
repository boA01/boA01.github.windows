from socket import timeout
import grpc
from proto import helloWorld_pb2, helloWorld_pb2_grpc

# 中间件
class DefaultInterceptor(grpc.UnaryUnaryClientInterceptor):
    def intercept_unary_unary(self, continuation, client_call_details, request):
        from datetime import datetime
        start = datetime.now()
        # 向下调用
        rsp = continuation(client_call_details, request)
        print(f"耗时：{(datetime.now()-start).microseconds/1000}ms")
        return rsp

if __name__ == "__main__":
    with grpc.insecure_channel("localhost:9091") as chan:
        # 添加中间件
        intercept_chan = grpc.intercept_channel(chan, DefaultInterceptor())
        stub = helloWorld_pb2_grpc.HelloStub(intercept_chan)
        
        hello_req = helloWorld_pb2.HelloRequest()
        hello_req.name = "boA"
        
        # rsp: helloWorld_pb2.HelloResponse = stub.SayHello(hello_req)
        
        try:
            rsp, call = stub.SayHello.with_call(
                hello_req,
                # 添加元数据
                metadata = (
                    ("name", "boA"),
                    ("pwd", "1234567")
                ),
                # 设置超时时间
                timeout = 3
            )
        except grpc.RpcError as e:
            d = e.details()
            print(d)
            status_code = e.code()
            print(status_code.name)
            # print(status_code.value)
        else:
            print(rsp.message)