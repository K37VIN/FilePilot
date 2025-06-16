import os
import shutil


def move_file(src_dir,filename,dest_dir):
  try:
    shutil.move(os.path.join(src_dir,filename),os.path.join(dest_dir,filename))
    return "File moved successfully"
  except:
    return "Error while moving file"
  
  