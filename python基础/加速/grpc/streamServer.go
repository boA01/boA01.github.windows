package main

import (
	"context"
	"fmt"
	"net"
	"sync"
	"time"

	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/metadata"
	"google.golang.org/grpc/status"

	"hellogrpc/proto"
)

const PORT = ":9091"

type GreeterServer struct{}

func (gs *GreeterServer) GetStream(req *proto.StreamReqData, res proto.Greeter_GetStreamServer) error {
	for i := 0; i < 10; i++ {
		_ = res.Send(&proto.StreamResData{
			Data: fmt.Sprintf("%v", time.Now().Unix()),
		})
		time.Sleep(time.Second)
	}
	return nil
}

func (gs *GreeterServer) PutStream(cliStr proto.Greeter_PutStreamServer) error {
	for {
		if recv, err := cliStr.Recv(); err != nil {
			fmt.Println(err)
			break
		} else {
			fmt.Println(recv.Data)
		}
	}
	return nil
}

func (gs *GreeterServer) AllStream(allStr proto.Greeter_AllStreamServer) error {
	wg := sync.WaitGroup{}
	wg.Add(2)

	go func(wg *sync.WaitGroup) {
		defer wg.Done()

		for {
			if data, err := allStr.Recv(); err == nil {
				fmt.Printf("客户端>>>%s\n", data.Data)
			} else {
				break
			}
		}
	}(&wg)

	go func(wg *sync.WaitGroup) {
		defer wg.Done()

		for i := 9; i > 0; i-- {
			if err := allStr.Send(&proto.StreamResData{
				Data: fmt.Sprintf("hi %d", i),
			}); err != nil {
				fmt.Printf("C：%s\n", err)
				break
			}
			time.Sleep(time.Second)
		}
	}(&wg)

	wg.Wait()
	return nil
}

// 中间件——token认证
func interceptor3(
	ctx context.Context, req interface{}, info *grpc.UnaryServerInfo, handler grpc.UnaryHandler,
) (resp interface{}, err error) {
	fmt.Println("进入中间件")
	// 获取元数据
	if md, ok := metadata.FromIncomingContext(ctx); ok {
		if idSlice, ok := md["id"]; ok && idSlice[0] == "boA" {
			if keySlice, ok := md["key"]; ok && keySlice[0] == "123456" {
				return handler(ctx, req)
			}
		}
		return resp, status.Error(codes.Unauthenticated, "认证失败")
	}
	return resp, status.Error(codes.Unauthenticated, "无token信息")
}

func main() {
	lis, err := net.Listen("tcp", PORT)
	if err != nil {
		panic(err)
	}
	defer lis.Close()

	rpcs := grpc.NewServer(
	// 添加中间件，多个使用ChainUnaryInterceptor()
	// grpc.UnaryInterceptor(interceptor3),
	// 流加拦截器
	// grpc.StreamInterceptor(interceptor4),
	)
	proto.RegisterGreeterServer(rpcs, new(GreeterServer))

	err = rpcs.Serve(lis)
	if err != nil {
		panic(err)
	}
}
