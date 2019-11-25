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
    {'School class':'4A','scores':[3,4,4,5,3,2,5,4,3,4,4]},
    {'School class':'4B','scores':[5,4,4,5,3,3,5,4,4,4,4]},
    {'School class':'4C','scores':[5,4,4,5,2,2,2,2,5,4,4,4,4]},
    {'School class':'4C','scores':[3,4,4,3,2,2,3,2,3,4,4,3,4]}]
    
if __name__ == "__main__":
    school = main()
score_summ=0
for school_class in school[0]['scores']:
    score_summ+=scores
    print(score_summ)
#print (score_summ/len(school['scores'])