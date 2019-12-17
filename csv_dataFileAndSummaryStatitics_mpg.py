import csv
#print('all ok')

#This is to set a floating point precision for printing. It sets the floating point to 2 decimal points
#%precision 2 doesn't work

with open('mpg.csv') as csvfile:
    cars = list(csv.DictReader(csvfile))
    # print(cars)
print(cars[:3])

print('################################# NEXT EXAMPLE ################################')
'''csv.Dictreader has read in each row of our csv file as a dictionary. len shows that our list is comprised of 234 dictionaries'''
print(len(cars))

print('################################# NEXT EXAMPLE ################################')
'''keys gives us the column names of our csv'''
print(cars[0].keys())

print('################################# NEXT EXAMPLE ################################')
'''
This is how to find the average cty fuel economy across all cars. All values in the dictionaries
are strings, so we need to convert to float.
'''
sumNumber = 0
for dictMpg in cars:
    #print(float(dictMpg['mpg_miles_per_gallon']))
    sumNumber = sumNumber + float(dictMpg['mpg_miles_per_gallon']) / len(cars)
    # print(sumNumber)
print(sumNumber)
print(sum(float(dictMpg['mpg_miles_per_gallon']) for dictMpg in cars)/ len(cars))

print('################################# NEXT EXAMPLE ################################')
'''''''!!!!!!!!!!!!!!! Use "set" to return the unique values for the number of cylinders the cars in our dataset have'''
cylinders = set(dictMpg['cylinders'] for dictMpg in cars)
print(cylinders)

print('################################# NEXT EXAMPLE ################################')
'''Here's a more complex example where we are grouping the cars by number of cylinder, and finding the average cty mpg for each group'''
listCylindersCars = list()
for cylinder in cylinders:  # iterate over all the cylinder levels
    sumMpg = 0
    cylinderTypeCount = 0
    for dictionary in cars: # iterate over all dictionaries
        if dictionary['cylinders'] == cylinder: # if the cylinder level type matches,
            sumMpg += float(dictionary['cylinders']) # add the cty mpg
            cylinderTypeCount += 1
    listCylindersCars.append((cylinder, sumMpg / cylinderTypeCount))  # append the tuple ('cylinder', 'avg mpg')
    listCylindersCars.sort(key=lambda x: x[0])
    #print(sumMpg)
    #print(cylinderTypeCount)
print(listCylindersCars)

print('################################# NEXT EXAMPLE ################################')
'''Use set to return the unique values for the class types in our dataset.
vehicleYear = print(set(dictionary[key] for dictionary in cars for key in dictionary))'''
for value in cars[0].values():
    print(value)
    print(type(value))
    print('--------------')
#print(vehicleclass)

print('################################# NEXT EXAMPLE ################################')
modelYear = set(dictionary['model_year'] for dictionary in cars)
#print(modelYear)

modelYearFuelSpend = list()
for year in modelYear:
    sumFuelSpend = 0
    for dictionary in cars:
        if dictionary['model_year'] == year:
            sumFuelSpend += float(dictionary['mpg_miles_per_gallon'])
    modelYearFuelSpend.append((year, sumFuelSpend))

newList = []
for key, value in modelYearFuelSpend:
    newList.append((value, key))
newList.sort(reverse=True)
print(newList)
print('################################# IMPORTANT LAMBDA ################################')
sortedList = sorted(modelYearFuelSpend, key=lambda x: x[1], reverse=True) #filtered by values in turple
print(sortedList)
