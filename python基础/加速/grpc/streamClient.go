package main

import (
	"context"
	"fmt"
	"sync"
	"time"

	"google.golang.org/grpc"
	"google.golang.org/grpc/status"

	"hellogrpc/proto"
)

// 中间件——时间统计，token认证
/*
func interceptor(
	ctx context.Context, method string,
	req, reply interface{}, cc *grpc.ClientConn,
	invoker grpc.UnaryInvoker, opts ...grpc.CallOption,
) error {
	start := time.Now()

	ctx = metadata.NewOutgoingContext(
		context.Background(),
		// 添加元数据
		metadata.New(
			map[string]string{
				"id":  "boA",
				"key": "123456",
			},
		),
	)
	// 向下调用
	err := invoker(ctx, method, req, reply, opts...)
	fmt.Printf("耗时：%s\n", time.Since(start))
	return err
}
*/

// 内置中间件——token认证
type customCredential struct{}

func (cc *customCredential) GetRequestMetadata(
	ctx context.Context, uri ...string,
) (map[string]string, error) {
	return map[string]string{
		"id":  "boA",
		"key": "1234567",
	}, nil
}

func (cc *customCredential) RequireTransportSecurity() bool {
	return false
}

func main() {
	conn, err := grpc.Dial(
		"localhost:9091",
		grpc.WithInsecure(),
		// 添加中间件
		// grpc.WithUnaryInterceptor(interceptor),
		grpc.WithPerRPCCredentials(new(customCredential)),
	)
	if err != nil {
		panic(err)
	}
	defer conn.Close()

	cli := proto.NewGreeterClient(conn)

	// 设置超时
	// ctx, cancel := context.WithTimeout(context.Background(), time.Second*3)
	// defer cancel()

	// 服务端流模式
	res, err := cli.GetStream(context.Background(), &proto.StreamReqData{Data: "boA"})
	if err != nil {
		st, ok := status.FromError(err)
		if !ok {
			panic("解析error失败")
		}
		fmt.Println(st.Message)
		fmt.Println(st.Code)
	} else {
		for {
			re, err := res.Recv()
			if err != nil {
				fmt.Println(err)
				break
			}
			fmt.Println(re.Data)
		}
	}

	// 客户端流模式
	putS, _ := cli.PutStream(context.Background())
	for i := 1; i < 10; i++ {
		putS.Send(&proto.StreamReqData{
			Data: fmt.Sprintf("hello %d", i),
		})
		time.Sleep(time.Second)
	}

	// 双向流模式
	allStr, _ := cli.AllStream(context.Background())
	wg := sync.WaitGroup{}
	wg.Add(2)

	go func(wg *sync.WaitGroup) {
		defer wg.Done()

		for {
			if data, err := allStr.Recv(); err != nil {
				fmt.Println(err)
				return
			} else {
				fmt.Printf("服务端>>>%s\n", data.Data)
			}
		}
	}(&wg)

	go func(wg *sync.WaitGroup) {
		defer wg.Done()

		for i := 1; i < 10; i++ {
			if err := allStr.Send(&proto.StreamReqData{
				Data: fmt.Sprintf("hello %d", i),
			}); err != nil {
				fmt.Printf("S：%s\n", err)
				break
			}
			time.Sleep(time.Second)
		}
	}(&wg)

	wg.Wait()
}
