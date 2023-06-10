import threading
from time import sleep


lock1 = threading.Lock()


def main():
    for _ in range(10):
        lock1.acquire()
        print(threading.current_thread().name)
        lock1.release()
        sleep(1)


def main():
    for _ in range(10):
        with lock1:
            print(threading.current_thread().name)
        sleep(1)


if __name__ == '__main__':
    threads = (threading.Thread(target=main, name=f'Thread-{i}') for i in range(10))
    for thread in threads:
        thread.start()

# #здесь разделение

lock1 = threading.Lock()
lock2 = threading.Lock()
event1 = threading.Event()
semaphore1 = threading.Semaphore(value=5)
barrier1 = threading.Barrier(5)


def foo():
    with lock1:
        sleep(1)
        with lock1:
            print(threading.current_thread().name)


def bar():
    with lock2:
        sleep(1)
        with lock1:
            print(threading.current_thread().name)


def baz():
    lock1.acquire()
    lock1.acquire()
    print(threading.current_thread().name)
    lock1.release()
    lock1.release()


if __name__ == '__main__':
    timer = threading.Timer(interval=10, function=baz)
    timer.start()
#


def func1():
    sleep(5)
    event1.set()


def func2():
    event1.wait()
    event1.clear()
    print('enter')


if __name__ == '__main__':
    thread1 = threading.Thread(target=func1)
    thread2 = threading.Thread(target=func2)
    thread1.start()
    thread2.start()



