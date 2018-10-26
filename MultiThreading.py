from threading import Thread
import time

class MyThread (Thread):
   def __init__(self, threadID, name, counter, delay):
      Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
      self.delay = delay
      
   def run(self):
      print ("Starting {}".format(self.name))
      print_time(self.name, self.counter, self.delay)
      print ("Exiting " + self.name)

def print_time(threadName, counter, delay):
   while counter:
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1


# Create new threads
thread1 = MyThread(1, "Thread-1", 5, 1)
thread2 = MyThread(2, "Thread-2", 5, 2)

# Start new Threads
thread1.start()
thread2.start()

print("Exiting Main Thread")
