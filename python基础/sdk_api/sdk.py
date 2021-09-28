class China():
    def __init__(self, path = ''):
        self._path = path
    
    def __getattr__(self, path):
        return China(f"{self._path}/{path}")

    __call__ = __getattr__

    # def users(self, username):
    #     return China(f'GET /user/{username}')

    
    def __str__(self):
        return self._path

    __repr__ = __str__

if __name__ == '__main__':
    u1 = China().status.user.timeline.list
    print(u1)
    '''
    u1 = China() = ''
    u1 = China().status = '/status'
    
    '''
    

    u2 = China().users("michael").repos
    print(u2)
    '''
    1：China()='' 实例化
    2：China().users=China('/users')='/users' 重建实例
    3：China().users('michael')=China('/users')('michael')=China('/users/michael')=/users/michael' 实例调用
    4：同2
    '''

    