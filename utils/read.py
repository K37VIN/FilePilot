def read_file(path):
  try:
   with open(path,"r") as f:
     return f.read()
  except:
    return "Error reading the file."
  