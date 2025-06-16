import os 
import shutil

def copy_file(src_dir,filename,dest_dir):
  try:
    shutil.copy2(os.path.join(src_dir,filename),os.path.join(dest_dir,filename))
    return "File copied successfully"
  except:
    return "Error in copying files"
  
  