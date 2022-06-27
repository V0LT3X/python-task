" Write a program to swap 2 numbers without taking third variable."

num1 = int(input("Enter a number 1 : "))
num2 = int(input("Enter a number 2  : "))

num1,num2 = num2,num1

print("After Swapping -> ")
print(f"number 1 = {num1},number 2 = {num2}")