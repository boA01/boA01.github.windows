
from collections import OrderedDict
 
getNumsFromString = lambda x: list(map(int, x.strip().split()))
def isInWindow(loc, window):
    """ 判断点击是否在窗内 """
    x, y, w, h = window
    return loc[0] >= x and loc[0] <= x + w and \
        loc[1] >= y and loc[1] <= y + h
 
N, M = getNumsFromString(input())
 
# 读取窗口，越向后表示越上层
windows = OrderedDict() # {loc: id}
for i in range(N):
    x, y, w, h = getNumsFromString(input())
    windows[(x, y, w, h)] = i + 1
 
# 读取点击操作
ids = [-1 for i in range(M)]
for i in range(M):
    loc = getNumsFromString(input())
    for window, id in list(windows.items())[::-1]:
        # 从顶级向底部判断
        if isInWindow(loc, window):
            windows.move_to_end(window)
            ids[i] = id
            break
 
print('\n'.join(list(map(str, ids))))