class People(object):

    def __init__(self, name, age, title):
        self.name = name
        self.age = age
        self.title = title
        
if __name__ == "__main__":
    p = People("jjj", 2, "hell")
    print(p.name)
 