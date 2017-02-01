import datetime
import os

from random import randint

def write_log(date):
  f = open('log.txt', 'a+')
  f.writelines(date.isoformat() + '\n')
  f.close()

def commit_github(date):
  os.system('git add .')
  os.system('git commit --date={date} -m "Update {date}."'.format(date=date.isoformat()))

def transformation(date) -> datetime.date:
  return datetime.timedelta(hours=randint(0, 24), minutes=randint(0, 60), seconds=randint(0, 60))

def commit(a):
	commit_count = randint(1,5)
	while commit_count > 0:
		date = datetime.datetime.strptime(a, '%Y%m%d')
		date += transformation(date)
		write_log(date)
		commit_github(date)
		commit_count -= 1

if __name__ == "__main__":
	begin = datetime.date(2017,2,1)
	end = datetime.date(2020,6,24)
	d = begin
	delta = datetime.timedelta(days=1)
	while d <= end:
		date = d.strftime("%Y%m%d")
		date = str(date)
		commit(date)
		d += delta

