import ctypes as cp

lib = cp.cdll.LoadLibrary("./libpycall.so")
lib.foo(1,2)
print("END")