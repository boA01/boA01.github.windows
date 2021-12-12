# 小版本golang
FROM golang:alpine AS builder

ENV GO111MoDULE=on \
    CGO_ENABLED=0 \
    GOOS=linux \
    GOARCH=amd64

WORKDIR /build

COPY go.mod .
COPY go.sum .
RUN go mod download

COPY . .

RUN go build -o bubble .
#############################
# 创建小镜像
FROM debian:stretch-slim

COPY ./wait-for.sh /
COPY ./templates /templates
COPY ./static /static
COPY ./conf /conf

COPY --from=builder /build/bubble /

RUN set -eux; \
    apt-get update; \
    apt-get install -y \
        --no-install-recommends \
        netcat; \
        chmod 755 wait-for.sh

ENTRYPOINT ["/bubble", "conf/config.ini"]
