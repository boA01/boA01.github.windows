# for num in range(100,1000):
#     print(str(num)+str(num)[::-1])
#     print(str(num)+str(num)[1::-1])
while 1:
    try:
        n = input(":")
        if n == n[::-1]:
            print(n+"是回文")
        # break
    except:
        break