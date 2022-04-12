print('''
 ____                    _                 __  __             _   _     
|  _ \  __ _ _   _ ___  (_)_ __     __ _  |  \/  | ___  _ __ | |_| |__  
| | | |/ _` | | | / __| | | '_ \   / _` | | |\/| |/ _ \| '_ \| __| '_ \ 
| |_| | (_| | |_| \__ \ | | | | | | (_| | | |  | | (_) | | | | |_| | | |
|____/ \__,_|\__, |___/ |_|_| |_|  \__,_| |_|  |_|\___/|_| |_|\__|_| |_|
             |___/  
''')
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
def days_in_month(year,month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year):
        if month == 2:
            return 29
        else:
            return month_days[month-1]
    else:
        return month_days[month-1]
value = True
while value:
  year = int(input("Enter a year: "))
  month = int(input("Enter a month: "))
  days = days_in_month(year, month)
  print("\n",days,"Days")
  choice = input("\nDo you want to continue? ")
  choice  = choice.capitalize()
  if choice == "Yes":
    pass
  else:
    value = False
print("\nThank You for using!\n")