import re

'''
\d
\w
\s
[a-zA-Z\_][0-9a-zA-Z\_]* python命名规则
^ 开头
$ 结尾
| 或
{m,n} m到n个
() 分组,group(n) groups()
. 任意一个
* 任意个
+ 至少一个
? 0或1个
+? 防止贪婪

re.match("rule", s)
re.split("rule", s)
'''

def pd(s):
    if re.match(r"w{3}\.\w.\.@qq.com", str(s), "1"):
        print("ok")
        return s
    return
