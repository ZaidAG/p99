import os
import shutil
path='\\Users\\agsha\\Desktop\\python\\c99'
print("Before copying the file")
print(os.listdir(path))
source="\\Users\\agsha\\Desktop\\python\\c99\\text.txt"
destination="\\Users\\agsha\\Desktop\\python\\c99\\copy.txt"
dest=shutil.copy(source,destination)
print("After copying the file")
print(os.listdir(path))