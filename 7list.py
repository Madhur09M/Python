#wap to ask the user to enter names of there three favourite movie and store them in a list
'''
mov1 = input("Enter the name of first movie : ")
mov2 = input("Enter the name of second movie : ")
mov3 = input("Enter the name of third movie : ")

list = []

list.append(mov1)
list.append(mov2)
list.append(mov3)

print(list)

'''

#wap to check whether a list contains the elements of a palindrome(Hint : use list.copy())

list1 = [1,2,3,2,1]
list2 = list1.copy()
list2.reverse()

if(list1 == list2):
    print("list contains elements of palindrome")
else:
    print("list does not contains elements of palindrome")
