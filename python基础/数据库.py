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

##########SQLite###########
import sqlite3

#连接或创建数据库文件
conn = sqlite3.connect("test.db")

#创建一个游标
cursor= conn.cursor()

#创建表
cursor.execute("create table user (id int primary key,name varchar(6),pwd varchar(16))")

#获得结果集
cursor.fetchall()

# 关闭指针
cursor.close()