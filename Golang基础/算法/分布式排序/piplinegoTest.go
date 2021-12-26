package test

import (
	"bufio"
	"fmt"
	"os"

	"./pipelineMiddleWare"
)

func mainx() {
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
	mainx()

	go func() {
		p := pipelineMiddleWare.Merge(
			pipelineMiddleWare.InMemorySort(pipelineMiddleWare.ArraySource(3, 3, 2, 5, 2, 5, 3)),
			pipelineMiddleWare.InMemorySort(pipelineMiddleWare.ArraySource(3, 3, 2, 5, 2, 5, 3)),
		)

		for v := range p {
			fmt.Println(v)
		}
	}()
}
