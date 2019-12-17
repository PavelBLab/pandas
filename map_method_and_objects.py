class Person:
    department = 'School of Information' #a class variable

    def set_name(self, newName): #a method
        self.name = newName
        return newName
    def set_location(self, newLocation):
        self.location = newLocation
        return newLocation

person = Person() #create instance of class Person
#Person().set_name('Christopher Brooks')
#or

name = person.set_name('Christopher Brooks')
location = person.set_location('Ann Arbor, MI, USA')

print('{} live in {} and works in the department {}'.format(name, location, person.department))

print('################################# NEXT EXAMPLE ################################')
'''
Here's an example of mapping the min function between two lists.
'''

store1 = [10.00, 11.00, 12.34, 2.34]
store2 = [9.00, 11.10, 12.34, 2.01]

cheapestStore = map(min, store1, store2)
print(cheapestStore)

'''Now let's iterate through the map object to see the values.'''
for i in cheapestStore:
    print(i)
