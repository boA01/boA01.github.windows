// 生成随机数
func main1() {
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

// 归并
func main2() {
	fmt.Println("<<<<<<<<<<<<<<")
	ch := make(chan int)
	defer close(ch)

	go func() {
		p := pipelineMiddleWare.Merge(
			pipelineMiddleWare.InMemorySort(pipelineMiddleWare.ArraySource(5, 3, 8, 8)),
			pipelineMiddleWare.InMemorySort(pipelineMiddleWare.ArraySource(2, 4, 6, 6)),
		)

		for v := range p {
			fmt.Println(v)
		}
		ch <- 0
	}()
	<-ch
}