
# X - Ask for the folder name 
# X - Create the folder structure
# X - YYYYMMDD_Hike - <NAME>
# X - SubDirs - RX100, Sony, M
# X - Copy files from SDcards to subfolders
# 
# Backup on server
# Delete files from SDcards


import os 
import datetime 
from distutils.dir_util import copy_tree

RootName= datetime.datetime.now().strftime("%Y%m%d") + '_Hike - '
DirName = input("Directory name: " + RootName)
MainDir = "D:/zArchive/" + RootName + DirName
SubDirs = ['RX100', 'Sony', 'M']
camera_path = "E:/DCIM/100MSDCF"

def yes_or_no(question):
    answer = input(question + "(y/n): ").lower().strip()
    print("")
    while not(answer == "y" or answer == "n"):
        print("Input y or n")
        answer = input(question + "(y/n):").lower().strip()
        print("")
    if answer[0] == "y":
        return True
    else:
        return False


try:
    os.makedirs(MainDir)    
    print("Directory " , MainDir ,  " -- created ")

    for i in range(len(SubDirs)):
        os.makedirs(MainDir + "/" + SubDirs[i]) 

except FileExistsError:
    print("Directory " , MainDir ,  " -- already exists")  
    # exit()


# Copy First SD card
if yes_or_no("First SD card ready?"):
    copy_tree(camera_path, MainDir + "/RX100")
    print("DONE - " + MainDir + "/RX100")
else:
    print("OK")


# Copy Second SD card
if yes_or_no("Second SD card ready?"):
    copy_tree(camera_path, MainDir + "/Sony")
    print("DONE - " + MainDir + "/Sony")
else:
    print("OK")


# Open folder
os.startfile(MainDir)



