from proto import hello_pb2

request = hello_pb2.HelloRequest()
request.name = "Boa"

# 序列化
res_str = request.SerializeToString()
print(res_str, len(res_str))

# 反序列化
request.ParseFromString(res_str)
print(request.name)


import json
json_str = json.dumps({
    "name": "Boa"
})
print(json_str, len(json_str))