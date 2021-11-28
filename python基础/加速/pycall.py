import ctypes as cp

lib_c = cp.cdll.LoadLibrary("./py_c/libpycall.so")
lib_go = cp.cdll.LoadLibrary("./py_go/libpycall.so")

libc.foo(1,2)
print("END")