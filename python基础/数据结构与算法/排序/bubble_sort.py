# 两两比较，确定末位
def bubble_sort(arr):
    for i in range(len(arr)-1, 1, -1):
        flag = True
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1]=arr[j+1], arr[j]
                flag = False
        if flag:
            break
    return arr