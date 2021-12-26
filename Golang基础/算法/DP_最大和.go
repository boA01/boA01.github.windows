package main

import (
	"fmt"
	"math"
)

var arr = [...]int{-2, 1, -3, 4, -1, 2, 1, 5, 4}

func main() {
	long := len(arr)
	dp := make([]int, long)
	dp[0] = arr[0]
	M := 0

	for i := 1; i < long; i++ {
		dp[i] = int(math.Max(float64(arr[i]), float64(arr[i]+dp[i-1])))
		if M < dp[i] {
			M = dp[i]
		}
	}
	fmt.Println(M)
}
