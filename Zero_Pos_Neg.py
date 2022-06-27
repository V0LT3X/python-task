"Take a number and check whether it is zero, positive or negative"

def check(num):
    if num==0:
        print("Number is Zero ")
    elif num>0:
        print("Number is Positive")
    else:
        print("Number is Nagetive")

num = int(input("Enter a number : "))
check(num)