#wap to store a word meaning in a python dictionary
#   table : "a piece of furniture", "list of facts and figures"
#   cat : "a small animal"
'''
dict1 = {
    "table" : ("a piece of furniture","list of facts and figures"),
    "cat" : "a small animal"
}

print(dict1.get("table"))
print(dict1.items())
'''
#wap to enter a 3 subject marks from the user and store them in a dictionary.
#start with an empty dictionary and add one by one.
#use subject as a key and marks as values

subjects = {}

a = input("maths :")
b = input("english :")
c = input("science :")

subjects.update({
    "Maths" : a,
    "English" : b,
    "Science" : c
})

print(subjects)
