total = 0
for i in range(5):
    try:
        n = int(input("Enter a number :"))
        total += n
    except ValueError as ex:
        print('Invalid number!')

print(total)