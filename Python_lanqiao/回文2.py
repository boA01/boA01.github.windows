a = "ABCABADCSABBAUYIIYU"
s = 0
# 回文数大于2个字符
for i in range(2, len(a)+1):
    b = []
    for j in range(len(a)-i+1):
        # 生成的组合
        new_s = a[j:j+i]
        if new_s == new_s[::-1]:
            b.append(new_s)
    # print(b)
    s += len(b)
print("总共子串回文：", s)