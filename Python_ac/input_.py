# a,b=(map(eval, input("+个数:"+"-个数:").split(" ")))
# n=list(map(eval, input("输入数字：").split(" ")))

def quick_sort(arr):
    if len(arr)>1:
        mid = arr.pop(0)
        l, r = [], []
        for i in arr:
            if i>mid:
                r.append(i)
            else:
                l.append(i)
        return quick_sort(l)+[mid]+quick_sort(r)
    else:
        return arr

arr = [1,2,3,1,1,2,30,0]
print(quick_sort(arr))