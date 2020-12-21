import _thread
import threading
import time

timesleep = [2,4]
# def output(noutput,sec,lock):
#     使用_thread
#     print("****start{}*****".format(noutput))
#     time.sleep(sec)
#     print("*****end{}*****".format(noutput))
#     lock.release()
def output(noutput,sec,name):
    #使用threading
    print("****start{}*****{}".format(noutput,name))
    time.sleep(sec)
    print("*****end{}*****{}".format(noutput,name))
class Mythread(threading.Thread):
    #使用面向对象
    def __init__(self,func,args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)




if __name__ == "__main__":
    nums = [6,4]
    threads = []
    n = len(nums)
    for i in range(n):
        t = Mythread(func=output,args=(i,nums[i],output.__name__))
        threads.append(t)

    for i in range(n):
        threads[i].start()

    for i in range(n):
        threads[i].join()  #线程没结束会阻塞于此，避免使用lock
    # #使用_thread
    # locks = []
    # #创建锁
    # for i in timesleep:
    #     a = _thread.allocate_lock()
    #     a.acquire()
    #     locks.append(a)
    # #创建线程
    # for i in range(len(timesleep)):
    #      _thread.start_new_thread(output,(i,timesleep[i],locks[i]))
    #
    # for i in range(len(timesleep)):
    #     while locks[i].locked(): pass


    #原语
    #锁  解决了线程间数据互斥访问
    #信号量