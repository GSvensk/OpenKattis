import datetime

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
tmp = input().split()

weekday = datetime.date(2009, int(tmp[1]), int(tmp[0])).weekday()
print(weekdays[weekday])

