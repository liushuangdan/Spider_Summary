
#用greenlet实现Python中的并发：
---

## 下面是greenlet的例子：

```python
from greenlet import greenlet
# greenlet 其实就是手动切换；gevent是对greenlet的封装，可以实现自动切换

def test1():
    print("123")
    gr2.switch()   # 切换去执行test2
    print("456")
    gr2.switch()   # 切换回test2之前执行到的位置，接着执行

def test2():
    print("789")
    gr1.switch()   # 切换回test1之前执行到的位置，接着执行
    print("666")


gr1 = greenlet(test1)   # 启动一个协程 注意test1不要加()
gr2 = greenlet(test2)   #
gr1.switch()

```
### 分析如下：

这里创建了两个greenlet协程对象，gr1和gr2，

分别对应于函数test1()和test2()。使用greenlet对象的switch()方法，即可以切换协程。

上例中，我们先调用”gr1.switch()”，函数test1()被执行，然后打印出”123″；

接着由于”gr2.switch()”被调用，协程切换到函数test2()，打印出”789″；

之后”gr1.switch()”又被调用，所以又切换到函数test1()。

但注意，由于之前test1()已经执行到第5行，也就是”gr2.switch()”，

所以切换回来后会继续往下执行，也就是打印”456″；

之后”gr2.switch()”又被调用，所以又切换到函数test2()。

接着由于”gr2.switch()”又被调用，协程切换到函数test2()，切换回test1之前执行到的位置，接着执行，打印出”666″；

现在函数test2()退出，同时程序退出。

### 执行结果：
```python
123
789
456
666
```

其实greenlet协程的实现就是使用了栈，其运行的上下文保存在栈中，”main”主协程处于栈底的位置，而当前运行中的协程就在栈顶。

这同函数是一样。此外，在任何时候，你都可以使用”greenlet.getcurrent()”，获取当前运行中的协程对象。比如在函数test2()中执行”greenlet.getcurrent()”，其返回就等于”gr2″。

