package main

import (
	"bufio"
	"fmt"
	"os"

	"dc/pipelineMiddleWare"
)

func createPipline(fileName string, fileSize int, chunkCount int) <-chan int {
	file, err := os.Create(fileName)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	mypipe := pipelineMiddleWare.RandomSourceArray(fileSize / 8)
	writer := bufio.NewWriter(file)
	pipelineMiddleWare.WriterSlink(writer, mypipe)
	writer.Flush()

	chunkSize := fileSize / chunkCount // 每份数量
	sortRes := []<-chan int{}
	pipelineMiddleWare.Init()
	for i := 0; i < chunkCount; i++ {
		file, err := os.Open(fileName)
		if err != nil {
			panic(err)
		}
		file.Seek(int64(i*chunkSize), 0)
		source := pipelineMiddleWare.ReadSource(bufio.NewReader(file), chunkSize)
		sortRes = append(sortRes, pipelineMiddleWare.InMemorySort(source))
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
	// fp := `E:\Py代码\boA01.github.windows\Golang基础\算法\分布式排序\`
	go func() {
		p := createPipline(fp+"big.in", 10000, 4)
		writeToFile(p, fp+"big.out")
		showFile(fp + "big.out")
		ch <- struct{}{}
		close(ch)
	}()
	<-ch
}
