#########mysql#############
import pymysql.cursors

connect = pymysql.Connect(
    user= ,
    host= ,
    port= 3306,
    passwd = ,
    db = "python",
    charset = "utf-8"
    )

###########redis############
import redis

conn = redis.connect(
    host = ,
    port = 6379,
    )

##########MongoDB###########
import pymongo

db = pymongo.MongoClient("mongodb://root:123456@localhost:27017/python")