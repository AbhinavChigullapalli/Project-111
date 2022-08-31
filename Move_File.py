import os
import shutil

from_dir='C:/Users/Abhinav C/Downloads'
to_dir='C:/Users/Abhinav C/Desktop/Document_Files'

list_of_files=os.listdir(from_dir)
print(list_of_files)

for files in list_of_files:
    name,extension=os.path.splitext(files)
    print(name)
    print(extension)