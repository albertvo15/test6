import threading, traceback, sys
class DebugLock(object):
    def __init__(self):
        self._lock = threading.Lock()
    def acquire(self):
        print >>sys.stderr, "acquired", self
        #traceback.print_tb
        self._lock.acquire()
    def release(self):
        print >>sys.stderr, "released", self
        #traceback.print_tb
        self._lock.release()
    def __enter__(self):
        self.acquire()
    def __exit__(self, type, value, traceback):
        self.release()


lock = DebugLock()

with lock:
  print "I'm atomic!"
