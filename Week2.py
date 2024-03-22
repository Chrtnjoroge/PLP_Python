# Initialize an empty list
my_list = []

# Appending the following elements to my_list: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("The list after appending:", my_list)
# Insert the value 15 at the second position in the list
my_list.insert(1, 15)
print("The list after inserting :", my_list)
# Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])
print("The list after extending:", my_list)
# Remove the last element from my_list
my_list.pop()
print("The list after popping:", my_list)
# Sort my_list in ascending order
my_list.sort()
print("The list after sorting:", my_list)
# Find and print the index of the value 30 in my_list
index_30 = my_list.index(30)
print("Index of 30 in my_list is:", index_30)
