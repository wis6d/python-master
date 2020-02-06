from datetime import date, time, datetime, timedelta

today = date.today()
millennium = date(2001, 1, 1)
result = today - millennium
print(str(result.days) + '日間')