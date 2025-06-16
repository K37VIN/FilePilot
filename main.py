import streamlit as st
from streamlit_tree_select import tree_select
from utils.list_files import list_files
from utils.check import check_exists
from utils.copy import copy_file
from utils.create import create_file
from utils.delete import delete_path
from utils.dir_create import create_directory
from utils.file_info import get_file_info
from utils.filter import filter_by_extension
from utils.move import move_file
from utils.read import read_file
from utils.rename import rename_file
from utils.write import write_file
from utils.zip import zip_folder
import os

st.set_page_config("📁 FilePilot", layout="wide")
st.title("📁 FilePilot")

root_dir = st.text_input("Enter Root Directory", value=os.getcwd())

if os.path.exists(root_dir):
    def build_tree_data(directory):
        """Build tree data structure for streamlit_tree_select"""
        try:
            items = []
            if os.path.isdir(directory):
                for item in os.listdir(directory):
                    item_path = os.path.join(directory, item)
                    if os.path.isdir(item_path):
                        items.append({
                            "label": item,
                            "value": item_path,
                            "children": build_tree_data(item_path)
                        })
            return items
        except (PermissionError, OSError):
            return []
    
    
    tree_data = {
        "label": os.path.basename(root_dir) or root_dir,
        "value": root_dir,
        "children": build_tree_data(root_dir)
    }

    selection = tree_select([tree_data])
    path = selection["checked"][0] if selection and selection.get("checked") else root_dir

    st.markdown(f"### Current Path: `{path}`")
    files = list_files(path)
    
    
    if files:
        files = [f for f in files if f is not None and f != ""]
    else:
        files = []
    
    st.write("### Contents:", files)

    tab1, tab2, tab3 = st.tabs(["📄 File Actions", "➕ Create", "ℹ️ Info"])

    with tab1:
        st.subheader("📄 File Actions")
        
        if files and len(files) > 0: 
            try:
                selected_file = st.selectbox("Select file", files, index=0)
                
                if selected_file and selected_file.strip():  
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        if st.button("Delete"):
                            result = delete_path(path, selected_file)
                            st.success(result)
                    
                    with col2:
                        new_name = st.text_input("Rename to")
                        if st.button("Rename") and new_name:
                            result = rename_file(path, selected_file, new_name)
                            st.success(result)
                    
                    with col3:
                        dest_dir = st.text_input("Move/Copy to")
                        if st.button("Move") and dest_dir:
                            result = move_file(path, selected_file, dest_dir)
                            st.success(result)
                        if st.button("Copy") and dest_dir:
                            result = copy_file(path, selected_file, dest_dir)
                            st.success(result)
                else:
                    st.error("Invalid file selection.")
            except Exception as e:
                st.error(f"Error with file selection: {str(e)}")
        else:
            st.info("No files in the current directory.")

    with tab2:
        st.subheader("➕ Create")
        new_file = st.text_input("New File Name")
        if st.button("Create File") and new_file:
            result = create_file(os.path.join(path, new_file))
            st.success(result)
        
        new_folder = st.text_input("New folder name")
        if st.button("Create Folder") and new_folder:
            result = create_directory(os.path.join(path, new_folder))
            st.success(result)

    with tab3:
        st.subheader("ℹ️ File Info / Viewer")
        
        if files and len(files) > 0: 
            try:
                info_file = st.selectbox("Select file to view info", files, key='info', index=0)
                
                if info_file and info_file.strip():  
                    full_path = os.path.join(path, info_file)
                    
                    if os.path.isfile(full_path):
                        try:
                            info = get_file_info(full_path)
                            if info:
                                st.write("**Size:**", info['Size'], "bytes")
                                st.write("**Created:**", info['Created'])
                                st.write("**Modified:**", info['Modified'])
                            
                            content = read_file(full_path)
                            if content is not None:
                                st.code(content, language='text')
                                data = st.text_area("Edit content:", value=content)
                                if st.button("Save Changes"):
                                    result = write_file(full_path, data, append=False)
                                    st.success(result)
                            else:
                                st.error("Could not read file content.")
                        except Exception as e:
                            st.error(f"Error processing file: {str(e)}")
                    else:
                        st.warning("Selected item is not a file.")
                else:
                    st.error("Invalid file selection.")
            except Exception as e:
                st.error(f"Error with file selection: {str(e)}")
        else:
            st.info("No files available to view.")

    st.divider()
    
    with st.expander("🔍 Filter Files by Extension"):
        ext = st.text_input("Enter extension (e.g., .txt)")
        if ext:
            try:
                filtered = filter_by_extension(path, ext)
                st.write("Filtered files:", filtered)
            except Exception as e:
                st.error(f"Error filtering files: {str(e)}")

    with st.expander("🗜️ Zip a Folder"):
        zip_name = st.text_input("Output Zip File Name")
        if st.button("Zip Folder") and zip_name:
            try:
                result = zip_folder(path, zip_name)
                st.success(result)
            except Exception as e:
                st.error(f"Error creating zip: {str(e)}")

else:
    st.error("Directory does not exist. Please enter a valid path.")