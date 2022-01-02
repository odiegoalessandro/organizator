from handler import Handler
import os
from watchdog.observers import Observer
import time

os.chdir("C:\\Users\\diego\\Downloads")

observer = Observer()
file_change_handler = Handler()
observer.schedule(event_handler = file_change_handler, path = os.getcwd(), recursive = False)
observer.start()

try:
  while True:
    time.sleep(1)
except KeyboardInterrupt:
  observer.stop()
finally:
  observer.join()