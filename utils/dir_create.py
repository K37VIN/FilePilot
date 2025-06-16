import os

def create_directory(path):
  try:
    os.makedirs(path,exists_ok=True)
    return "Directory created sucessfully"
  except:
    return "Error creating directory"
  

  