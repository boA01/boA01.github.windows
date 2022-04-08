安装工具
pip install grpcio
pip install grpcio-tools

编写proto文件
/*
syntax = "proto3"; // 版本申明

import "base.proto"; // 导入文件
import "google/protobuf/empty.proto"; // 导入内置empty
import "google/protobuf/timestamp.proto"; // 导入内置timestamp

// package proto;  // 指定包名
option go_package = "./;proto"; // golang的包名

枚举类型
enum Gender {
    MALE = 1;
    FEMALE = 0;
}

类似于结构体
message 消息名 {
    [属性] 类型 命名 = 编号;  // 类型定义
    Gender g = 2;
    map<string, string> m = 3; // 映射
    google.protobuf.Timestamp addTime = 4; // 时间
}

类似于接口
service 服务名 {
    rpc 方法名 ([stream] 请求类型) returns ([stream] 响应类型); // 方法定义
}
*/

编译通式
protoc -I=导入文件路径 xxx.proto --插件名_out=输出路径 --插件名_opt=模块路径

生成python文件
python -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I. helloWorld.proto

生成golang文件
protoc -I. helloWorld.proto --go_out=plugins=grpc:.

protoc --go_out=../protos --go_opt=paths=source_relative --go-grpc_out=../protos --go-grpc_opt=paths=source_relative echo.proto