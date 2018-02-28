
students = [
     {'first_name':  'Michael', 'last_name': 'Jordan'},
     {'first_name': 'John', 'last_name': 'Rosales'},
     {'first_name': 'Mark', 'last_name': 'Guillen'},
     {'first_name': 'KB', 'last_name': 'Tonel'}
]

def dictionary1(x):
    for i in x:
        print i['first_name'], i['last_name']

dictionary1(students)


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name': 'Jordan'},
     {'first_name': 'John', 'last_name': 'Rosales'},
     {'first_name': 'Mark', 'last_name': 'Guillen'},
     {'first_name': 'KB', 'last_name': 'Tonel'}
  ],
 'Instructors':[
     {'first_name': 'Michael', 'last_name': 'Choi'},
     {'first_name': 'Martin', 'last_name': 'Puryear'}
  ]
 }

def dictionary2(x):
    for key, data in users.items():
        print key
        count = 0
        for value in data:
            count += 1
            counter = value['first_name'] + value['last_name']
            print count, '-', value['first_name'], value['last_name'], '-', len(counter)

dictionary2(users)
