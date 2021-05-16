from dao import Util
from util import People
import pywebio as pw
from pywebio.input import *
from pywebio.output import *
from functools import partial
from pywebio.session import go_app, hold
# import numpy as np
# import pandas as pd

def log():
    u = input_group(inputs=[
        input("用户名：", name='u_name'),
        input("密码：", name='u_passwd')
    ])

    u = Util()

    if u.log()==True:
        arr=[]
        for i in u.select_():
            arr.append(list(
                list(i.values())+[put_buttons(['编辑'],[lambda:go_app("bianji")])]
                )
            )

        put_table(
            tdata=arr,
            header=['姓名', '年龄', '口号','操作']
            )
    hold()

def bianji(choice=' ', use_x=0):
    if choice=='删除':
        print("delete")
    else:
        popup('', [
              put_html('<h3>信息如下：</h3>'),
              put_table([['A', 'B'], ['C', 'D']]),
              put_buttons(['确定'], [lambda: go_app("main")])
              ]
            )
    hold()

def test():
    put_row([
        put_buttons(['注册'], [lambda:go_app("bianji")]),
        put_buttons(['登录'], [lambda:go_app("log")])
    ], size="50% 2px 50%"
    )
    
    # put_link('注册', app='main')  #  使用app参数指定任务名
    # put_link('登录', app='log')

def btn_click(btn_val):
    put_text("You click %s button" % btn_val)

def main():
    put_grid(
        [
            [
                put_buttons(['注册'], [lambda:go_app("bianji")]),
                put_buttons(['登录'], [lambda:go_app("log")])
            ]
        ], cell_height='20px', cell_width='60px'
    )

    # put_buttons(['注册'], [lambda: go_app('test')])
    # put_buttons(['登录'], [lambda: go_app('log')])
    
    hold()

if __name__=="__main__":
    # pw.start_server({'注册': task_1, '登录': task_2})
    # 等价于 pw.start_server([test, task_1, task_2, main, bianji]) 'index': test, 
    pw.start_server([main,test,bianji])
    # test()