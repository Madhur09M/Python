# check if the number input by the user is odd or even
'''
num = int(input("Enter a number : "))

if(num%2 == 1):
    print("number is odd")
else:
    print("number is even")
'''

#wap to find the greatest of three numbers enterde by the user
'''
num1 = int(input("Enter the 1st number : "))
num2 = int(input("Enter the 2nd number : "))
num3 = int(input("Enter the 3rd number : "))

if(num1<num2):                  #if num1 < num2
    if(num2<num3):
        print(num3)
    else:
        print(num2)
elif(num1>num2):                #if num1 > num2  
    if(num1>num3):
        print(num1)
    else:
        print(num3)
else:                           #if num1 = num2
    if(num1>num3):
        print(num1)
    else:
        print(num3)
'''

#wap to check if a number is a multiple of 7 or not

num4 = int(input("Enter a number : "))

if(num4%7 == 0):
    print("Number is the multiple of 7")
else:
    print("Number is not the multiple of 7")