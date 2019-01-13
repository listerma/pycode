from datetime import date


#获取当前日期，格式化为日报地址模式year-month/day
tdate = date.today()
print(tdate)
datetmp = str(tdate).split("-",1)
print(datetmp)