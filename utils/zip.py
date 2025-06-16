import shutil 

def zip_folder(folder_path,output_zip):
  try:
    shutil.make_archive(output_zip,'zip',folder_path)
    return f"The provided folder has been zipped and saved as {output_zip}.zip"
  except:
    return "Error while zipping the folder"
  
  