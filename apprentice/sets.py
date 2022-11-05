
# Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)

my_list = [1, 3, 4, 4, 5, 5]
my_set = set(my_list)
print(my_set)

# Accessing set members
my_set = {1, 2, 3, 4, 5, 6, 6}
print(8 in my_set)

for i in my_set:
    print(i)

# Adding items
my_set = {1, 2, 3, 4, 5, 6, 6}
my_set.add(7)
print(my_set)

my_set.update({8, 9, 10})
print(my_set)

# Removing items
my_set = {1, 2, 3, 4, 5, 6, 6}
my_set.remove(6)
print(my_set)

my_set.discard(8)
print(my_set)

item_removed = my_set.pop()
print(item_removed)

#item_removed = my_set.pop(9)
#print(item_removed)

# Deleting a set
my_set={"a","b","c","c"}
my_set.clear()
print(my_set)

# set operations
first_set = {1, 2, 3, 4, 5}
second_set = {'one', 'two', 'three', 'four', 'five'}
combine_set = first_set.union(second_set)
print(combine_set)

first_set={'one','two','three'}
second_set={'three','four','one'}
print(first_set.intersection(second_set))
