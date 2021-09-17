'''
右上区域没有点的点
'''
# arr=[(1, 2), (5, 3), (4, 6), (7, 5), (9, 0)]
n = int(input())
arr = []
for i in range(n):
    arr.append(tuple(map(int,input().split(' '))))

arr_sort=sorted(arr,key=lambda x:x[0])
arr_sort_y=[i[1] for i in arr_sort]
l = len(arr_sort)

for i in range(l-1):
    if (y:=arr_sort[i][1]) > max(arr_sort_y[i+1:]):
        print(arr_sort[i][0],y)
print(arr_sort[-1][0],arr_sort[-1][1])