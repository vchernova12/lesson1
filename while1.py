"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
    question=input("Как дела?")
    return(question) 
if __name__ == "__main__":
    answer=ask_user()
while True:
    if answer =="Хорошо":
        break
    else:
       ask_user()
       

