#Assigning elements to a list

names=['Aman','Yash','Daksh','Shreya']
print(names)
names[2]='Parag'
names[3]='Vatsala'
print(names)
names.append('Shanu')
print(names)


#Accessing elements from a tuple

mytuple=('C','C++','Python','Java','Matlab')
print(mytuple[3])
print(mytuple[4])


#Deleting different dictionary elements

mydict={'Apple':'Red','Banana':'Yellow','Grape':'Purple'}
del mydict['Banana']
del mydict['Grape']
print(mydict)
