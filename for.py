"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    school=[
    {'School class':'4A','scores':[5,5,4,5,3,2,5,4,3,5,5]},
    {'School class':'4B','scores':[5,4,4,5,3,3,5,4,4,4,4]},
    {'School class':'4C','scores':[5,4,4,5,4,2,4,2,5,4,4,4,4]},
    {'School class':'4C','scores':[3,2,2,3,2,2,3,2,3,2,2,3,2]}]
    return (school)   
if __name__ == "__main__":
    school = main()

for number_of_class in range(len(school)):
    score_summ=0
    for scores in school[number_of_class]['scores']:
        score_summ+=scores
    print (score_summ/len(school[number_of_class]['scores']))

for number_of_class in range(len(school)):
    score_summ=0
    for scores in school[number_of_class]['scores']:
        score_summ+=scores
    print (score_summ, len(school[number_of_class]['scores']))
print (sum(score_summ)/sum(len(school[number_of_class]['scores'])))


