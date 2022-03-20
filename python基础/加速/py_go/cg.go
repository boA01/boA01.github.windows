package main

/*
#include <stdio.h>

static void SayHello(const char* s) {
	puts(s);
}
*/

import (
	"C"
)

//export Foo
func Foo(a, b int) int {
	// C.puts(C.CString("完成\n")) // go字符串转c *char
	// C.SayHello(C.CString("完成\n")) // 调用自己写的c函数
	return a + b
}

//export Fib
func Fib(n int) int {
	if n == 1 || n == 2 {
		return 1
	} else {
		return Fib(n-1) + Fib(n-2)
	}
}

func main() {}

/*
//export Foo 必须写

Linux
go build -buildmode=c-shared -o _foo.so pycall.go

Windows
go build -ldflags "-s -w" -o main.dll -buildmode=c-shared main.go 动态库

go build -o libpycall.a -buildmode=c-archive pycall.go 静态库
gcc -shared -fpic -o demo.so demo.c
gcc -v test.c -o test1 libpycall.a demo.so -lWinMM -lntdll -lWS2_32
*/
