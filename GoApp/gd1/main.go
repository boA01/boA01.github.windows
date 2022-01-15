package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func hi(c *gin.Context) {
	c.JSON(200, gin.H{
		"message": "hi golang",
	})
}

func main() {
	r := gin.Default() //返回默认路由的引擎

	r.Static("/blog", "./statics/blog") //加载静态资源
	r.LoadHTMLGlob("templates/**/*")    //模板解析，正则匹配
	// r.LoadHTMLFiles("./templates/index.tmpl") //模板解析，文件名匹配

	r.GET("/", func(c *gin.Context) {
		c.HTML(http.StatusOK, "blog/index.tmpl", gin.H{ //模板渲染
			"title": "https://boa.com",
		})
	})

	r.GET("/users/index", func(c *gin.Context) {
		c.HTML(http.StatusOK, "users/index.tmpl", gin.H{
			"title": "boA",
		})
	})

	r.GET("/hi", hi)
	r.Run(":8080") //启动服务,默认8080，例：":9090"
}
