lines = []
with open("test.txt", "rt") as f:
    for line in f.readlines():
        line = line.strip()
        if len(line) > 0:
            lines.append(line)


with open("test.txt", "wt") as f:
    for line in lines:
        f.write(line + "\n")
