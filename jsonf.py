import json
data = {"name":"Tirtha","age":34}
jeson_string = json.dumps(data)
print(type(jeson_string))

from datetime import date,timedelta,datetime

date1 = date(2025,8,20)
print(date1.month)



data = datetime.now()

print(data)