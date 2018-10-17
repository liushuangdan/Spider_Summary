
# 进程和进程池
---

## 进程编程

1. 导入线程和进程的包
2. 新建进程或者线程的类t
3. 函数启动线程/进程 t.start()
4. 主线程或者主进程 t.join()
5. 限制进程和线程的个数， Pool
6. 进程池和线程池的作用就是
    a) 限制进程或者线程的个数 
    b) 重用进程和线程

---
## 进程编写代码的例子：
```python
from multiprocessing import Process
import multiprocessing
import time
# 1. 我们需要生成一个多进程的类
# 2. 开启这个多进程 start
# 3. 等待所有的进程结束 join
def task1(msg):
    print('task1: hello, %s' % msg)
    time.sleep(1)
def task2(msg):
    print('task2: hello, %s' % msg)
    time.sleep(1)
def task3(msg):
    print('task3: hello, %s' % msg)
    time.sleep(1)
if __name__ == '__main__':
    # 输入的参数target是函数， args是参数
    p1 = Process(target=task1, args=('one',))
    p2 = Process(target=task2, args=('two',))
    p3 = Process(target=task3, args=('three',))

    start = time.time()

    p1.start()
    p2.start()
    p3.start()

    print("The number of CPU is:" + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print("child p.name: " + p.name + "\tp.id: " + str(p.pid))

    p1.join()
    p2.join()
    p3.join()

    end = time.time()
    print('3 processes take %s seconds' % (end - start))

```

## 进程执行结果
```python

The number of CPU is:4
child p.name: Process-2	p.id: 8456
child p.name: Process-3	p.id: 13236
child p.name: Process-1	p.id: 14036
task1: hello, one
task2: hello, two
task3: hello, three
3 processes take 1.9531116485595703 seconds

```


---

## 进程池的代码编写
```python
from multiprocessing import Pool
import time


def task(msg):
    print('hello, %s' % msg)
    time.sleep(5)
    print('finished %s'% msg)

def task2(msg):
    print('Say, %s' % msg)
    time.sleep(1)
    print('Say finish %s' % msg)


if __name__ == '__main__':
    pool = Pool(processes=4)

    for x in range(10):
        print('111')
        pool.apply_async(task, args=(x,))

    for x in range(5):
        print('222')
        pool.apply_async(task2, args=(x,))
    # 执行完close以后就不能再向pool中放置任务了
    pool.close()
    pool.join()

    print('processes done.')
```

###进程池执行结果

```python
111
111
111
111
111
111
111
111
111
111
222
222
222
222
222
hello, 0
hello, 1
hello, 2
hello, 3
finished 0
hello, 4
finished 1
hello, 5
finished 2
hello, 6
finished 3
hello, 7
finished 4
hello, 8
finished 5
hello, 9
finished 6
Say, 0
finished 7
Say, 1
Say finish 0
Say, 2
Say finish 1
Say, 3
Say finish 2
Say, 4
Say finish 3
Say finish 4
finished 8
finished 9
processes done.
```



