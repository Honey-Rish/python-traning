num1 = int(input("enter the number 1:"))
num2 = int(input("enter the number 2:"))



hcf = int(1)
for i in range(1, min(num1, num2)):
    # for checking of condtion #any variable count start from 0 to make sure it doesnt get subtract we use ac=1
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
if num1==0 or num2==0:
    print("please enter non zero numbers")

if hcf == 1:
    print("its a coprime")
else:
    print("not a coprime")

