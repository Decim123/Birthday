import datetime
from datetime import datetime
now = datetime.now()
my_birthday = datetime(now.year, 4, 20)
if now > my_birthday:
    my_birthday = datetime((now.year) + 1, 4, 20)
difference =  my_birthday - now
print(my_birthday - now)