def create_file(path):
  try:
     open(path,"w").close()
     return "File created successfully."
  except:
     return "Error creating file."
  

