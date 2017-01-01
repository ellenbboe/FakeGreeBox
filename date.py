import datetime
begin = datetime.date(2014,1,20)
end = datetime.date(2014,4,1)
d = begin
delta = datetime.timedelta(days=1)
while d <= end:
    print d.strftime("%Y-%m-%d")
    d += delta
