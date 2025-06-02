# while loop

# #wap to print numbers from 1 to 100
'''
i = 1

while i<=100 :
    print(i)
    i += 1
'''
#wap to print numbers from 100 to 1
'''
n = 100

while n>=1 :
    print(n)
    n -= 1
'''
#wap to print multiplicatation table of a number p
'''
p = int(input("Enter the number :"))
q = 1

while q<=10 :
    print(p*q)
    q += 1
'''
#wap to print the elements of the following list using a loop
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''
list1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

r = 0
while r <= len(list1)-1 :
    print(list1[r])
    r += 1
'''
#wap to search an eklement in the following tupple using a loop
#(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
'''
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

s = 0
x = 49
while s <= len(tup)-1 :
    if(tup[s] == x):
        print("Found at index :",s)
    s += 1
'''
#wap to print the sum of n natural numbers
'''
sum = 0
n = int(input("Enter the num : "))
while n>=1 :
    sum = sum+n
    n -= 1
print("Sum :",sum)
'''
#for loop

#wap to print the elements of the following list using a loop
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''
list2 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for val in list2:
    print(val)
'''
#wap to search an eklement in the following tupple using a loop
#(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
'''
tup2 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
y = 36
idx = 0
for num in tup2:
    if(num==y):
         print("Item found at index :",idx)
    idx += 1
'''

#range() function
'''
for i in range(10):              #range(stop)
      print(i)                   #prints 0-9

for j in range(3,10):            #range(start, stop)
    print(j)                     #print 3-9

for k in range(3, 10, 2):        #range(start, stop, step_size)
    print(k)                     # prints 3, 5, 7, 9
'''

#wap to print all the even numbers from 1 to 10
'''
for num in range(2, 11, 2):
    print(num)
'''

#wap to print all the numbers from 1 to 100
'''
for d in range(101):
    print(d)
'''

#wap to print all the numbers from 100 to 1
'''
for e in range(100, 0, -1):
    print(e)
'''

#wap to print multiplicatation table of a number f
'''
f = int(input("Enter the number :"))

for g in range(10):
    print(f*(g+1))
'''

#wap to print the factorial of n natural numbers

n = int(input("Enter the number : "))
factorial = 1

for n in range(n,1,-1):
    factorial = factorial*n

print("Factorial :",factorial)
