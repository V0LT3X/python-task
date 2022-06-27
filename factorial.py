
def factorial(num):
    if num<0:
        return 0
    elif num==0 or num==1:
        return 1
    else:
        return num * factorial(num-1)

        # fact = 1
        # while(num>1):
        #     fact *=num
        #     num -=1
        # return fact

num = int(input("Enter a number : "))
print(factorial(num))
