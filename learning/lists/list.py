#basics of lists
#index start from 0
subjects = ['Maths', 'cpp', 'DBMS', 'Office Automation']

print(subjects)

#access individual subject by index

print(subjects[2])


#negative index refers from end of the list
print(subjects[-1])


#slice of lists refers
print(subjects[1:3])

#modify list 

subjects[2] = "ASP.net"

print(subjects)