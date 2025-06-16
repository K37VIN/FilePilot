import os
from datetime import datetime


def get_file_info(path):
  try:
    return {
      "Size":os.path.getsize(path),
      "Created":datetime.fromtimestamp(os.path.getctime(path)),
      "Modified":datetime.fromtimestamp(os.path.getmtime(path))
    }
  except:
    return None