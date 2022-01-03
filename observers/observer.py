from time import time
from watchdog.observers import Observer as WatchDogObserver

class Observer:
  def __init__(self, handler, path):
    self.handler = handler
    self.path = path
    self.observer = WatchDogObserver()
  
  def start(self):
    self.observer.schedule(self.handler, self.path, False)
    try:
      self.observer.start()
      while True:
        time.sleep(1)
    except KeyboardInterrupt:
      self.observer.stop()
    finally:
      self.observer.join()
  
  def stop(self):
    self.observer.stop()
    self.observer.join()