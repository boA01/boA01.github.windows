package test

import (
    "fmt"
    "testing"
)

func TestIf(t *testing.T) { 
    res := testErr1()

    if res != nil {
        t.Fataif("有错误\n目标：%v,实际：%v\n", true, res)
    }
    t.Logf("测试通过")
}

// go test -v  [-test.run 函数名]