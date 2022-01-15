package main

import (
	"fmt"
	"net/http"
	"path"

	"github.com/gin-gonic/gin"
)

type User struct {
	Username string `form:"uname"`
	Password string `form:"pwd"`
}

func main() {
	r := gin.Default()

	r.LoadHTMLFiles("./login.html", "./success.html")

	// 获取URI参数（注意路由匹配冲突）
	r.GET("/blog/:year/:month", func(c *gin.Context) {
		year := c.Param("year")
		month := c.Param("month")
		c.JSON(http.StatusOK, gin.H{
			"year":  year,
			"month": month,
		})
	})

	r.GET("/web", func(c *gin.Context) {
		// res := c.Query("query") // 获取地址栏参数值
		res := c.DefaultQuery("query", "boa666") //带默认值
		// res, ok := c.GetQuery("query") //带判断

		// url重定向
		c.Redirect(http.StatusMovedPermanently, "https://my.oschina.net/"+res)

		// 路由重定向
		// c.Request.URL.Path("./admin")
	})

	r.GET("/admin", func(c *gin.Context) {
		c.HTML(http.StatusOK, "login.html", nil)
	})

	r.POST("/login", func(c *gin.Context) {
		/*
		   uname := c.PostForm("uname")
		   pwd := c.PostForm("pwd")
		   // pwd := c.DefaultPostForm("CAPTCHA", "***")

		   u := User{
		       username: uname,
		       password: pwd,
		   }
		*/

		var u User
		c.ShouldBind(&u) //属性绑定
		fmt.Printf("%#v\n", u)

		c.HTML(http.StatusOK, "success.html", gin.H{
			"Name": u.Username,
		})
	})

	r.POST("/upload", func(c *gin.Context) {
		// 读取文件
		f, err := c.FormFile("f1")
		if err != nil {
			return
		} else {
			// 保存到本地
			// dst := fmt.Sprintf("./%s", f.Filename)
			dst := path.Join("./", f.Filename)
			_ = c.SaveUploadedFile(f, dst)
			c.JSON(http.StatusOK, gin.H{
				"status": "OK",
			})
		}
	})

	r.Run(":8080")
}
