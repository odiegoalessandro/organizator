from watchdog.events import FileSystemEventHandler
import os
from utils import Utils

class FileOrganizerHandler(FileSystemEventHandler):
  def on_any_event(self, event):
    pass
  
  def on_created(self, event):
    pass

  def on_deleted(self, event):
    pass

  def on_modified(self, event):
    print(event)
    if os.path.isdir(event.src_path):
      return
    
    elif Utils.is_text_file(event) == True:
      path = Utils.make_folder("texto")
      Utils.move_file(event, path)

    elif Utils.is_code_file(event) == True:
      path = Utils.make_folder("codigos")
      Utils.move_file(event, path)

    elif Utils.is_doc_file(event) == True:
      path = Utils.make_folder("documentos")
      Utils.move_file(event, path)

    elif Utils.is_executable_file(event) == True:
      path = Utils.make_folder("executavel")
      Utils.move_file(event, path)

    elif Utils.is_image_file(event) == True:
      path = Utils.make_folder("imagens")
      Utils.move_file(event, path)

    elif Utils.is_mp3_file(event) == True:
      path = Utils.make_folder("audio")
      Utils.move_file(event, path)

    elif Utils.is_pdf_file(event) == True:
      path = Utils.make_folder("pdf")
      Utils.move_file(event, path)

    elif Utils.is_presentation_file(event) == True:
      path = Utils.make_folder("apresentação")
      Utils.move_file(event, path)

    elif Utils.is_spreadsheet_file(event) == True:
      path = Utils.make_folder("excel")
      Utils.move_file(event, path)

    elif Utils.is_video_file(event) == True:
      path = Utils.make_folder("video")
      Utils.move_file(event, path)
      
    elif Utils.is_compact_file(event) == True:
      path = Utils.make_folder("compact")
      Utils.move_file(event, path)