package main

import (
	_ "fmt"
	"html/template"
	"net/http"
)

func index(w http.ResponseWriter, r *http.Request) {
	t, err := template.ParseFiles("./base.tmpl", "./index.tmpl")
	if err != nil {
		return
	}
	t.ExecuteTemplate(w, "index.tmpl", "boA")
}

func home(w http.ResponseWriter, r *http.Request) {
	t, err := template.ParseFiles("./base.tmpl", "./home.tmpl")
	if err != nil {
		return
	}
	t.ExecuteTemplate(w, "home.tmpl", "Boa")
}

func rp(w http.ResponseWriter, r *http.Request) {
	t, err := template.New("rp.tmpl").Delims("{(", ")}").ParseFiles("./rp.tmpl")
	if err != nil {
		return
	}
	err = t.Execute(w, "boA")
	if err != nil {
		return
	}
}

func main() {
	http.HandleFunc("/index", index)
	http.HandleFunc("/home", home)
	http.HandleFunc("/rp", rp)
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		return
	}
}
