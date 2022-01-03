from observers.observer import Observer
from handler import Handler
import os

if __name__ == "__main__":
  os.chdir("C:\\Users\\diego\\Downloads")
  path = os.getcwd()
  handler = Handler()
  observer = Observer(Handler(), os.getcwd())
  observer.start()