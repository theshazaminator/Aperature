from datetime import datetime
from datetime import date

big_list = {"products": ["milk", "eggs"], "experation month": 2 "experation day": 3}

day = []


day.append(big_list["experation day"])

for items in day:
    print()


datemonth = date(2022, big_list["experation month"],big_list["experation day"] )

print(datemonth)



current_time = date.today()
print(current_time)

if datemonth == current_time:
    print("Expired")
else:
    print("Not Expired")



