'''
进程
资源分配的最小单位

线程
执行的最小单位
'''

import os
print(f"父进程{os.getpid()} start!!!")
pid = os.fork()
if pid == 0:
    print(f"子进程{os.getpid()} start!11")
else:
    print("!!!")