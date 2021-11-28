package main

import (
	"C"
)

// export Foo
func Foo(a, b int) int{
	return a+b
}

func main() {}

/*
// export Foo 必须写

go build -buildmode=c-shared -o libpycall.so pycall.go
*/