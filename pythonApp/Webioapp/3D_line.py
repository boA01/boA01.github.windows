import math as mt
from typing import Union
import pyecharts.options as opts 
from pyecharts.charts import Line3D
from pywebio.output import put_html

def float_range(start: Union[int, float], end: Union[int, float], step, round_number: int = 2):
    temp = []
    while True:
        if start < end:
            temp.append(round(start, round_number))
            start += step
        else:
            break
    return temp

for v in float_range(0, 2*mt.pi, 0.05):
    print(v)
    for u in float_range(-2, 2, 0.05):
        x=u*sin(v)
        y=cos(v)
        z=u
        
