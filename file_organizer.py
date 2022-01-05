from observers.observer import Observer
from file_organizer_handler import FileOrganizerHandler
import os

if __name__ == "__main__":
  os.chdir("C:\\Users\\diego\\Downloads")
  observer = Observer(FileOrganizerHandler(), os.getcwd())
  observer.start()