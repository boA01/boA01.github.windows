import math
# r = int(input())
# area = math.pi*r**2
# print("%.7f"%area)
# print(f"{round(area,7)}")

arr = [1,2,1,2,2,1,4,5,2,2]
arr1 = []
n = 1

for i in sorted(arr, reverse=True):
    if i not in arr1[:n]:
        arr1.insert(0, i)
        n+=1
    else:
        arr1.append(i)
# sorted(arr2, key=arr2.count)
print(arr1)