package main

import (
	"fmt"
	"html/template"
	"net/http"
)

type User struct {
	Name string
	Age  int
}

func hello(w http.ResponseWriter, r *http.Request) {
	// 2.解析模板
	t, err := template.ParseFiles("./hello.tmpl")
	if err != nil {
		fmt.Println("parse template failed", err)
		return
	}

	name := "boA"

	// 3.渲染模板
	err = t.Execute(w, name)
	if err != nil {
		fmt.Println(err)
		return
	}
}

func outPeo(w http.ResponseWriter, r *http.Request) {
	t, err := template.ParseFiles("./people.tmpl")

	if err != nil {
		return
	}

	u1 := User{
		Name: "boA",
		Age:  18,
	}

	m1 := map[string]interface{}{
		"Name": "Boa",
		"Age":  18,
	}

	err = t.Execute(w, []interface{}{
		0: u1,
		1: m1,
	})

	if err != nil {
		return
	}
}

func main() {
	http.HandleFunc("/", outPeo)

	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		fmt.Println("http server start failed", err)
		return
	}
}
