from datetime import date, time, datetime, timedelta

today = date.today()
d1 = timedelta(days=1000)
result = today + d1
print(result.isoformat())