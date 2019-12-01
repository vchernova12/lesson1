students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
names = []
print(type(names))
for student in range(len(students)):
    names.append(f'{(students[student]["first_name"])}')
print(names)
uniq_names = []
for student in range(len(students)):
    print(uniq_names)
    if student not in uniq_names:
        uniq_names.append(f'{(students[student]["first_name"])}')
        print(uniq_names)
        #print names.count(students[student]["first_name"]))
print(uniq_names)
  