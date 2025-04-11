#We need to use the datetime library
from datetime import datetime

current_date = datetime.now()
print('Today is ' + str(current_date))

#timedelta is used to define a period of time
from datetime import datetime, timedelta
today = datetime.now()
print('Today is: ' + str(today))
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))

#There is another way to use this library
from datetime import datetime
current_date = datetime.now()
print(str(current_date.year) + '.' + str(current_date.month) + '.' + str(current_date.day))

#When receiving the date as a string and need to convert it to a datetime object
from datetime import datetime
birthday = input('When is your birthday (dd/mm/yyyy)?')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')#用來將字串轉換為 datetime 物件的方法，通常用在你從外部讀入一個時間格式的字串時，想要對它進行時間的運算、比較等操作。
#'%y'指的是兩位數的年份，因此西元年應改為'%Y'四位數較合適
print('Birthday: ' + str(birthday_date))
print('Happy Birthday!')
print("這是第二次 commit 的修改")