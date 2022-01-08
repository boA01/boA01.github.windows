from pywebio.output import *
from pywebio.pin import *
from pywebio import start_server

import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Helix equation
# t = np.linspace(0, 10, 100) # 
# x, y, z = np.cos(t), np.sin(t), t
# x, y, z = np.random.random(10),np.random.random(10),np.random.random(10)
# x, y, z = np.random.rand(3, 1000)
# x, y, z = np.random.randn(3, 5000) # 正态分布

# x = np.arange(8) #
# y = np.linspace(10,20,5) #线性序列 
# z = np.logspace(1,3,3,base=3) #等比数列
# np.zeros((m,n))
# np.ones((m,n))
# np.empty((m,n))
# np.fromfunction(fun,(m,n))

# a*b multiplu(a,b)对应元素相乘
# kronx(a,b) 张量积
# outer(a,b) 外积, 叉乘；|a||b|sin<a,b> (张量积的一种形式)
# dot(a,b) matnul(a,b) 内积，点乘；|a||b|cos<a,b> 

def reset():
    x = np.random.normal(25, 8, 400).astype(int)
    y, z = np.random.randint(0, 51, (2,400))

    df = pd.DataFrame(data = {
        "x":x,
        "y":y,
        "z":z
    })
    df1 = df.sort_values(by='x',ascending=False)
    df1.to_csv(r"data.csv", index=False)

def reset1():
    toast("Clicked")
    reset()

def d1(df):
    fig = go.Figure(data=[go.Scatter3d(
        x=df["x"],
        y=df["y"],
        z=df["z"],
        mode='markers',
        marker=dict(
            size=20,
            color=df["x"],
            colorscale='Viridis',   # choose a colorscale
            opacity=1               # 不透明度
        )
    )])

    fig.show()
    # fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    # html = fig.to_html(include_plotlyjs="require", full_html=False)
    # return html

def d2(df):
    put_slider(name="x", value=-1, min_value=-1, max_value=100, step=1)
    while True:
        pin_wait_change("x")
        x = pin.x
        if x == -1:
            df1 = df
        else:
            if x-2 < 0:
                df1 = df.loc[(df['x']>=0) & (df['x']<x+3)]
            elif x+2 > 100:
                df1 = df.loc[(df['x']>= x-2) & (df['x']<= x)]
            else:
                df1 = df.loc[(df['x']>= x-2) & (df['x']<= x+2)]
        d1(df1)
        # with use_scope("res", clear=True):
        #     put_text(f"x = {pin.x}")

def d3():
    print("start")
    put_button("重置", onclick=reset1, color='success', outline=True)

def index(df):
    put_column([
        d3(),
        d2(df),
    ])

def main():
    df = pd.read_csv(r"E:\Py代码\boA01.github.windows\data.csv")
    index(df)

# start_server(main, port=9090, auto_open_webbrowser=True)
reset()
# '''

# [0,'n',0] [100, 'n', 100]

# r=10
# (0,0) l (0,20)