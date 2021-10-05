#本位与后面位比较，确定本位
def select_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[i]<arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr