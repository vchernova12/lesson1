"""

Домашнее задание №1

Исключения: приведение типов

* Напишите функцию get_summ(num_one, num_two), которая принимает 
  на вход два целых числа (int), складывает их и возвращает результат 
  сложения
* Оба аргумента нужно приводить к целому числу при помощи int() и 
  перехватывать исключение ValueError если приведение типов не сработало
    
"""

def get_summ(num_one, num_two):
    try:
        #num_one= input("Введите число: ")
        #num_two= input("Введите число: ")
        num_one=int(num_one)
        num_two=int(num_two)
        return (num_one+num_two)

    except ValueError:
        print ("Должны быть введены цисла")
if __name__ == "__main__":
    
    print(get_summ(2, 2))
    print(get_summ(3, "3"))
    print(get_summ("4", "4"))
    print(get_summ("five", 5))
    print(get_summ("six", "шесть"))
