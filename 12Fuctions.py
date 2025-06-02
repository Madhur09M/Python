#avg of 3 numbers
'''
def avg(a,b,c):
    avg = (a+b+c)/3
    return avg

print(avg(2,2,2))
print(avg(9,8,7))
'''
#wap to calculate the length of the list
'''
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8]

def calc_len(list):
    print(len(list))

calc_len(list1)
calc_len(list2)
'''
#wap to print all the elements of the list in the single line
'''
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8]
i=1

def ele_list(list):
    for i in list:
        print(i, end =" ")

ele_list(list1)
ele_list(list2)
'''

#wap to find the factorial of n
'''
def calc_fact(i):
    factorial = 1
    for n in range(1, i+1):
        factorial = n*factorial
    return factorial

print("Factorial :",calc_fact(5))
'''
#wap to convert the USD into INR
'''
def cur_conv(USD):
    INR = USD*85.35
    return INR

print("INR :",cur_conv(10))
'''
#wap to check whether the number is even or odd
'''
def num(n):
    if n%2 == 0:
        print("EVEN")
    else:
        print("ODD")

num(5) 
num(1246)
'''

#Recursion
#ex.1
'''
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)
'''
#factorial using recursion
'''
def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return fact(n-1)*n

print(fact(5))
'''
#wap to find the sum of n natural numbers using recursion
'''
def sum(n):
    if n==0 :
        return 0
    return n + sum(n-1) 

print(sum(5))
'''
#wap to print all the elements of the list

def list_ele(list, idx=0):
    if (idx == len(list)):
        return
    print(list[idx])
    list_ele(list, idx+1)

list1 = [1, 2, 3, 4]

list_ele(list1)
