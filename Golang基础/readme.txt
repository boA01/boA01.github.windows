# GOPATH——解决重复依赖问题
    第三方包仓库

# GoModule模式——解决项目结构问题
    项目文件存放位置

开启
    go env -w GO111MODULE=on
墙问题解决
    添加代理(.bashr或.zshrc)
        go env -w GOPROXY=https://goproxy.cn,direct #镜像源goproxy.io等
    更换/关闭 包校验
        go env -w GOSUMDB="sum.golang.goole.cn"或off

go env 查看环境变量

项目结构
go-mod-test -->模块名
    Makefile
    bin
    src
        config-folder -->目录  （导入）
            config-file.go -->文件名
                package xxx -->包名 （调用）
        test-folder
            xxx_test.go
                package test -->test包，测试
        pk1
            pk1
                pk1.go
            pk1.go
        main.go
            package main -->mian包，当前包可执行
            import (
                "go-mod-test/src/pk1"
                pk1pk1 "go-mod-test/src/pk1/pk1"  //目录名相同了，起别名
            )
    go.mod
    go.sum
    vendor

go mod init go-mod-test #初始化Module，生成go.mod
go mod tidy #更新依赖，生成go.sum
go mod download #下载依赖-默认GOPATH
go mod vendor #创建下载依赖目录，生成vendor，像极了pip，maven
go mod verify #包校验


go run ./src/main.go // 执行main包

go build ./src/main.go -o ./bin/ // 编译main包

go test -v  [-test.run 函数名] // 单元测试

go get xxx // 拉取并下载依赖

go install test-folder // 安装

go fix
go fmt
go doc
go vet

make build // 编译项目
make test // 执行测试