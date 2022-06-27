"Write a program to swap 2 numbers using third variable"

num1 = int(input("Enter a number 1 : "))
num2 = int(input("Enter a number 2 : "))

temp = num2
num2 = num1
num1 = temp

print("After Swapping -> ")
print(f"number 1 = {num1},number 2 = {num2}")