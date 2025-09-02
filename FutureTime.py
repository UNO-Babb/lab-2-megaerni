#FutureTime.py
#Name: Meg Aerni
#Date: 9/1/2024
#Assignment: Lab 2

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 5) % 24
  currentMinute = now.minute
  
  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  morehours = input("How many hours: ")
  morehours = int(morehours)
  print(type(morehours))
  #Ask user for minutes
  moreminutes = input("How many minutes: ")
  moreminutes = int(moreminutes)

  #Calculate the time after the user-supplied time has passed.
  finalminute = (now.minute + moreminutes) % 60
  hourspill = (finalminute)//60
  finalhour = (now.hour + morehours + hourspill)

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
  print(finalhour + ":" + finalminute)


if __name__ == '__main__':
  main()
