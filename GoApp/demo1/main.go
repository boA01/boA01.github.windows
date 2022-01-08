package main

import (
	"fmt"
	"net/http"
)

func hello(rw http.ResponseWriter, _ *http.Request) {
	rw.Write([]byte("hello boA"))
}

func main() {
	http.HandleFunc("/", hello)
	server := &http.Server{
		Addr: ":8888",
	}

	fmt.Println("server startup...")

	if err := server.ListenAndServe(); err != nil {
		fmt.Printf("server startup failed, err:%v\n", err)
	}
}
