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

def commit(date):
	while True:
		commit_count = randint(1,5)
		while commit_count > 0:
			date = datetime.datetime.strptime(str(date), '%Y%m%d')
			date += transformation(date)
			write_log(date)
			commit_github(date)
			commit_count -= 1

if __name__ == "__main__":
        begin = datetime.date(2017,1,1)
        end = datetime.date(2017,2,1)
        d = begin
        delta = datetime.timedelta(days=1)
        while d <= end:
                date = d.strftime("%Y%m%d")
                commit(date)
                d += delta

