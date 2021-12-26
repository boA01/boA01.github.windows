package pipelineMiddleWare

import (
	"encoding/binary"
	"fmt"
	"io"
	"math/rand"
	"sort"
	"time"
)

var startTime time.Time // 构造时间

func Init() {
	startTime = time.Now()
}

func UseTime() {
	fmt.Println(time.Since(startTime)) //统计耗时
}

// 内存排序
func InMemorySort(in <-chan int) <-chan int {
	out := make(chan int, 1024)

	go func() {
		data := []int{}

		for v := range in {
			data = append(data, v) //添加数据到数组
		}

		fmt.Println("数据读取完成", time.Since(startTime))
		sort.Ints(data) //排序
		fmt.Println(data)

		for _, v := range data {
			out <- v
		}
	}()
	return out
}

// 合并
func Merge(in1, in2 <-chan int) <-chan int {
	out := make(chan int, 1024)

	go func() {
		v1, o1 := <-in1
		v2, o2 := <-in2

		// 归并思想
		for o1 || o2 {
			if (o1 && v1 <= v2) || !o2 {
				out <- v1
				v1, o1 = <-in1
			} else {
				out <- v2
				v2, o2 = <-in2
			}
		}

		fmt.Println(o1, o2)
		if o1 {
			out <- v1
		}
		if o2 {
			out <- v2
		}
	}()
	return out
}

// 多路归并
func MergeN(inputs ...<-chan int) <-chan int {
	length := len(inputs)
	if length == 1 {
		return inputs[0]
	}
	m := length / 2
	return Merge(MergeN(inputs[:m]...), MergeN(inputs[m:]...))
}

// 写入
func WriterSlink(writer io.Writer, in <-chan int) {
	for v := range in {
		buf := make([]byte, 8)
		binary.BigEndian.PutUint64(buf, uint64(v))
		writer.Write(buf)
	}
}

// 读取
func ReadSource(reader io.Reader, chunksize int) <-chan int {
	out := make(chan int, 1024)

	go func() {
		buf := make([]byte, 8)
		readsize := 0

		for {
			n, err := reader.Read(buf)
			readsize += n

			if n > 0 {
				out <- int(binary.BigEndian.Uint64(buf))
			}

			if err != nil || (chunksize != -1 && readsize >= chunksize) {
				break
			}
		}
	}()
	return out
}

// 随机数组
func RandomSourceArray(count int) <-chan int {
	out := make(chan int)

	go func() {
		for i := 0; i < count; i++ {
			out <- rand.Int()
		}
		close(out)
	}()
	return out
}

func ArraySource(num ...int) <-chan int {
	var out = make(chan int)

	go func() {
		for _, v := range num {
			out <- v
		}
		close(out)
	}()
	return out
}
