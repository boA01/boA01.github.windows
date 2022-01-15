package main

import (
	"fmt"
	"html/template"
	"net/http"
)

func f1(w http.ResponseWriter, r *http.Request) {
	kua := func(arg string) string {
		return arg + "666!"
	}

	t := template.New("f.tmpl") //创建模板对象
	t.Funcs(template.FuncMap{
		"kua666": kua,
	}) //添加函数
	_, err := t.ParseFiles("./f.tmpl") //解析模板

	if err != nil {
		fmt.Println(err)
		return
	}

	t.Execute(w, "boA")
}

func td1(w http.ResponseWriter, r *http.Request) {
	t, err := template.ParseFiles("./t.tmpl", "./ul.tmpl") // 注意顺序
	if err != nil {
		return
	}
	t.Execute(w, "boA")
}

func main() {
	http.HandleFunc("/", f1)
	http.HandleFunc("/tmplDemo", td1)

	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		fmt.Println(err)
		return
	}
}
