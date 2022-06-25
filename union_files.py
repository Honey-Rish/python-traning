with open("email1.txt", "rt") as f1, open("email2.txt", "rt") as f2:
    unique_lines = set(f1.readlines()) | set(f2.readlines())

for line in sorted(unique_lines):
    print(line, end='')