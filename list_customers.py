import re

f = open("customers.txt", "rt")

customers = []
for line in f.readlines():
    name_match = re.search('[a-zA-Z ]+', line)
    if name_match is None:
        continue

    name = name_match.group().strip()
    if len(name) == 0:
        continue

    mobile_match = re.search(r'\d+', line)
    if mobile_match is None:
        continue

    mobile = mobile_match.group()

    customers.append((name, mobile))

f.close()
#print(customers)

for name, mobile in sorted(customers):
    print(f"{name:20} {mobile}")