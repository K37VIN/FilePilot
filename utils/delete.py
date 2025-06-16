import os
import shutil

def delete_path(directory,name):
   path=os.path.join(directory,name)
   try:
      if os.path.isdir(path):
         shutil.rmtree(path)
      elif os.path.isfile(path):
         os.remove(path)
         return "Deleted successfully"
   except:
      return "Delete failed"
   