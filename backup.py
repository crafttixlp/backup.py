import os
import shutil
import datetime
import time

#frome time import sleep

#the name of the original folder
scr_dir = "C:/Users/crafttixlp/Desktop/fol1"

#the name of the backup folder
dest_dir = r'C:/Users/crafttixlp/Downloads/'

nowStr = datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
dest_dir2 = dest_dir + "backup-" + nowStr

files = os.listdir(dest_dir[:dest_dir.rfind("/")])

deleteKey = dest_dir[dest_dir.rfind("/")+1:]

files = os.listdir(scr_dir)

backup_time = 24
####################################################
####################################################

for file in files:
    if deleteKey+"backup-" in file:
        shutil.rmtree(dest_dir[:dest_dir.rfind("/")]+"/"+file)
    

#print(files)
shutil.copytree(scr_dir, dest_dir2)
print("finished copying !")