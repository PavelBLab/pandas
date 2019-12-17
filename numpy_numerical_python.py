import numpy as np
#print('OK')

'''Creating Arrays'''
print('Creating Arrays')
myList = [1, 2, 3]
x = np.array(myList)
print(type(x))
print(x, '\n')

'''Or just pass in a list directly'''
print('Or just pass in a list directly')
y = np.array([4,5,6])
print(y, '\n')

'''diag extracts a diagonal or constructs a diagonal array.'''
print('diag extracts a diagonal or constructs a diagonal array.')
print(np.diag(y), '\n')

print('################################# NEXT EXAMPLE ################################')
'''Pass in a list of lists to create a multidimensional array.'''
print('Pass in a list of lists to create a multidimensional array.')
z = np.array([[1,2,3],[4,5,6]])
print(z, '\n')

'''Use the shape method to find the dimensions of the array. (rows, columns)'''
print('Use the shape method to find the dimensions of the array. (number of rows, number of columns)')
print('shape', z.shape, '\n')

print('################################# NEXT EXAMPLE ################################')
'''arange/create returns evenly spaced values within a given interval.'''
print('arange returns evenly spaced values within a given interval.')
n = np.arange(0, 30, 2) # start at 0 count up by 2, stop before 30
print(n, '\n')

'''reshape returns an array with the same data with a new shape.'''
print('reshape(3, 5) returns an array with the SAME DATA with a new shape.')
print(n.reshape(3, 5), '\n') # 3 * 5 = 15 this is a number of items in array (should be exact 15)

print('################################# NEXT EXAMPLE ################################')
'''linspace returns evenly spaced numbers over a specified interval.'''
print('linspace(0, 4, 50) returns evenly spaced numbers over a specified interval.')
o = np.linspace(0, 4, 50) # return 9 evenly spaced values from 0 to 4
print(o, '\n')

'''resize changes the shape and size of array in-place.'''
print('resize(3, 3) changes the shape and size of array in-place.')
o.resize(3, 3)
print(o, '\n')

print('################################# NEXT EXAMPLE ################################')
'''ones returns a new array of given shape and type, filled with ones.'''
print('ones(3 -# arrays, 2 - # items) returns a new array of given shape and type, filled with ones.')
print(np.ones((3, 2)), '\n')

'''zeros returns a new array of given shape and type, filled with zeros.'''
print('zeros(2 -# arrays, 3 - # items) returns a new array of given shape and type, filled with zeros.')
print(np.zeros((2, 3)), '\n')

'''eye returns a 2-D array with ones on the diagonal and zeros elsewhere.'''
print('eye(4) returns a 2-D array with ones on the diagonal and zeros elsewhere. The difference between eye and diag that eye create a new array and diag reconstruct the old one')
print(np.eye(4), '\n')

print('################################# NEXT EXAMPLE ################################')
'''Create an array using repeating list (or see np.tile)'''
print('Create an array using repeating list (or see np.tile)')
print(np.array([1, 2, 3] * 3), '\n')

'''Repeat elements of an array using repeat.'''
print('Repeat elements of an array using repeat.')
print(np.repeat([1, 2, 3], 3), '\n')


print('################################# NEXT EXAMPLE ################################')
'''Combining Arrays'''
print('Combining Arrays')
p = np.ones([2, 3], float) # can be int
print(p, '\n')

'''Use vstack to stack arrays in sequence vertically (row wise).'''
print('Use vstack to stack arrays in sequence vertically (row wise).')
print(np.vstack([p, p+4, p*3]), '\n')

'''Use hstack to stack arrays in sequence horizontally (column wise).'''
print('Use hstack to stack arrays in sequence horizontally (column wise).')
print(np.hstack([p, 2*p]), '\n')

print('################################# NEXT EXAMPLE ################################')
'''Operations'''
print('Operations')

print(x + y) # elementwise addition     [1 2 3] + [4 5 6] = [5  7  9]
print(x - y) # elementwise subtraction  [1 2 3] - [4 5 6] = [-3 -3 -3]
print(x * y) # elementwise multiplication  [1 2 3] * [4 5 6] = [4  10  18]
print(x / y) # elementwise divison         [1 2 3] / [4 5 6] = [0.25  0.4  0.5]
print(x**2) # elementwise power  [1 2 3] ^2 =  [1 4 9]
x.dot(y) # dot product  1*4 + 2*5 + 3*6

z = np.array([y, y**2])
print(z)
print('array length', len(z), '\n') # number of rows of array

'''Let's look at transposing arrays. Transposing permutes the dimensions of the array.'''
print('Let\'s look at transposing arrays. Transposing permutes the dimensions of the array.')

'''The shape of array z is (2,3) before transposing.'''
print('The shape of array z is (2,3) before transposing.')
print('==> array shape (#rows, #columns)', z.shape, '\n')

'''Use .T to get the transpose. The number of rows has swapped with the number of columns.'''
print('Use .T to get the transpose. The number of rows has swapped with the number of columns.')
print(z.T)
print('==> array shape (#rows, #columns)', z.T.shape, '\n')

'''Use .dtype to see the data type of the elements in the array.'''
print('Use .dtype to see the data type of the elements in the array.')
print(z.dtype, '\n')

'''Use .astype to cast to a specific type.'''
print('Use .astype to cast to a specific type.')
z = z.astype('f') #f  = float
print(z.dtype, '\n')



print('################################# NEXT EXAMPLE ################################')
'''Math Functions'''
print('Math Functions')
a = np.array([-4, -2, 1, 3, 5])
print('array:', a)
print('sum:', a.sum())
print('max:', a.max())
print('min:', a.min())
print('mean:', a.mean())
print('standart deviation:', a.std(), '\n')

'''argmax and argmin return the index of the maximum and minimum values in the array.'''
print('argmax and argmin return the index of the maximum and minimum values in the array.')
print('index of the maximum values in the array:', a.argmax())
print('index of the minimum values in the array:', a.argmin())


print('################################# NEXT EXAMPLE ################################')
'''Indexing / Slicing'''
print('Indexing / Slicing')
s = np.arange(13)**2
print(s, '\n')

'''Use bracket notation to get the value at a specific index. Remember that indexing starts at 0.'''
print('Use bracket notation to get the value at a specific index. Remember that indexing starts at 0.')
print(s[0], s[4], s[-1], '\n')

'''Use : to indicate a range. array[start:stop]
Leaving start or stop empty will default to the beginning/end of the array.
'''
print('Use : to indicate a range. array[start:stop]. Leaving start or stop empty will default to the beginning/end of the array.')
print(s[1:5], '\n')

'''Use negatives to count from the back.'''
print('Use negatives to count from the back.')
print(s[-4:], '\n')

'''A second : can be used to indicate step-size. array[start:stop:stepsize]
Here we are starting 5th element from the end, and counting backwards by 2 until the beginning of the array is reached.
'''
print('A second : can be used to indicate step-size. array[start:stop:stepsize]. Here we are starting 5th element from the end, and counting backwards by 2 until the beginning of the array is reached.')
print(s[-5::-2])
print(s[:10:2], '\n')

'''Let's look at a multidimensional array.'''
print('Let\'s look at a multidimensional array.')
r = np.arange(36)
print(r)
r.resize((6, 6)) # 6*6 = 36
print('resize:(6,6)', r, '\n')

'''Use bracket notation to slice: array[row = index starts with 0, column = index starts with 0]'''
print('Use bracket notation to slice: array[row = index starts with 0, column = index starts with 0]')
print(r[2, 2], '\n')

'''And use : to select a range of rows or columns'''
print('And use : to select a range of rows or columns')
print(r[3, 3:6], '\n')

'''Here we are selecting all the rows up to (and not including) row 2, and all the columns up to (and not including) the last column.'''
print('Here we are selecting all the rows up to (and not including) row 2, and all the columns up to (and not including) the last column.')
print(r[:2, :-1], '\n')

'''This is a slice of the last row, and only every other element.'''
print('This is a slice of the last row, and only every second element starting from 0.')
print(r[-1, ::2])
print(r[:-1, 0:4:3], '\n') # every 3rd element starts from 3

'''We can also perform conditional indexing. Here we are selecting values from the array that are greater than 30. (Also see np.where)'''
print('We can also perform conditional indexing. Here we are selecting values from the array that are greater than 30. (Also see np.where)')
print(r[r > 30], '\n')

'''Here we are assigning all values in the array that are greater than 30 to the value of 30.'''
print('Here we are assigning all values in the array that are greater than 30 to the value of 30.')
r[r > 30] = 30
print(r, '\n')

print('################################# NEXT EXAMPLE ################################')
'''Copying Data'''
print('Copying Data')

'''Be careful with copying and modifying arrays in NumPy!
r2 is a slice of r'''
print('Be careful with copying and modifying arrays in NumPy!.r2 is a slice of r')
r2 = r[:3,:3]
print(r2, '\n')

'''Set this slice's values to zero ([:] selects the entire array)'''
print('Set this slice\'s values to zero ([:] selects the entire array)')
r2[:] = 0
print(r2, '\n')

'''r has also been changed!'''
print('r has also been changed!')
print(r, '\n')

'''To avoid this, use r.copy to create a copy that will not affect the original array'''
print('To avoid this, use r.copy to create a copy that will not affect the original array')
rCopy = r.copy()
print(rCopy, '\n')

'''Now when rCopy is modified, r will not be changed.'''
print('Now when rCopy is modified, r will not be changed.')
rCopy[:] = 10
print(rCopy, '\n')
print(r, '\n')

print('################################# NEXT EXAMPLE ################################')
'''Iterating Over Arrays'''
print('Iterating Over Arrays', '\n')

'''Let's create a new 4 by 3 array of random numbers 0-9.'''
print('Let\'s create a new 4 (rows) by 3 (colums) array of random numbers 0-9.')
test = np.random.randint(0, 10, (4,3))
print(test, '\n')

'''Iterate by row:'''
print('Iterate by row:')
for row in test:
    print(row)

'''Iterate by index:'''
print('Iterate by index:')
print(range(len(test)))
for index in range(len(test)):
    print(test[index])

'''Iterate by row and index:'''
print('Iterate by row and index:')
for row, index in enumerate(test):
    print('row:', row, 'index:', index)


'''Use zip to iterate over multiple iterables'''
print('Use zip to iterate over multiple iterables')
test2 = test**2
print(test2)
for i, j in zip(test, test2):
    print(i,'+',j,'=',i+j)
