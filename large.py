#Accept 3 numbers and display the largest number.
num1=int(input("enter 1st numbers:"))
num2=int(input("enter 2nd numbers:"))
num3=int(input("enter 3rd numbers:"))
if(num1>num2)and(num1>num3):
 largest = num1
elif(num2>num1)and(num2>num3):
 largest = num2
else:
 largest = num3
print("The largest number is",largest)
