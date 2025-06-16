import os

def list_files(directory):
  try:
    return os.listdir(directory)
  except FileNotFoundError:
    return []
  