package main

import (
	"bufio"
	"fmt"
	"os"
	"time"

	"dc/pipelineMiddleWare"
)

func mainx() {
	fmt.Println("hello main")
	filename := "data.txt"
	var count = 10000
	file, _ := os.Create(filename)

	defer file.Close()

	mypipe := pipelineMiddleWare.RandomSourceArray(count)
	writer := bufio.NewWriter(file)
	pipelineMiddleWare.WriterSlink(writer, mypipe)
	writer.Flush()

	file, _ = os.Open(filename)
	defer file.Close()
	mypiperead := pipelineMiddleWare.ReadSource(bufio.NewReader(file), -1)
	counter := 0
	for v := range mypiperead {
		fmt.Println(v)
		counter++

		if counter > 1000 {
			break
		}
	}
}

func main() {
	fmt.Println("<<<<<<<<<<<<<<")
	// ch := make(chan int)

	go func() {
		p := pipelineMiddleWare.Merge(
			pipelineMiddleWare.InMemorySort(pipelineMiddleWare.ArraySource(5, 3, 6)),
			pipelineMiddleWare.InMemorySort(pipelineMiddleWare.ArraySource(2, 4, 7, 8)),
		)

		for v := range p {
			fmt.Println(v)
		}
		// ch <- 0
		// close(ch)
	}()
	// <-ch
	// runtime.Gosched()
	time.Sleep(time.Second * 10)
}
