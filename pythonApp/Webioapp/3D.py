from pywebio.output import put_html
from typing import Union

import math
import pyecharts.options as opts
from pyecharts.charts import Surface3D

import numpy as np 
"""
"""


def float_range(start: int, end: int, step: Union[int, float], round_number: int = 2):
    """
    浮点数 range
    :param start: 起始值
    :param end: 结束值
    :param step: 步长
    :param round_number: 精度
    :return: 返回一个 list
    """
    temp = []
    while True:
        if start < end:
            temp.append(round(start, round_number))
            start += step
        else:
            break
    return temp


def surface3d_data():
    # u = np.linspace(0, 2*np.pi, 50)
    # v = np.linspace(0, np.pi, 50)

    # x = np.outer(np.cos(u), np.sin(v))
    # y = np.outer(np.sin(u), np.sin(v))
    # z = np.hypot(x,y)
    # yield zip(x, y, z)

    for t0 in float_range(-2, 2, 0.05):
        y = t0
        for t1 in float_range(-1, 1.01, 0.05):
            x = t1
            # x = math.sqrt(1-t1**2)
            # if t1!=0:
            #     x*=(t1/abs(t1))
            z = np.sin(x ** 2 + y ** 2)
            # z = math.hypot(x,y)
            yield [x, y, z]

def surface3d_data_1():
    u, v = np.mgrid[-2:2:80j, 0:2*np.pi:40j]
    x = u*np.sin(v)
    y = u*np.cos(v)
    z = np.hypot(x,y)
    yield [x, y, z]

def surface3d_data_2():
    for v in float_range(0, 2*math.pi, 0.05):
        # print(v)
        # for u in float_range(-2, 2, 0.05):
            x=math.sin(v) #0,1,0,-1,0
            y=math.cos(v) #1,0,-1,0,1
            z=abs(3-math.hypot(x,y)) #1
            yield [x,y,z]

l = list(surface3d_data_2())
# print(l)

# u, v = np.mgrid[-2:2:80j, 0:2*np.pi:40j]
# x = u*np.cos(v)
# y = u*np.sin(v)
# z = np.abs(u)
# l = list(zip(*x,*y,*z))
# print(l)
# '''
c = (
    Surface3D()
    .add(
        series_name="",
        shading="color",
        # data=list(zip(*x,*y,*z)),
        data = l,
        xaxis3d_opts=opts.Axis3DOpts(type_="value"),
        yaxis3d_opts=opts.Axis3DOpts(type_="value"),
        grid3d_opts=opts.Grid3DOpts(width=100, height=40, depth=100),
    )
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(
            dimension=2,
            max_=1,
            min_=-1,
            # range_color=[
            #     "#313695",
            #     "#4575b4",
            #     "#74add1",
            #     "#abd9e9",
            #     "#e0f3f8",
            #     "#ffffbf",
            #     "#fee090",
            #     "#fdae61",
            #     "#f46d43",
            #     "#d73027",
            #     "#a50026",
            # ],
        )
    )
    
)

c.width = "100%"
put_html(c.render_notebook())
# '''