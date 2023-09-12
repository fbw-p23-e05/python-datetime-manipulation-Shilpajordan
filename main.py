# Task 1
from datetime import datetime as dt, timedelta
"""current_datetime =datetime.now()

new_date = datetime.now() - timedelta(days=15)
print(new_date.strftime("%Y-%m-%d")) """

# Task 2
""" current_datetime =datetime.now()

new_date = datetime.now() + timedelta(days=7)
print(new_date.strftime("%Y-%m-%d")) """

# Task 3

current_date =dt(2020, 1, 1)
# new_date = datetime.now()+  timedelta(days=25)
# print(new_date.strftime("%Y-%m-%d"))
due_date =current_date + timedelta(days=25)

print("Hello Friedrich, your rent of 300 € is due on ",due_date.strftime("%d %B, %Y"))