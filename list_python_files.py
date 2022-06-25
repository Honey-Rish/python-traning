import os

STARTDIR = r'c:\classroom\may17\demo'  # Raw string

allentries = os.walk(STARTDIR)

count = 0
for (dirname, folders, files) in allentries:
    for file in files:
        if file.endswith(".py"):
            print(dirname + '\\' + file)
            count += 1

print(f"Count = {count}")