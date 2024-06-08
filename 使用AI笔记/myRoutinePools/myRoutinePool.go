package main

import(
	"fmt"
	"time"
	"atomic"
)

type threadPool struct {
	workers int32 //协程池总容量
	runningWorkers atomic.Int32 // 活跃的协程个数

	waiting atomic.Int32 // 阻塞等待的数量
	cond    *sync.Cond   // 条件变量，用于阻塞等待协程池中协程对象

	closed chan struct{} // Pool是否关闭
	// 配置信息
	option *Options

	// 回收对象
	victim sync.Pool  // 表示释放的协程对象
	// 操作local对象的锁
	lock sync.Locker
	// 协程对象缓存
	local goWorkerCache

	// 判断goPurge是否已经结束
	purgeDone int32
	// 等待协程对象停止（包括协程池 和用户协程）
	allRunning *wait.Wait
}

// 构建协程池对象
// capacity: -1表示不限定 >0表示最大的协程个数
func NewPool(capacity int32, opts ...Options) *Pool {

}

func (p *Pool) Waiting() int32 {
	return p.waiting.Load()
}

func (p *Pool) Running() int32 {
	return p.running.Load()
}

func (p *Pool) Cap() int32 {
	return p.capactiy
}

func (p *Pool) Free() int32 {
	if p.Cap() < 0 {
		return -1
	}
	return p.Cap() - p.Running()
}

// 调整容量
func (p *Pool) Tune(capacity int32) {

}

// 外部提交任务
func (p *Pool) Submit(task TaskFunc) error {
}

func (p *Pool) getGoWorker() (*goWorker, error) {

}


func (p *Pool) Close() {
}

func (p *Pool) CloseWithTimeOut(timeout time.Duration) error {
}
func (p *Pool) IsClosed() bool {
}

// 定期清理：长时间未使用的*goWorker
func (p *Pool) goPurge() {
}

// 循环利用协程对象
func (p *Pool) recycle(gw *goWorker) bool {
}