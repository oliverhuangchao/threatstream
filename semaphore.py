import threading
import random
import time



class mythread(threading.Thread):
    
    def __init__(self,name):
        self.interval = random.randrange(1,6)
        threading.Thread.__init__(self)
        self.name = str(name)

    def run(self):
        sema.acquire()
        seat = avail_table.pop()
        print "%s seats in %s" % (self.name,seat)
        time.sleep(self.interval)
        avail_table.append(seat)
        sema.release()







n = 10
avail_table = ['A','B','C','D','E']
threat_list = []
sema = threading.Semaphore(len(avail_table))
for i in range(10):
    threat_list.append(mythread(i))

for item in threat_list:
    item.start()
    #item.join()
