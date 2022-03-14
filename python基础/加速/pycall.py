import ctypes as cp

lib_c = cp.cdll.LoadLibrary("./py_c/libpycall.so")
lib_go = cp.cdll.LoadLibrary("./py_go/libpycall.so")

lib_c.foo(1,2)
fib = lib_go.Fib
add = lib_go.Add
print("END")