#FutureTime.py
#Name:
#Date:
#Assignment:

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour-6) % 24
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  hours= input("Enter hours: ")
  hours= int(hours) # change from text to number
  futureHour= currentHour + hours
  print(futureHour)
  #Ask user for minutes
  mintues= input("Enter mintues: ")
  mintues= int(mintues) # change from text to number
  futuremintues= currentMinute + mintues

  strHour= str(futureHour)
  strmintue= str(futuremintues)
  if futuremintues < 10:
    strmintue= "0" + strmintue #add a leading zero to one digit mintue

    
  #Calculate the time after the user-supplied time has passed.

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()
