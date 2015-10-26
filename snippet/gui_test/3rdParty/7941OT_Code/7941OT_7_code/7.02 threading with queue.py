"""
Code illustration: 7.02

Threading with Queue Simple Demo

Tkinter GUI Application Development Hotshot
""" 



import Queue
import threading

class Worker(threading.Thread):
   def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
 
   def run(self):
        while True:
            job = self.queue.get()
            self.taskHandler(job)
 
   def taskHandler(self, job):
        print 'doing task %s'%job
        self.queue.task_done()
       
def main(tasks):
    queue = Queue.Queue()
    #populate queue with tasks 
    for task in tasks:
        queue.put(task)
    # create a list of threads and pass the queue as its argument
    for i in range(6):
        mythread = Worker(queue)
        #mythread.setDaemon(True)
        mythread.start()

    # wait for the queue to finish
    queue.join()
    print 'all tasks completed'
 
if __name__ == "__main__":
    tasks = 'A B C D E F'.split()
    main(tasks)