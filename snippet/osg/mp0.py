#-*- coding:utf-8 -*-
from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name: %s '% __name__)
    if hasattr(os, 'getppid'):  # only available on Unix
        print('parent process: %d'% os.getppid())
    print('process id:%d'% os.getpid())

def f(name):
    info('function f')
    print('hello %s'% name)

if __name__ == '__main__':
    info('main line')
    print("start process")
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
    print("process end")
