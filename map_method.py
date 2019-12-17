people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    personList = person.split(' ')
    title = person.split()[0]
    lastName = person.split()[-1]
    #return title + ' ' + lastName
    return '{} {}'.format(title, lastName)

print(list(map(split_title_and_name, people)))
