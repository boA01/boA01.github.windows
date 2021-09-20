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

re.match("rule", s) #从头匹配一个符合规则的字符串
re.split("rule", s) #扫描整个string找到第一个匹配然后返回
.group() 返回被 RE 匹配的字符串
.start() 返回匹配开始的位置
.end() 返回匹配结束的位置
.span()返回一个元组包含匹配 (开始,结束) 的位置
'''

def pd(s):
    if re.match(r"w{3}\.\w.\.@qq.com", str(s), "1"):
        print("ok")
        return s
    return