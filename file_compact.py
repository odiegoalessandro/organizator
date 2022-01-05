from file_compact_handler import FileCompactHandler
from observers.observer import Observer
import os

if __name__ == "__main__":
  if os.path.exists("C:\\Users\\diego\\Downloads\\compact") == False:
    os.chdir("C:\\Users\\diego\\Downloads")
    os.mkdir("compact")
  os.chdir("C:\\Users\\diego\\Downloads\\compact")
  observer = Observer(FileCompactHandler(), os.getcwd())
  observer.start()