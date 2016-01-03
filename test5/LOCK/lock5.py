
import traceback
from threading import Lock

class DebugLock():
  def __init__(self, lock=None):
    self.lock = lock or Lock()

    # normally done with __dict__
    for command in dir(self.lock):
      self.__dict__[command] = getattr(self.lock, command)

X = DebugLock()
y = X.lock

Y = DebugLock(y)
X.acquire()
Y.acquire()
X.release()
Y.release()
