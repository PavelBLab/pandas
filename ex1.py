people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']
#print(people[0].split(' '))

'''
def split_title_and_name(person):
    newList = []
    for i in person:
        newList.append(i.split(' '))
    return newList

print(split_title_and_name(people))
'''

def split_title_and_name(person):
    title = person.split()[0]
    surname = person.split()[-1]
    return '{} {}'.format(title, surname)

print(list(map(split_title_and_name, people)))
