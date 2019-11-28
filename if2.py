"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    entery= input("Введите значение:")
    return (entery)
def line_comparer (line_1, line_2):
    if type(line_1) == str or type(line_2) == str:
        if len(line_1)==len(line_2):
            return "1"
        elif len(line_1)!=len(line_2) and len(line_1)>len(line_2):
            return "2"
        elif len(line_1)!=len(line_2) and (line_2) == 'learn':
            return "3"
    else:
        return "0"
if __name__ == '__main__':
    line_1= main()
    line_2= main()
    comparison_result=line_comparer (line_1, line_2)
print(comparison_result)
