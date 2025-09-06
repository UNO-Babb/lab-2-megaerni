#FutureTime.py
#Name: Meg Aerni
#Date: 9/1/2024
#Assignment: Lab 2

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 5) % 12
  currentMinute = now.minute
  
  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  morehours = input("How many hours: ")
  morehours = int(morehours)

  #Ask user for minutes
  moreminutes = input("How many minutes: ")
  moreminutes = int(moreminutes)

  #Calculate the time after the user-supplied time has passed.
  finalminute = (currentMinute + moreminutes) % 60
  hourspill = (currentMinute + moreminutes) // 60
  finalhour = ((currentHour + morehours + hourspill - 1) % 12) + 1

  #Do not use any if statements in calculating the time.
  finalminute1 = (finalminute) // 10
  finalminute2 = (finalminute) % 10
  finalhour1 = (finalhour) // 10
  finalhour2 = (finalhour) % 10
  #Output the future time in standard format "HH:MM"
  finalminute1 = str(finalminute1)
  finalminute2 = str(finalminute2)
  finalhour1 = str(finalhour1)
  finalhour2 = str(finalhour2)
  print(finalhour1 + finalhour2 + ":" + finalminute1 + finalminute2)

if __name__ == '__main__':
  main()
