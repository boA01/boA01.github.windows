docker build . -t goweb_app # 构建镜像

docker run -p 8888:8888 goweb_app # 运行镜像

http://127.0.0.1:8888 # 测试服务