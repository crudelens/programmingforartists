'''
4. Given a year, write a function that outputs if it is a leap year.
   Condition for leap year:
   on every year that is evenly divisible by 4
   except every year that is evenly divisible by 100
   unless the year is also evenly divisible by 400
'''
def leapYear(yearin):
   if yearin%100==0:
      if yearin%400==0:
         return True
      else:
         return False
   elif yearin%4==0:
      return True
   else:
      return False

yearin=int(input("Enter a Year: "))
ans=leapYear(yearin)
if ans==True:
   print(f"The Year {yearin} is a Leap Year.")
else:
   print(f"The Year {yearin} is not a Leap Year.")