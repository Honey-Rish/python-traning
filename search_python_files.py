import os


def fileHasString(filename, words):
    try:
        with open(filename, 'rt') as f:
            contents = f.read()
            for w in words:
                if w in contents:
                    return True

            return False
    except:
        return False


STARTDIR = r'c:\classroom\may17\demo'  # Raw string
SEARCHSTRING = ['__eq__', '__str__']
allentries = os.walk(STARTDIR)

for (dirname, folders, files) in allentries:
    for file in files:
        if file.endswith(".py"):
            filename = dirname + '\\' + file
            if fileHasString(filename, SEARCHSTRING):
                print(filename)