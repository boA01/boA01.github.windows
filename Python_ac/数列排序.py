arr = [1,2,1,2,2,1,4,5,2,2]
arr1 = []

for i in sorted(arr, reverse=True):
    if i not in arr1:
        arr1.insert(0, i)
    else:
        arr1.append(i)
# sorted(arr2, key=arr2.count)
print(arr1)