package main

import (
    "github.com/gin-gonic/gin"
    "net/http"
)

func hi(c *gin.Context) {
    name := c.MustGet("name") //获取上下文值
    c.JSON(200, gin.H{
        "message": name,
    })
}

// 中间件函数
func m1(c *gin.Context){
    fmt.Println("m1 in ...")
    
    // 计数
    start := time.Now()

    // go funcXXX(c.Copy()) //中间调用协程，解决并发不安全

    c.Set("name", "boA") //通过中间件传值
    c.Next() //调用后续的处理函数
    // c.Abort() //阻止调用后续处理函数

    cost := time.Since(start) //花费时间
    fmt.Printf("用户浏览了%v\n", cost)
    
    fmt.Println("m1 out ...")
}

func goodDay(doCheck bool) gin.HandlerFunc{
    return fucn(c *gin.Context) {
        if doCheck{
            fmt.Println("今天是个好日子")
        } else {
            c.Next()
        }
    }
}

func main() {
    r := gin.Default() //返回默认路由的引擎,
    // 默认中间件：Logger(), Recovey();
    // gin.New() //没有默认中间件的路由

    // r.GET("/hi", hi)

    // r.Use(m1) //全局注册中间件
    r.GET("/hi", m1, hi) //单独注册
    
    // RESTful API (风格：请求对应动作)
    r.GET("/book", func(c *gin.Context){
        c.JSON(200, gin.H{
            "message":"get",
        })
    }) //获取

    r.POST("/book", func(c *gin.Context){
        c.JSON(http.StatusOK, gin.H{
            "message":"post",
        })
    }) //发送

    r.PUT("/book", func(c *gin.Context){
        c.JSON(http.StatusOK, gin.H{
            "message":"put",
        })
    }) //更新

    r.DElETE("/book", func(c *gin.Context){
        c.JSON(http.StatusOK, gin.H{
            "message":"delete",
        })
    }) //删除

    r.Any("/user", func(c *gin.Context){
        c.JSON(http.StatusOK, gin.H{
            "message": "any"
        })
        switch c.Request.Method {
            case "GET":
                c.JSON(http.StatusOK, gin.H{
                    "message":"get",
                })
            case http.MethodPost:
                c.JSON(http.StatusOK, gin.H{
                    "message":"post",
                })
            case http.MehtodPut:
                c.JSON(http.StatusOK, gin.H{
                    "message":"put",
                })
            case http.MehtodDelete:
                c.JSON(http.StatusOK, gin.H{
                    "message":"delete",
                })
        }
    }) //所有类型

    // 非法路由
    r.NoRoute(func(c *gin.Context){
        c.JSON(http.StatusNotFound, gin.H{
            "msg": "不存在",
        })
    })

    // 路由组
    videoGroup := r.Group("/video", goodDay(true))
    { //视觉效果
        videoGroup.GET("/a", func(c *gin.Context){
            c.JSON(http.StatusOK, gin.H{
                "msg": "/video/a",
            })
        })

        videoGroup.GET("/b", func(c *gin.Context){
            c.JSON(http.StatusOK, gin.H{
                "msg": "/video/b",
            })
        })
        
        videoGroupC := r.Group("/c")// 可嵌套
        {
            videoGroup.GET("/a", func(c *gin.Context){
                c.JSON(http.StatusOK, gin.H{
                    "msg": "/video/c/a",
                })
            })

            videoGroup.GET("/b", func(c *gin.Context){
                c.JSON(http.StatusOK, gin.H{
                    "msg": "/video/c/b",
                })
            })
        }
    }

    r.Run(":8080") //启动服务,默认8080，例：":9090"
}
