# read and write lock for a passage

import threading

class rw_lock:
	def __init__(self):
		self.r_lock = threading.Lock()
		self.w_lock = threading.Lock()
		self.reader = 0
		self.writer = False

	def write_acquire(self):
		self.w_lock.acquire()

	def write_release(self):
		self.w_lock.release()

	def read_acquire(self):
		self.r_lock.acquire()
		self.reader += 1
		if self.reader == 1:
			self.w_lock.acquire()
		self.r_lock.release()

	def read_release(self):
		self.r_lock.acquire()
		self.reader -= 1
		if self.reader == 0:
			self.w_lock.release()
		self.r_lock.release()



class ReadWriteLock:
    def __init__(self):
        self._read_ready = threading.Condition()
        self._changereader = threading.Lock()
        self._readers = 0
        
    def acquire_read(self):
        self._read_ready.acquire()
        self._changereader.acquire()
        try:
            self._readers+=1
        finally:
            self._read_ready.release()
            self._changereader.release()
    
    def release_read(self):
        self._changereader.acquire()
        try:
            self._readers-=1
            if not self._readers:
                self._read_ready.notifyAll()
        finally:
            self._changereader.release()
            
    def acquire_write(self):
        self._read_ready.acquire()
        while self._readers:
            self._read_ready.wait()
    
    def release_write(self):
        self._read_ready.release()