package main

import (
	"context"
	"fmt"
	"net"

	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/metadata"
	"google.golang.org/grpc/status"

	proto "hellogrpc/proto"
)

type HelloServer struct{}

/* client
	添加元数据
   // metadata（元数据）
	md := metadata.Pairs(
		"uName", "boA",
		"pwd", "123456",
	)
	md := metadata.New(
		map[string]string{
			"uName": "boA",
			"pwd":   "123456",
		})
	ctx := metadata.NewOutgoingContext(context.Background(), md)

	res, _ := cli.GetStream(ctx, &proto.SayHello{Name: "boA"})

*/

func (hs *HelloServer) SayHello(ctx context.Context, req *proto.HelloRequest) (*proto.HelloResponse, error) {
	msg := "你好 " + req.GetName()
	return &proto.HelloResponse{Message: msg}, nil
}

// 中间件函数
func interceptor1(
	ctx context.Context, req interface{}, info *grpc.UnaryServerInfo, handler grpc.UnaryHandler,
) (resp interface{}, err error) {
	fmt.Println("进入中间件~~~")
	res, err := handler(ctx, req)
	fmt.Println("退出中间件~~~")
	return res, err
}

// 中间件——token认证
func interceptor2(
	ctx context.Context, req interface{}, info *grpc.UnaryServerInfo, handler grpc.UnaryHandler,
) (resp interface{}, err error) {
	// 获取元数据
	if md, ok := metadata.FromIncomingContext(ctx); ok {
		if idSlice, ok := md["name"]; ok && idSlice[0] == "boA" {
			if keySlice, ok := md["pwd"]; ok && keySlice[0] == "123456" {
				return handler(ctx, req)
			}
		}
		return resp, status.Error(codes.Unauthenticated, "认证失败")
	}
	return resp, status.Error(codes.Unauthenticated, "无token信息")
}

func main() {
	lis, err := net.Listen("tcp", "0.0.0.0:9091")
	if err != nil {
		panic(err)
	}
	defer lis.Close()

	rpcs := grpc.NewServer(
		// 添加中间件
		// grpc.UnaryInterceptor(interceptor1),
		grpc.ChainUnaryInterceptor(
			interceptor1,
			interceptor2,
		),
	)
	proto.RegisterHelloServer(rpcs, new(HelloServer))
	rpcs.Serve(lis)
}
