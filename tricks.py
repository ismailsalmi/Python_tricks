# Generate numbers inside list
print('Generate numbers inside list')
numbers = [num for num in range(0, 10)]
print(numbers)
print('===============================================================')

# Reverse string list tuple data
print('Reverse string list tuple data')
tpl = (1, 2, 3, 4, 5)
print(tpl[::-1])
print('===============================================================')

# From list a one string
print('From list a one string')
fruits = ['Banaba ', 'Raspberry ', 'Apple ', 'Orange ']
print(''.join(fruits))
print('===============================================================')

# Reverse variables values
print('Reverse variables values')
x, y = 'one', 1
print(x, y)
x, y = y, x
print(x, y)
print('===============================================================')

# Use enums without import library
print('Use enums without import library')
class Days:
    MO, TU, WE, TH, FR, SA, SU = \
        ('Monday', 'Tuesday', 'Wednesday',
         'Thursday', 'Friday', 'Saturday', 'Sunday')
print(Days.FR)
print('===============================================================')

# Find minimum number and maximum number in list
print('Find minimum number and maximum number in list')
ls = [num for num in range(0, 100, 5)]
print('MAX',min(ls), 'MIN ',max(ls))
print('===============================================================')

# Compare string arg
print('Compare string arg')
from collections import Counter
result = Counter(str(8+2)) == Counter(str(20-10))
print(result)
print('===============================================================')

# Merge two lists to one list
print('Merge two lists to one list')
ls1 = [1, 2, 3, 4, 5]
ls2 = ['a', 'b', 'c', 'd', 'e']
print([lists for lists in zip(ls1, ls2)])
print('===============================================================')

# Comparison
print('Comparison')
comp1 = (1 > 0 == 0)
print(comp1)
comp2 = (2 < 1 > 0)
print(comp2)
print('===============================================================')

# Convert list to string with slash separated
print('Convert list to string with slash separated')
lis = ["Monday", 15, 12, 1992]
print('/'.join(map(str, lis)))
print('===============================================================')

# Merge two Dictionaries in one dictionary
print('Merge two Dictionaries in one dictionary')
dic1, dic2 = {1:'a', 2:'b'},  {3:'c', 4:'d'}
dic1.update(dic2)
print(dic1)
print('===============================================================')

# The difference between the two Lists
print('The difference between the two Lists')
list1 = ['Zouheir', 'Samir', 'Hamid', 'Jamal']
list2 = ['Zouheir', 'Samir', 'Jamal', 'Ismail']
defferents = list(set(list1).symmetric_difference(list2))
print(defferents)
print('===============================================================')

# Removing duplicates items from a list
print('Removing duplicates items from a list')
listNumbers = (10, 30, 20, 15, 16, 18, 16)
print(list(set(listNumbers)))
print('===============================================================')

# Enumarate
print("Enumerate and remove duplicates items a list")
listString = ['Java', 'Kotlin', 'Python', 'Ruby', 'Ruby']
print(sorted([enume for enume in enumerate(set(listString))]))
print('===============================================================')

# Convert variable number and list to dictionary
print('Convert variable number and list to dictionary')
ids = range(0, 4)
listMumbers = ['Ismail', 'Samir', 'Noraddin', 'Yassin']
mergeToDict = dict(zip(ids, listMumbers))
print(mergeToDict)






