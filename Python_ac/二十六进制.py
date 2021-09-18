def test(n):
    r2 = [chr(j) for j in range(65,91)]
    l = []

    while n > 26:
        y = n%26
        l.append(y)
        n = n//26
    else:
        l.append(n)
    l.reverse()

    for i in l:
        print(r2[i-1])

if __name__ == "__main__":
    try:
        year = eval(input("请输入年份："))
    except:
        print("年份！！！")
    else:
        test(year)
    finally:
        pass