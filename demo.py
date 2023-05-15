from datetime import datetime,timedelta
#timedelta is the interval between two dates

d1 = input("Enter date of issue(dd/mm/yyyy)")
#d2 = input("Enter date of submit(dd/mm/yyyy)")
d1 = d1.split("/")
d1 = datetime(int(d1[2]),int(d1[1]),int(d1[0]))
print(d1)
d2 = datetime(2022,5,20)
result = d2-d1
print(result.days)

