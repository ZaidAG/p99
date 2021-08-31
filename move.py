import os
import shutil
path='\\Users\\agsha\\Desktop\\python\\c99'
print("Before moving the file")
print(os.listdir(path))
source="\\Users\\agsha\\Desktop\\python\\c99\\newFolder"
destination="\\Users\\agsha\\Desktop\\python\\c99\\myFolder"
dest=shutil.move(source,destination)
print("After moving the file")
print(os.listdir(path))