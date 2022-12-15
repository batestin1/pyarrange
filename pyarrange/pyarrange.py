
#############################################################################################################################
#   filename:pyarrange.py                                                       
#   created: 2022-12-15                                                              
#   import your librarys below                                                    
#############################################################################################################################


import glob
import os
import shutil
import sys

def arrange(path=input("path: ").replace('\\','/')):
    #C:\Users\Bates\Pictures
    #path = input("").replace('\\','/')
    #path = "C:/Users/Bates/Pictures"
    for files in glob.glob(f"{path}/*"):
        files_replace = files.replace('\\','/')
        extension = os.path.splitext(files_replace)[1]
        if not os.path.exists(f"{path}/{extension.replace('.','')}"):
                    os.makedirs(f"{path}/{extension.replace('.','')}")
        for filepath in glob.iglob(f"{path}/*{extension}"):
                new = f"{path}/{extension.replace('.','')}"
                try:
                    if filepath.endswith(f"{extension}"):
                        shutil.move(filepath,new)
                except:
                    pass
    return print("Files Organized Successfully")