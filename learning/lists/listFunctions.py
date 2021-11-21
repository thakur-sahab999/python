some_numbers = [1, 2, 3, 4, 5]
subjects = ['Maths', 'Cpp', 'Cpp', 'DBMS', 'Office Automation']

#print
print(subjects)

#extend the lists
#subjects.extend(some_numbers)
#print(subjects)

#append item to the end of list
subjects.append("visual studios")
print(subjects)

#insert item

subjects.insert(2, 'drawing')
print(subjects)

#remove item
subjects.remove("drawing")
print(subjects)

#pop an item from end of list
subjects.pop()
print(subjects)

#check for items that

print(subjects.index('DBMS'))

#counts the numbers of time item appeared in the lists

print(subjects.count('cpp'))

#sort the list 

subjects.sort()
print(subjects)

#reverse the lists
subjects.reverse()
print(subjects)

#copy the list
subjects2 = subjects.copy()
print(subjects2)