# from threadpool import ThreadPool  # 线程池模式
# t = ThreadPool(2)  # 创建一个线程池，最大容量为2

#基本进程
# import multiprocessing #进程包
# import time
# def worker():
#     time.sleep(2)
#     print(multiprocessing.current_process().name)#打印当前进程的名字
#     print(multiprocessing.current_process().pid)#打印当前进程的id
#     print(multiprocessing.current_process().is_alive())#打印当前进程是否存活
#
# if __name__ == "__main__":
#     print('线程开始')
#     p = multiprocessing.Process(target = worker)#只用函数名 不加括号
#     p.start()#开始
#     p.join()#堵塞
#     print('线程结束')


#进程的通信方式有两种：共享内存和队列
# from multiprocessing import Process, Queue
# def write(q):#写入队列
#     print('加入队列成功：{}'.format(Process.pid))
#
#     for i in range(10):#0-9
#         print('往队列放入：{}'.format(i))
#         q.put(i)
# def read(q):#读取队列
#     print('加入队列成功：{}'.format(Process.pid))
#
#     while True:#有东西就读取
#         value = q.get()#取出队列中的值
#         print('读取队列中的值：{}'.format(value))
#
# if __name__ == '__main__':
#     q = Queue()#创建队列
#     pw = Process(target=write, args=(q,))#创建写入进程
#     pr = Process(target=read, args=(q,))#创建读取进程
#     pw.start()#启动写入进程
#     pr.start()#启动读取进程
#
#     pw.join()#堵塞写入进程
#同步通信进程池
# import multiprocessing
# def index(i):
#     result = i * i
#     return result
#
# if __name__ == '__main__':
#     i = list(range(100))#生成100个任务
#     pool = multiprocessing.Pool(processes=4) # 创建一个进程池，最大容量为4
#     # pool_result = pool.map(index, i) # 并行执行最大任务数，返回结果
#     pool_result = pool.apply(index,args=(1,))#执行一次任务，返回结果
#     pool.close() # 关闭进程池 不创建进程
#     pool.join() # 等待进程池中的所有进程执行完毕
#     print('Pool {}'.format(pool_result))

#异步通信进程池
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import time


# import asyncio
# async def index(i):
#     print('正在执行')
#     await asyncio.sleep(2)
#     print('执行完毕')
#
# asyncio.run(index(1))
# print()

# def generator1():
#     for i in range(3):
#         yield i
#
# def generator2():
#     yield from generator1()
#     for j in range(3, 6):
#         yield j
#
# # 使用 generator2
# for value in generator2():
#     print(value)

# def iterable_function():
#     yield from ['a', 'b', 'c']
#
# # 使用 iterable_function
# for value in iterable_function():
#     print(value)

#add_callback()方法

# from tornado.ioloop import IOLoop, PeriodicCallback
# import requests
# #业务逻辑操作写这里
# def get_data():
#     url = requests.get('https://www.baidu.com')
#     result = requests.get(url)
#     print(result.text)
#
# #异步操作写这里
# async def runner():
#     loop = IOLoop.current()
#     #任务派发写这里
#     for i in range(10):
#         loop.add_callback(get_data)
#
# print("This will be executed before the loop finishes")
#
# if __name__ == '__main__':
#      IOLoop.current().run_sync(runner)

#run_in_executor()方法

from tornado.ioloop import IOLoop, PeriodicCallback
import requests
from concurrent.futures import ThreadPoolExecutor
#业务逻辑操作写这里
def get_data():
    url = requests.get('https://www.baidu.com')
    result = requests.get(url)
    print(result.text)
async def runner():
    loop = IOLoop.current()
    #也可以用线程池ProcessPoolExecutor
    executor = ThreadPoolExecutor(20)

    #任务派发写这里
    for i in range(10):
        loop.run_in_executor(executor, get_data)
print('This will be executed before the loop finishes')
if __name__ == '__main__':
    IOLoop.current().run_sync(runner)