package main

import (
	"fmt"
	"sync"
)

type threadPool struct {
	workers int
	queue   chan func()
	wg      sync.WaitGroup
}

func newThreadPool(workers int) *threadPool {
	return &threadPool{
		workers: workers,
		queue:   make(chan func()),
	}
}

func (p *threadPool) run() {
	p.wg.Add(p.workers)

	for i := 0; i < p.workers; i++ {
		go func() {
			defer p.wg.Done()

			for f := range p.queue {
				f()
			}
		}()
	}
}

func (p *threadPool) submit(f func()) {
	p.queue <- f
}

func (p *threadPool) wait() {
	print("first in wait", len(p.queue))
	p.wg.Wait()
	print("first out", len(p.queue))
	close(p.queue)
}

func main() {
	pool := newThreadPool(4)

	pool.run()

	for i := 0; i < 10; i++ {
		pool.submit(func() {
			fmt.Println("正在执行的任务:", i)
		})
	}

	// go func() {
	// 	time.Sleep(time.Second)
	// 	close(pool.queue)
	// }()

	pool.wait()

	fmt.Println("所有任务已完成")
}