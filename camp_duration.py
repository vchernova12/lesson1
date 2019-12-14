import calendar
from datetime import datetime
camp_begin= input('начало кампании')
camp_end=input('конец кампании')
#camp_begin = '12/23/2010'
camp_begin= datetime.strptime(camp_begin, '%m/%d/%Y')
camp_end= datetime.strptime(camp_end, '%m/%d/%Y')
if camp_begin.month  != camp_end.month:
    duration_month_1=int(calendar.monthrange(camp_begin.year,camp_begin.month)[1]) - camp_begin.day
    duration_month_2=camp_end.day
    duration_2_months=duration_month_1+duration_month_2
    print(duration_2_months)
else:
    duration = (camp_end.day-camp_begin.day)
    print(duration) 


#datetime.datetime(2010, 12, 23, 0, 0)
#print(camp_begin)