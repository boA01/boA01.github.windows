l1 = [
    [1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1],
    [1,0,0,0,0,0,1],
    [1,0,0,0,0,0,1],
    [1,0,0,0,0,0,1],
    [1,1,1,1,1,1,1],
]

X = len(l1)-2
Y = len(l1[0])-2

def f2(arr, x, y):
    while arr[X][Y] != 2:
        if arr[x][y] == 0:
            arr[x][y] = 2 # 标记
            print(x,y)
            if f2(arr, x+1, y):
                return True
            elif f2(arr, x, y+1):
                return True
            elif f2(arr, x-1, y):
                return True
            elif f2(arr, x, y-1):
                return True
            else:
                return False
        else:
            return False

f2(l1,1,1) #迷宫，起点