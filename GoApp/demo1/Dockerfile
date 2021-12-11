# 拉去alpine Linux发行版
FROM golang:alpine

# 设置编译阶段需要的环境变量
ENV GO111MoDULE=on \
    CGO_ENABLED=0 \
    GOOS=linux \
    GOARCH=amd64

# 工作目录切到/build
WORKDIR /build

# 代码复制到工作目录
COPY . .

# 编译代码
RUN go build -o app .

# 工作目录切到/dist
WORKDIR /dist

# 将可执行文件拷贝到工作目录
RUN cp /build/app .

# 申明服务端口
EXPOSE 8888

# 启动容器是运行app
CMD ["/dist/app"]