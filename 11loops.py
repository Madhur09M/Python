#wap to print numbers from 1 to 100
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

tup2 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
y = 36
idx = 0
for num in tup2:
    if(num==y):
         print("Item found at index :",idx)
    idx += 1
