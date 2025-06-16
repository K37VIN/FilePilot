def write_file(path,data,mode):
  try:
    with open(path,mode) as f:
      f.write(data + '\n')
    return "Write successful"
  except:
    return "Write failed"
  
  