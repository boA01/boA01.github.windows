import pymongo

class Util(object):
    def __init__(self):
        pass

    def log(self, host = '127.0.0.1', user = 'root', passwd = '4211', dbs = 'test1', cts = 'c3'):
        blog = False
        try:
            client = pymongo.MongoClient(host=(host))
            db = client[dbs] #选择数据库
            self.ct = db[cts] #选择集合
        except:
            pass
        else:
            blog = True
        finally:
            return blog

    def add_(self, *plist):
        self.ct.insert_many(list(plist))

    def delete_(self, **kw):
        self.ct.remove(kw)
    
    def update_one(self, id = 0, **args):
        self.ct.updateOne({'_id':id},{'$set':args}, False, False)
    
    def update_all(self, o_kw, n_kw):
        self.ct.update(o_kw,{'$set':n_kw}, False, True)

    def select_(self, id = 0, **kw):
        result = self.ct.find(kw, {"_id": id})
        return result
        # for i in result:
        #     print(i)

if __name__ == "__main__":
    u = Util()
    u.log()

    if u.blog==True:
        p1 = {'name': "cpp",
             'age': 2,
             'title': 'very good!!!'
            }

        p2 = {'name': "java",
             'age': 1,
             'title': 'very good!!!'
            }
        # u.add_(p1, p2)
        # u.delete_(name=None)
        # u.delete_(id=ObjectId('6085662e1e8a304d10581c68'))
        # u.update_all({'age':4},{'age':2})
        u.select_()
        # u.select_(age={'$lt':2})