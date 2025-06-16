import os

def rename_file(directory,old_name,new_name):
  try:
    os.rename(os.path.join(directory,old_name),os.path.join(directory,new_name))
    return "Renamed successfully"
  except:
    return "Rename failed"
  
