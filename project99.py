import os
import time
import shutil

def main():
    deleted_folders_count=0
    deleted_files_count=0

    path = 'C:/Users/saisripadmanabhuni/downloads/python'
    days =30
    seconds = time.time() - (days * 24 * 60 * 60)

    if os.path.exists(path):
     for root_folder , folders , files in  os.walk(path):
        if seconds >= get_file_or_folder_age(root_folder):
            remove_folder(root_folder)
            deleted_folders_count +=1
     else:
        if seconds >= get_file_or_folder_age(path):
             remove_file(path)
             deleted_files_count+=1
        else:
         print(f'"{path}"is not found')
        deleted_files_count +=1

        print(f"Total Folders Deleted:{deleted_folders_count}")
        print(f"Total Files Deleted:{deleted_files_count}")

def remove_folder(path):

    if not shutil.rmtree(path):
        print(f"{path} is removed successfully")
    else:
        print(f"Unable to Delete the"+path)

def remove_file(path):
    if not os.remove(path):
        print(f"{path} is removed successfully")
    else:
        print(f"Unable to Delete the"+path)

def get_file_or_folder_age(path):
    ctime = os.stat(path).st_ctime
    return ctime

main()