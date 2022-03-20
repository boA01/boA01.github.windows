import ctypes as cp
import numpy as np
import pandas as pd

lib_c = cp.cdll.LoadLibrary("./py_c/libpycall.so")
lib_go = cp.cdll.LoadLibrary("./py_go/libpycall.dll")

lib_c.foo(1,2)

fib = lib_go.Fib
add = lib_go.Add
outStr = lib_go.OutStr
out1Arr = lib_go.Out1Arr
out2Arr = lib_go.Out2Arr

# print(fib(3))
# print(add(3,4))

a = np.array([[1,2,3],[3,4,5],[9, 2, 3]], dtype=np.int32)
ptr = a.__array_interface__['data'][0]
print(ptr)
# out1Arr(ptr)
out2Arr(ptr, 3)

print("END")