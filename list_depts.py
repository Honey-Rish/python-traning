f = open("employees.txt", "rt")
depts = {}

for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) < 3:
        continue     # ignore line as we don't have enough data

    dno, name, salary = parts  # Unpacking

    if not salary.isdigit():
        continue   # Ignore line as invalid salary

    if dno in depts:
        total, names = depts[dno]  # unpack tuple
        total = total + int(salary)
        names.append(name)
        depts[dno] = (total, names)
    else:
        depts[dno] = (int(salary), [name])

f.close()

for dno, details in sorted(depts.items()):
    total, names = details
    print(f"{dno} {total:8} {','.join(names)}")