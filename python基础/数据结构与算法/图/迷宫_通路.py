ar = [
  ["XYZE"],
  ["SFZS"],
  ["XDEE"]
]

arr = ["".join(i) for i in ar]
r = len(arr) # 行
l = len(arr[0]) # 列

s = "XDEZSE"

def f(x, y, c):
    if 0 <= x < r and 0 <= y < l and arr[x][y] == c[0]: # 是否匹配
        print(x,y,c)
        try:
            # c.pop(0)
            c = c[1:]
            if c == []:
                return True
        except: # 全部匹配完成
            return True
        if f(x+1, y, c):
            # print("下")
            return True
        elif f(x, y+1, c):
            # print("右")
            return True
        elif f(x-1, y, c):
            # print("上")
            return True
        elif f(x, y-1, c):
            # print("左")
            return True
        else:
            return False
    else:
        return False

def main():
    for i in range(r):
        for j in range(l):
            if s[0] == arr[i][j]: # 起始点
                ss = list(s)
                if f(i, j, ss): # 起点，目标字符串
                    print("ok")
                    return True
                else:
                    print("no")
    return False
main()