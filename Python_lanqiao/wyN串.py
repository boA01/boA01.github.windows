'''
小A很喜欢字母N，他认为连续的N串是他的幸运串。
有一天小A看到了一个全部由大写字母组成的字符串，
他被允许改变最多2个大写字母（也允许不改变或者
只改变1个大写字母），使得字符串中所包含的最长
的连续的N串的长度最长。你能帮助他吗？

输出描述:
对于每一组测试样例，输出一个整数，表示操作后包含的最长的连续N串的长度。
3
NNTN
NNNNGGNNNN
NGNNNNGNNNNNNNNSNNNN

输出例子:
4
10
18
'''

number = input()
for i in range(int(number)):
    a = input()
    b = []
    c = 0
    for j in a:
        b.append(j)
        if len(b) - b.count('N') >= 3:
            b.pop(0)
        c = max(c, len(b))
    print(c)