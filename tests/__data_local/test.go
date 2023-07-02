package main

// This is a comment
import (
	"fmt"
	"strings"
)

func main() {
	/*
	Another comment
	*/
	for i := 0; i < 10; i++ {
		fmt.Println(strings.Repeat(" ", (10-i)) + strings.Repeat("*", (i*2+1)))
	}

	for i := 10; -1 < i; i-- {
		fmt.Println(strings.Repeat(" ", (10-i)) + strings.Repeat("*", (i*2+1)))
	}
}
