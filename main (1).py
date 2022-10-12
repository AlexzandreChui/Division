# Created By: Alex Chui with help from Owen Whalley
# Created On: 2022/10/12
# This code asks the user for two numbers to calculate the quotient of.
x = int(input("Enter your first number: "))
y = int(input("Enter your second number: "))

count = -1
# This code tells the computer to calculate the quotient using only subtraction.
while x > 0:
  x -= y
  count += 1
# This code tells the computer to calculate the remainder.
if x < 0:
  for i in range(1):
    x += y
    break

print("The quotient is "+str(count)+" with a remainder of "+str(x))