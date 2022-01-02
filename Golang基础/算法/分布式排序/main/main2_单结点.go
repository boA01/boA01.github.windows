package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"

	"dc/pipelineMiddleWare"
)

func createNetPipline(fileName string, fileSize int, chunkCount int) <-chan int {
	file, err := os.Create(fileName)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	mypipe := pipelineMiddleWare.RandomSourceArray(fileSize / 8)
	writer := bufio.NewWriter(file)
	pipelineMiddleWare.WriterSlink(writer, mypipe)
	writer.Flush()

	chunkSize := fileSize / chunkCount
	sortAddr := []string{}
	pipelineMiddleWare.Init()

	file, err = os.Open(fileName)
	if err != nil {
		panic(err)
	}

	for i := 0; i < chunkCount; i++ {
		file.Seek(int64(*&chunkSize), 0)
		source := pipelineMiddleWare.ReadSource(bufio.NewReader(file), chunkSize)
		addr := ":" + strconv.Itoa(7000+i)

		pipelineMiddleWare.NetWordkWrite(addr, pipelineMiddleWare.InMemorySort(source))
		sortAddr = append(sortAddr, addr)
	}

	sortRes := []<-chan int{}
	for _, addr := range sortAddr {
		sortRes = append(sortRes, pipelineMiddleWare.NetWordkRead(addr))
	}

	return pipelineMiddleWare.MergeN(sortRes...)
}

func writeToFile(in <-chan int, fileName string) {
	file, err := os.Create(fileName)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	writer := bufio.NewWriter(file)
	defer writer.Flush()

	pipelineMiddleWare.WriterSlink(writer, in)

}

func showFile(fileName string) {
	file, err := os.Open(fileName)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	p := pipelineMiddleWare.ReadSource(bufio.NewReader(file), -1)
	counter := 0

	for v := range p {
		fmt.Println(v)
		counter++
		if counter > 1000 {
			break
		}
	}
}

func main() {
	ch := make(chan struct{})
	fp := "E://Py代码//boA01.github.windows//Golang基础//算法//分布式排序//"

	go func() {
		p := createNetPipline(fp+"big.in", 10000, 4)
		writeToFile(p, fp+"big.out")
		showFile(fp + "big.out")
		ch <- struct{}{}
		close(ch)
	}()
	<-ch
}
