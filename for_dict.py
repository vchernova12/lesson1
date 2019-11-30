students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
names = list()
print(type(names))
for number_in_students in range(len(students)):
    names += (students[number_in_students]['first_name'])
    print(names)
    print(students[number_in_students]['first_name'])

    #for student in students[number_in_students]['first_name']:
