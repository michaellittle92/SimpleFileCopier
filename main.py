import shutil
import os
    
original_folder = '/Users/michael/Desktop/FileMover/Original'
moved_folder_location = '/Users/michael/Desktop/FileMover/MovedLocation'
    
file_names = os.listdir(original_folder)
    
for file_name in file_names:
    shutil.move(os.path.join(original_folder, file_name), moved_folder_location)