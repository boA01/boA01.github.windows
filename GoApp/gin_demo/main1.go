package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

func hello(w http.ResponseWriter, r *http.Request) {
	_, _ = fmt.Fprintln(w, "<h1>hello Golang</h1>")
}

func hi(w http.ResponseWriter, r *http.Request) {
	b, err := ioutil.ReadFile("./hi.txt")
	if err != nil {
		fmt.Println("read file err")
	} else {
		_, _ = fmt.Fprintln(w, string(b))
	}
}

func main() {
	//http.HandleFunc("/hello", hello)
	http.HandleFunc("/hi", hi)
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		fmt.Printf("http server failed, err:%v\n", err)
		return
	}
	// fmt.Println("hello boa")
}
