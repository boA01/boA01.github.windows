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

//export Add
func Add(a, b int) int {
	return a + b
}

func main() {}

/*
//export Foo 必须写

go build -buildmode=c-shared -o _foo.so pycall.go
*/
