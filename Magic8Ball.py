#Magic8Ball.py
#Name: Meg Aerni
#Date: 9/1/2025
#Assignment: Lab 2

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.

  #Prompt the user for their question.
  answers = ["Yes", "Yes, indeed", "For certain", "It is hard to say", "No one knows", "Only time will tell", "No", "Definitely not",
           "Not in a million years", "Ask again later", "Difficult to predict", "Shouldn't make any assumptions", 
           "Very doubtful", "Ask again, please", "Shhhh! It's a secret", "You should know that already"]

  print("Magic 8 Ball")
  input("Ask a 'yes or no' question: ")
  #Answer question randomly with one of the options from your earlier list.

  length = len(answers)
  r = random.random() * length
  r = int(r)
  response = answers[r]
  print(response)



if __name__ == '__main__':
  main()