import calendar
from datetime import datetime


def camp_duration(camp_begin,camp_end):
    try:
        camp_begin= datetime.strptime(camp_begin, '%m/%d/%Y')
        camp_end= datetime.strptime(camp_end, '%m/%d/%Y')
        if (datetime.now().month==camp_begin.month and (camp_begin.day- datetime.now().day) <= 5) or camp_end.month < camp_begin.month or camp_end.year < camp_begin.year or camp_end.year-camp_begin.year>=2:
            raise ValueError ("Пожалуйста, проверьте правильность дат в кампании.")
        elif camp_end.month-camp_begin.month >= 1 and camp_end.year==camp_begin.year:
            second_to_last_month=camp_begin.month
            duration_in_between=0
            for months_in_camp in range((camp_end.month-camp_begin.month-1)):
                second_to_last_month +=1
                duration_in_between += calendar.monthrange(camp_end.year,second_to_last_month)[1]
            duration_first_month = calendar.monthrange(camp_begin.year,camp_begin.month)[1] - camp_begin.day +1 
            duration_last_month = camp_end.day
            duration = duration_first_month+duration_last_month+duration_in_between
            return(duration)
        elif camp_end.year>camp_begin.year:
            second_to_last_month=camp_begin.month
            duration_in_year_1=0
            for months_in_camp in range((12-camp_begin.month)):
                second_to_last_month +=1
                duration_in_year_1 += calendar.monthrange(camp_begin.year,second_to_last_month)[1]
            second_to_last_month=0
            duration_in_year_2=0
            for months_in_camp in range((camp_end.month-1)):
                second_to_last_month +=1
                duration_in_year_2 += calendar.monthrange(camp_end.year,second_to_last_month)[1]
            duration_first_month = calendar.monthrange(camp_begin.year,camp_begin.month)[1] - camp_begin.day +1 
            duration_last_month = camp_end.day
            duration = duration_first_month+duration_last_month+duration_in_year_1+duration_in_year_2
            return(duration)
        elif camp_end.month==camp_begin.month and camp_end.year==camp_begin.year:
            duration = (camp_end.day-camp_begin.day)+1
            return(duration) 
    except ValueError:
        print("Даты кампании не были введены или указаны в несоответствующем формате")

if __name__ == "__main__":
    print(camp_duration('11/12/2019','12/15/2019'))
    print(camp_duration('27/12/2019','03/12/2019'))
    print(camp_duration('02/12/2019','04/12/2019'))