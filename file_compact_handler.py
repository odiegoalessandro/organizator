import shutil
from watchdog.events import FileSystemEventHandler

class FileCompactHandler(FileSystemEventHandler):
  def on_any_event(self, event):
    pass
  def on_closed(self, event):
    pass
  def on_created(self, event):
    pass
  def on_deleted(self, event):
    pass
  def on_moved(self, event):
    pass
  def on_modified(self, event):
    if event.is_directory:
      shutil.move(event.src_path, "C:\\Users\\diego\\Documents")