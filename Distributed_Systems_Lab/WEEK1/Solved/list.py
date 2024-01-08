list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print (list) # Prints complete list
print (list[0]) # Prints first element of the list
print (list[1:3]) # Prints elements starting from 2nd till 3rd
print (list[2:]) # Prints elements starting from 3rd element
print (tinylist * 2) # Prints list two times
print (list + tinylist) # Prints concatenated lists

# Functions & Methods in LIST

# add an element
list = ['physics', 'chemistry', 1997, 2000]
list.append('maths')
print(list)

# To delete an element in a list
del list[2]
print(list)

# To check a data in a list,
print("in operator: ", 'physics' in list)
print("in operator: ", 'english' in list)
print("length: ", len(list))
print("count: ", list.count('physics'))

# modifying lists
list = ['physics', 'chemistry', 1997, 2000]
list.pop()
print("pop: ",list)
list.insert (2, 'maths')
print("insert: ", list)
list.remove('chemistry')
print("remove: ", list)
list.reverse()
print("reverse: ", list)
