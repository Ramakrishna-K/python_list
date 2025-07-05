# In Python, a list is an ordered, mutable (changeable) collection that allows duplicate elements.
# Creating a List
fruits = ['apple','banana','cherry']
numbers = [1,2,3,4,5]

mixed =[1,'helo',2.5,True]
empty_list = []
print(fruits)

# Accessing Elements in  list
print(fruits[0])
print(fruits[-1])

# Modifying Lists

fruits[1] ="blueberry"
print(fruits)

#  methods in lists etc
fruits.append("orange")
fruits.insert(1, "grape")
fruits.remove("apple")

print(fruits)

# lenth of a list
print(len(fruits))
