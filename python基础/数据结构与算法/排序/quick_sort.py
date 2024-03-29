# 按基准值，左大右小摆放，分而治之
def quick_sort(arr):
    if len(arr)>1: #递归入口
        mid = arr.pop() #基值
        l, r = [], []
        for i in arr:
            if i>mid:
                r.append(i) #大于基准值放右边
            else:
                l.append(i) #小于基准值放左边
        return quick_sort(l) + [mid] + quick_sort(r)
    else:
        return arr

print(quick_sort([1,3,1,3,2,4]))