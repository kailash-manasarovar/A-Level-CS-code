'''
Created on 10 Jun 2018

@author: katharinemurphy
'''
import random
correctAnswer = ''
#generate number
for i in range (4):
    tempChar = str(random.randint(0,9))
    correctAnswer = correctAnswer + tempChar
guess = ''
attempts = 0
while guess != 'q':
    guess = input('Please enter your 4 digit number or q to quit :')
    #Make sure it is 4 digits long and contains only digits
    if guess.isnumeric() and len(guess) == 4:
        numCorrect = 0
        #How many numbers did they guess correctly?
        for i in range(0,3):
            if guess[i] == correctAnswer[i]:
                numCorrect += 1
        
        #Have they guessed it?
        if(guess == correctAnswer):
            print('Well done... That took you '+ str(attempts) +' attempts!')
        else:
            print('That is not right. You guessed '+ str (numCorrect) +' numbers correctly this time')
attempts += 1
print(correctAnswer)