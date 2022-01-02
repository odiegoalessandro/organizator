import os
import shutil

def extension_type(event):
  return event.src_path[event.src_path.rindex('.') + 1:]

class Utils:
  def is_text_file(event):
    if extension_type(event) == 'txt':
      return True
    return False

  def is_pdf_file(event):
    if extension_type(event) == 'pdf':
      return True
    return False

  def is_mp3_file(event):
    if extension_type(event) == 'mp3':
      return True
    return False

  def is_image_file(event):
    if extension_type(event) in ('png', 'jpg', 'bmp', 'gif', 'raw', 'svg', 'jpeg'):
      return True
    return False

  def is_video_file(event):
    if extension_type(event) in ('mov', 'mp4', 'avi', 'flv'):
      return True
    return False

  def is_doc_file(event):
    if extension_type(event) in ('doc', 'docx'):
      return True
    return False

  def is_spreadsheet_file(event):
    if extension_type(event) in ('xls', 'xlsx'):
      return True
    return False

  def is_presentation_file(event):
    if extension_type(event) in ('ppt', 'pptx'):
      return True
    return False

  def is_code_file(event):
    if extension_type(event) in ('py', 'cs', 'js', 'php', 'html', 'sql', 'css', 'ts', 'tsx', 'json'):
      return True
    return False

  def is_executable_file(event):
    if extension_type(event) in ('exe', 'msi'):
      return True
    return False

  def is_compact_file(event):
    if extension_type(event) in ('rar', 'zip'):
      return True
    return False

  def make_folder(foldername):
    if os.path.exists(foldername) == True:
      return os.getcwd() + os.sep + str(foldername)
    else:
      os.mkdir(str(foldername))

  def move_file(event, path):
    try:
      shutil.move(event.src_path, path)
    except:
      pass