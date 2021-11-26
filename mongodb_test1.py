import pymongo
client = pymongo.MongoClient(host='127.0.0.1')
# client = MongoClient('mongodb://localhost:27017/')

# db_list = client.list_database_names()
# print(db_list)

db = client.test1
# db = client['test1']

# print(db)
ct = db.c3
# collection = db['c3']

# person = {
#     'name': "c",
#     'age': '2',
#     'title': 'very good!!!'
# }

# ct.insert_one(person)
# result = ct.insert([p1, p2])
# result = ct.insert_many([p1, p2])

ct.update_one({'age':2},{'$set': {'age': 2}})
# ct.update_many()

# ct.remove({"_id": "5f618b03d43f336dbe0935f3"})

result = ct.find({}, {'_id':0})
# results = collection.find({'name':'python'})
# for result in results:
for i in result:
    print(i.get('age'))

# results = collection.find({'age':{'$gt':20}})#条件查询

# $lt小于{'age': {'$lt': 20}}  
# $gt大于{'age': {'$gt': 20}}  
# $lte小于等于{'age': {'$lte': 20}}  
# $gte大于等于{'age': {'$gte': 20}}  
# $ne不等于{'age': {'$ne': 20}}  
# $in在范围内{'age': {'$in': [20, 23]}}  
# $nin不在范围内{'age': {'$nin': [20, 23]}}  
# $regex匹配正则表达式{'name': {'$regex': '^M.*'}}name以M开头  
# $exists属性是否存在{'name': {'$exists': True}}name属性存在  
# $type类型判断{'age': {'$type': 'int'}}age的类型为int  
# $mod数字模操作{'age': {'$mod': [5, 0]}}年龄模5余0  
# $text文本查询{'$text': {'$search': 'Mike'}}text类型的属性中包含Mike字符串  
# $where高级条件查询{'$where': 'obj.fans_count == obj.follows_count'}自身粉丝数等于关注数 


