// AI 生成的快速排序

package main

import (
    "fmt"
    "sync"
)

var wg sync.WaitGroup

func quickSort(arr []int, start int, end int, c chan []int) {
    if start < end {
        pivot := partition(arr, start, end)
	wg.Add(2)
	go func(){
	    defer wg.Done()
            quickSort(arr, start, pivot-1, c)
	}()
	go func(){
            defer wg.Done()
	    quickSort(arr, pivot+1, end, c)
	}()
        wg.Wait()
    }
    c <- arr[start:end] // send the sorted slice to the channel
}

func partition(arr []int, low int, high int) int {
    i := (low - 1)
    pivot := arr[high]

    for j := low; j <= high-1; j++ {
        if arr[j] < pivot {
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
        }
    }
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1
}

func main() {
    nums := []int{38,27,43,3,9,82,10}
	c := make(chan []int)
    wg.Add(1) // we are starting one goroutine
	go func(){
	    defer wg.Done()
        quickSort(nums, 0, len(nums)-1, c)
	}()
	// merge the sorted slices in order to get a sorted large slice
    final := []int{}
    for i:= 0;i<len(nums);i++{
        temp := <-c // receive from channel
	final = append(final,temp...)
    }
    fmt.Println("sorted array is ",final)
}