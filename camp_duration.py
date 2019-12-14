import calendar
from datetime import datetime


def camp_duration():
    camp_begin= input('начало кампании')
    camp_end=input('конец кампании')
    camp_begin= datetime.strptime(camp_begin, '%m/%d/%Y')
    camp_end= datetime.strptime(camp_end, '%m/%d/%Y')
    if camp_end.month - camp_begin.month == 1:
        duration_first_month = int(calendar.monthrange(camp_begin.year,camp_begin.month)[1]) - camp_begin.day + 1
        duration_last_month = camp_end.day
        duration_2_months=duration_first_month + duration_last_month
        print(duration_2_months)
    elif camp_end.month-camp_begin.month > 1:
        second_to_last_month=camp_begin.month
        print(second_to_last_month)
        duration_in_between=0
        for months_in_camp  in range((camp_end.month-camp_begin.month-1)):
            second_to_last_month +=1
            duration_in_between += calendar.monthrange(camp_end.year,second_to_last_month)[1]
            print(duration_in_between, second_to_last_month,camp_end.month)
        duration_first_month = calendar.monthrange(camp_begin.year,camp_begin.month)[1] - camp_begin.day +1 
        duration_last_month = camp_end.day
        duration = duration_first_month+duration_last_month+duration_in_between
        print(duration,duration_in_between)
    elif camp_end.month==camp_begin.month:
        duration = (camp_end.day-camp_begin.day)+1
        print(duration) 
    elif camp_end.month < camp_begin.month:
        raise ValueError ("Пожалуйста, проверьте правильность дат в кампании. Окончание кампании запланировано раньше начала")


if __name__ == "__main__":
    camp_duration()


