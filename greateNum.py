"Take 2 numbers and display greatest number. (Also check equal number condition)"

num1 = int(input("Enter a number 1 : "))
num2 = int(input("Enter a number 2 : "))

if num1==num2:
    print("Both Numbers are equal ")
elif num1>num2:
    print(f"Number 1 = {num1} is greater than Number 2")
else:
    print(f"Number 2 =  {num2} is greater than Number 1")