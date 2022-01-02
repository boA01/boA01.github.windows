package pipelineMiddleWare

import (
	"bytes"
	"encoding/binary"
	"fmt"
	"io"
	"math/rand"
	"net"
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

		for _, v := range data {
			out <- v
		}
		close(out)
		fmt.Println("排序完成", time.Since(startTime))
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
		close(out)
		fmt.Println("归并完成", time.Since(startTime))
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
	return Merge(MergeN(inputs[0:m]...), MergeN(inputs[m:]...))
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
		close(out)
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

func IntToByte(n int) []byte {
	data := int64(n)
	byteBuf := bytes.NewBuffer([]byte{})

	binary.Write(byteBuf, binary.BigEndian, data)
	return byteBuf.Bytes()
}

func ByteToInt(bts []byte) int {
	byteBuf := bytes.NewBuffer(bts)
	var data int64
	binary.Read(byteBuf, binary.BigEndian, &data)
	return int(data)
}

// 心跳
func HeartBeat(conn net.Conn, heartChan chan struct{}, timeout int) {
	for {
		select {
		case <-heartChan:
			// log.Println(hc)
			conn.SetDeadline(time.Now().Add(time.Duration(timeout) * time.Second))
		case <-time.After(time.Second * 30):
			conn.Close()
			return
		}
	}
}
