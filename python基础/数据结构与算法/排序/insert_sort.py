# 依次将元素插入到正确位置
def insert_sort(arr):
    for i in range(1, len(arr)):
        j = i-1
        item = arr[i] #待插入元素
        while j>=0 and arr[j]>item: 
            arr[j+1] = arr[j] #大的后移
            j-=1
        arr[j+1] = item #插入到正确位置
    return arr

print(insert_sort([1,2,2,42,0,1]))
