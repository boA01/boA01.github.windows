from fastapi import FastAPI, Header, Body, Form

app = FastAPI()

#             获取url参数
# http://127.0.0.1:8000/user1/666
@app.get("/user/{id}")
def get_user1(id):
    return {"id":id}

#             接收请求头数据
# http://127.0.0.1:8000/user2?id=666
@app.get("/user")
def get_user2(id,token=Header(None)):
    return {"id":id, "token":token}
    
#             接收json数据
@app.api_route("/login_json",methods=('GET','POST','PUT'))
def login_json(data=Body(None)):
    return {"data":data}

#             接收form数据
@app.api_route("/login_form",methods=('GET','POST','PUT'))
def login_form(userName=Form(None), userPwd=Form(None)):
    return {"data":{"name":userName,"passwd":userPwd}}


# if __name__ == "__main__":
