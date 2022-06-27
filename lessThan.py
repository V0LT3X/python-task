"""Take a number check if a number is less than 100 or not.
If it is less than 100 then check if it is odd or even."""

num = int(input("Enter a number : "))

if num<100:
    print("Number is less than 100")
    if num%2==0:
        print("Number is Even ")
    else:
        print("Number is Odd")
else:
    print("Number is not less than 100")