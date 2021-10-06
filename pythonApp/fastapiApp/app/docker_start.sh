sudo docker run -d --name myfastapi -p 80:80 myFastAPI

# 导出镜像
# docker save -o myfastapi.tar myfastapi

# 部署的机器执行
# docker load < myfastapi.tar 