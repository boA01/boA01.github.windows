import ctypes as cp
import numpy as np
import pandas as pd

lib_c = cp.cdll.LoadLibrary("./py_c/libpycall.so")
so = cp.cdll.LoadLibrary("./py_go/libpycall.so")

lib_c.foo(1,2)

fib = so.Fib
add = so.Add
outStr = so.OutStr
out1Arr = so.Out1Arr
out2Arr = so.Out2Arr

# print(fib(3))
# print(add(3,4))

a = np.array([[1,2,3],[3,4,5],[9, 2, 3]], dtype=np.int32)
ptr = a.__array_interface__['data'][0]
out1Arr(ptr, 9)
out2Arr(ptr, 3)

print("END")