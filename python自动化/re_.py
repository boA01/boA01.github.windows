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
'''
def pd(s):
    if re.match(r"\d{3}\w1.\d*@qq.com", str(s), "1"):
        print("ok")
        return s
    return


    
