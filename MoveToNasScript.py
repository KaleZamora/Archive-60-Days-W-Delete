import shutil
import os
from datetime import datetime
import time

today = datetime.now()
now = time.time()
today2 = today.strftime('%Y')
today3 = today.strftime('%m-%Y')
path = "Put Parent Folder of Folders to Be Archived Here"
path2 = "Put New Location Of Archive Path Here" + today2 +"\\" + today3
holder = []

for i in os.listdir(path):
    path3 = os.path.join(path, i)
    holder = holder.append(path3)
    if os.stat(path3).st_mtime < now - (60*86400) and os.path.isdir(path3):
        shutil.copytree(path3, os.path.join(path2, i))
for i in holder:
    os.remove(holder[i])
