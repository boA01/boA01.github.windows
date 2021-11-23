l1 = [
    [1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1],
    [1,3,0,0,0,0,1],
    [1,0,0,3,3,0,1],
    [1,0,3,0,0,0,1],
    [1,0,3,0,0,0,1],
    [1,1,1,1,1,1,1],
]

def f1(arr, x=1, y=1):
    if arr[5][5] == 2:
        return arr
    else:
        if arr[x][y] == 0:
            print(x,y)
            arr[x][y] = 2
            if f1(arr, x+1, y):
                return True
            elif f1(arr, x, y+1):
                return True
            elif f1(arr, x, y-1):
                return True
            elif f1(arr, x-1, y):
                return True
        else:
            return False

f1(l1) // 引用传递；一维l1[:]，多维copy.deepcopy(l1)

for i in l1:
    print(i)