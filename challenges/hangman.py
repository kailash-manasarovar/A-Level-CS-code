# # importing the time module
# import time
# 
# # welcoming the user
# name = input("What is your name? ")
# 
# print("Hello, " + name, "Time to play hangman!")
# 
# print("")
# 
# # wait for 1 second
# time.sleep(1)
# 
# print("Start guessing...")
# time.sleep(0.5)
# 
# # here we set the secret
# word = "secret"
# 
# # creates an variable with an empty value
# guesses = ''
# 
# # determine the number of turns
# turns = 10
# 
# # Create a while loop
# # check if the turns are more than zero
# while turns > 0:         
# 
#     # make a counter that starts with zero
#     failed = 0             
# 
#     # for every character in secret_word    
#     for char in word:      
# 
#     # see if the character is in the players guess
#         if char in guesses:    
#     
#         # print then out the character
#             print(char)
# 
#         else:
#     
#         # if not found, print a dash
#             print("_")
#        
#         # and increase the failed counter with one
#             failed += 1    
# 
#     # if failed is equal to zero
# 
#     # print You Won
#     if failed == 0:        
#         print("You won!")
# 
#     # exit the script
#         break              
# 
#     #print
# 
#     # ask the user go guess a character
#     guess = input("guess a character:") 
# 
#     # set the players guess to guesses
#     guesses += guess                    
# 
#     # if the guess is not found in the secret word
#     if guess not in word:  
#  
#     # turns counter decreases with 1 (now 9)
#         turns -= 1        
#  
#     # print wrong
#         print("Wrong")
#  
#     # how many turns are left
#         print("You have", +turns, "more guesses")
#  
#     # if the turns are equal to zero
#         if turns == 0:           
#     
#         # print "You Loose"
#             print("You Loose")
 
 
# Ray's Hangman from Oxford
import tkinter as tk
import random
import fileinput
from tkinter import *
 
 
 
# ------------------Functions for Single Player Mode-------------------------
def random_word(category):
    file = [line for line in fileinput.input(category)]
    rand = random.Random()
    return file[int(rand.random() * len(file))],
 
 
def turn_word_to_list(category):
    global word_list
    word_list = list(random_word(category))
    global word
    global game_word
    word = str(word_list[0])
    game_word = list(word)
    for letter in game_word:
        letter.lower()
 
    global letter_count
    game_word.pop()
 
    letter_count = len(game_word)
    # print("This word has {0} letters.".format(letter_count))
    global x_coordinate
    x_coordinate = 100
    num = 0
    while num < letter_count:
        x_coordinate += 30
        num += 1
        hangman_welcome_canvas.create_text(x_coordinate, 500, text="_", font=("Proxima Nova Rg", 30))
 
 
def draw_background():
    hangman_welcome_canvas.create_line(200, 400, 600, 400, fill="black", width=7)
    hangman_welcome_canvas.create_line(202, 150, 202, 400, fill="black", width=7)
    hangman_welcome_canvas.create_line(200, 150, 400, 150, fill="black", width=7)
    hangman_welcome_canvas.create_line(396, 150, 396, 200, fill="black", width=7)
 
 
#      canvas.pack()
 
 
def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x - r, y - r, x + r, y + r, **kwargs)
 
 
tk.Canvas.create_circle = _create_circle
 
 
def _create_circle_arc(self, x, y, r, **kwargs):
    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs["end"] - kwargs["start"]
        del kwargs["end"]
    return self.create_arc(x - r, y - r, x + r, y + r, **kwargs)
 
 
tk.Canvas.create_circle_arc = _create_circle_arc
 
 
# ------------------------End of Functions for Single Player Mode-----------------------
 
# WrongLetterText = hangman_welcome_canvas.create_text(200, 450, text = "You've entered this letter already and it is wrong.", font = ("Proxima Nova Rg", 15))
# CorrectLetterText = hangman_welcome_canvas.create_text(200, 450, text = "You've entered this letter already and it is correct", font = ("Proxima Nova Rg", 15))
 
 
def multi_gameword_entry():
    hints_given_num = 1
    global gameWord
    global gameWordList
    global gameWordEntry
    hangman_welcome_canvas.create_text(250, 550, text="Enter a word here:", font=("Proxima Nova Rg", 15))
    gameWordEntry = Entry(hangman)
    gameWordEntry.focus()
    gameWordEntry.pack()
 
    gameWordEntryWindow = hangman_welcome_canvas.create_window(330, 542, anchor=NW, window=gameWordEntry)
    submitButton = Button(hangman, text="OK", font=("Proxima Nova Rg", 15), height=1, width=5, command=submitWordInput)
    submitButtonWindow = hangman_welcome_canvas.create_window(460, 530, anchor=NW, window=submitButton)
 
def play_multi():  # multi-player mode canvas, functions
    global hints_given_num
    hints_given_num = 1
    hangman_welcome_canvas.delete("all")  # clear canvas
    hangman_welcome_canvas.create_text(400, 80, text="Play with Friends!", font=("Proxima Nova Rg", 50))
    #    hangman_welcome_canvas.create_text(400,500,text= "Play with your friends!", font = ("Proxima Nova Rg", 30))
 
    global correctGuessesList_multi
    global wrongGuessesList_multi
    global total_guesses_multi
    global wrongGuessesNum_multi
 
    correctGuessesList_multi = []  # original values for correct guesses, total guesses
    wrongGuessesList_multi = []
    total_guesses_multi = 6
    wrongGuessesNum_multi = 0
 
    backButtonFunc()
    multi_gameword_entry()
 
 
def invalidInputDisplay():
    hangman_welcome_canvas.create_text(200, 450, text="Invalid Input! Try again", font=("Proxima Nova Rg", 15),
                                       tag="InvalidInputText")
 
 
def WrongLetterRepeated():
    hangman_welcome_canvas.delete("InvalidInputText", "WrongLetterText", "CorrectLetterText")
    hangman_welcome_canvas.create_text(200, 450, text="You've entered this letter already and it's incorrect.",
                                       font=("Proxima Nova Rg", 15), tag="InvalidInputText")
 
 
def CorrectLetterRepeated():
    hangman_welcome_canvas.delete("InvalidInputText", "WrongLetterText", "CorrectLetterText")
    hangman_welcome_canvas.create_text(200, 450, text="You've entered this letter already and it's correct.",
                                       font=("Proxima Nova Rg", 15), tag="InvalidInputText")
 
hints_given_num = 1
def hint():
    global hints_given_num
 
    if hints_given_num > 3:
        hangman_welcome_canvas.create_text(400, 125, text = "You have 0 hints left", font = ("Proxima Nova Rg", 15))
        hangman_welcome_canvas.delete("hintButton")
    else:
 
        random_num = random.randint(0, letter_count)
        #print(letter_count)
        #print(random_num)
        index_random_num = random_num - 1
        random_hint = gameWordList[index_random_num]
        hinted_list = []
 
        while random_hint not in hinted_list and random_hint not in correctGuessesList_multi:
            hints_given_num += 1
            hinted_list.append(random_hint)
            correctGuessesList_multi.append(random_hint)
            if len(correctGuessesList_multi) == len(gameWordList):
                hangman_welcome_canvas.delete("all")
                hangman_welcome_canvas.create_text(400, 300, text="YOU WIN!", font=("Proxima Nova Rg", 72),
                                                   justify="center")
                hangman_welcome_canvas.create_text(400, 500, text="The word was: {0}".format(gameWord.upper()),
                                                   font=("Proxima Nova Rg", 30), justify="center")
                backButtonFunc()
 
            elif random_hint.lower() in gameWordList:
                indices = []
                offset = 0
                # print(correctGuessesList_multi)
                # print(gameWordList)
                for theLetter in range(gameWordList.count(random_hint)):
                    indices.append(gameWordList.index(random_hint, offset))
                    offset = indices[-1] + 1
                #  index = game_word.index(userInput) +1
                if len(indices) > 1:
 
                    for num in indices:
                        index = num + 1
                        new_count1 = letter_count - index
                        correctGuessesList_multi.append(random_hint.lower())
                        new_x_coordinate = x_coordinate
                        new_x_coordinate = x_coordinate - 30 * new_count1
                        hangman_welcome_canvas.create_text(new_x_coordinate, 495, text=random_hint,
                                                           font=("Proxima Nova Rg", 15))
 
                elif len(indices) == 1:
                    correctGuessesList_multi.append(random_hint.lower())
                    index = indices[0] + 1
                    # print(indices)
                    num2 = 0
                    new_count = letter_count - index
                    # print(new_count)
                    new_x_coordinate = x_coordinate
                    new_x_coordinate = x_coordinate - 30 * new_count
                    # print(new_x_coordinate)
 
                    hangman_welcome_canvas.create_text(new_x_coordinate, 495, text=random_hint,
                                                       font=("Proxima Nova Rg", 15))
        #print(random_hint)
 
        #print(hints_given_num)
#make hints maximum 3 hints, fill in letter after hitting button 'hint', check if letter is already hinted
 
def submitWordInput():
    hints_given_num = 1
    global gameWord
    global gameWordList
    gameWord = gameWordEntry.get()
    #print(gameWord)
    gameWordEntry.delete(0, END)
    gameWordEntry.insert(0, "")
    gameWordList = list(gameWord)
    hangman_welcome_canvas.delete("all")
    hangman_welcome_canvas.create_text(400, 80, text="Multi-Player Mode", font=("Proxima Nova Rg", 50))
    #    hangman_welcome_canvas.create_text(400,440,text= "Play with your friends!", font = ("Proxima Nova Rg", 30))
    # print(gameWordList)
    backButtonFunc()
    draw_background()
    hangman_welcome_canvas.create_text(250, 550, text="Enter a letter here:", font=("Proxima Nova Rg", 15))
 
 
 
    global letter_count
    letter_count = len(gameWordList)
    # print("This word has {0} letters.".format(letter_count))
    global x_coordinate
    x_coordinate = 100
    num = 0
    while num < letter_count:
        x_coordinate += 30
        num += 1
        hangman_welcome_canvas.create_text(x_coordinate, 500, text="_", font=("Proxima Nova Rg", 30))
 
 
    hintButton = Button(hangman, text="Hints", font=("Proxima Nova Rg", 15), height=1, width=3,
                                command = hint)
    hintButton.configure(width=20, activebackground="white", relief=FLAT)
    hintButton_window = hangman_welcome_canvas.create_window(280, 430, anchor=NW, window=hintButton)
 
    #hint_multiplayer()
    # ===========================================================================================
    def submitLetterInput():
        userLetterChoice = userLetterEntry.get()
        # print(userLetterChoice)
        userLetterEntry.delete(0, END)
        userLetterEntry.insert(0, "")
        userLetterChoiceList = list(userLetterChoice)
 
        # print("something")
        acceptable_answers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                              'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
 
        if userLetterChoice.upper() == gameWord.upper():
            hangman_welcome_canvas.delete("all")
            hangman_welcome_canvas.create_text(400, 300, text="YOU WIN!", font=("Proxima Nova Rg", 72),
                                               justify="center")
            hangman_welcome_canvas.create_text(400, 500, text="The word was: {0}".format(gameWord.upper()),
                                               font=("Proxima Nova Rg", 30), justify="center")
 
 
            backButtonFunc()
 
        elif userLetterChoice.upper() not in acceptable_answers:
            invalidInputDisplay()
 
 
        elif len(userLetterChoiceList) != 1:
            invalid = hangman_welcome_canvas.create_text(200, 450, text="Invalid Input! Try again",
                                                         font=("Proxima Nova Rg", 15))
 
        elif userLetterChoice.upper() in wrongGuessesList_multi:
            # invalid.pack_forget()
            hangman_welcome_canvas.create_text(200, 450, text="You've entered this letter already and it is wrong.",
                                               font=("Proxima Nova Rg", 15))
        elif userLetterChoice.lower() in correctGuessesList_multi:
            hangman_welcome_canvas.create_text(200, 450, text="You've entered this letter already and it is correct",
                                               font=("Proxima Nova Rg", 15))
        else:
            if userLetterChoice.lower() in gameWordList:
                indices = []
                offset = 0
                # print(correctGuessesList_multi)
                # print(gameWordList)
                for theLetter in range(gameWordList.count(userLetterChoice)):
                    indices.append(gameWordList.index(userLetterChoice, offset))
                    offset = indices[-1] + 1
                #  index = game_word.index(userInput) +1
                if len(indices) > 1:
 
                    for num in indices:
                        index = num + 1
                        new_count1 = letter_count - index
                        correctGuessesList_multi.append(userLetterChoice.lower())
                        new_x_coordinate = x_coordinate
                        new_x_coordinate = x_coordinate - 30 * new_count1
                        hangman_welcome_canvas.create_text(new_x_coordinate, 495, text=userLetterChoice,
                                                           font=("Proxima Nova Rg", 15))
 
                elif len(indices) == 1:
                    correctGuessesList_multi.append(userLetterChoice.lower())
                    index = indices[0] + 1
                    # print(indices)
                    num2 = 0
                    new_count = letter_count - index
                    # print(new_count)
                    new_x_coordinate = x_coordinate
                    new_x_coordinate = x_coordinate - 30 * new_count
                    # print(new_x_coordinate)
 
                    hangman_welcome_canvas.create_text(new_x_coordinate, 495, text=userLetterChoice,
                                                       font=("Proxima Nova Rg", 15))
 
                if len(correctGuessesList_multi) == len(gameWordList):
                    hangman_welcome_canvas.delete("all")
                    hangman_welcome_canvas.create_text(400, 300, text="YOU WIN!", font=("Proxima Nova Rg", 72),
                                                       justify="center")
                    backButtonFunc()
 
            else:
                # wrongGuessesNum += 1
                wrongGuessesList_multi.append(userLetterChoice.upper())
 
                if len(wrongGuessesList_multi) == 1:
 
                    hangman_welcome_canvas.create_circle(398, 200, 30, fill="black")
                    hangman_welcome_canvas.update()
 
                elif len(wrongGuessesList_multi) == 2:
 
                    hangman_welcome_canvas.create_line(398, 230, 398, 330, fill="black", width=5)
                    hangman_welcome_canvas.update()
 
                elif len(wrongGuessesList_multi) == 3:
 
                    hangman_welcome_canvas.create_line(398, 250, 360, 290, fill="black", width=5)
                    hangman_welcome_canvas.update()
 
                elif len(wrongGuessesList_multi) == 4:
 
                    hangman_welcome_canvas.create_line(398, 250, 436, 290, fill="black", width=5)
                    hangman_welcome_canvas.update()
 
                elif len(wrongGuessesList_multi) == 5:
 
                    hangman_welcome_canvas.create_line(398, 330, 360, 370, fill="black", width=5)
                    hangman_welcome_canvas.update()
 
                elif len(wrongGuessesList_multi) == 6:
 
                    hangman_welcome_canvas.create_line(398, 330, 436, 370, fill="black", width=5)
                    hangman_welcome_canvas.delete("all")
                    hangman_welcome_canvas.create_text(400, 300, text="GAME OVER!", font=("Proxima Nova Rg", 72),
                                                       justify="center")
                    hangman_welcome_canvas.create_text(400, 500, text="The word was: {0}".format(gameWord),
                                                       font=("Proxima Nova Rg", 30), justify="center")
                    retryMultiPlayer()
                    backButtonFunc()
                    hangman_welcome_canvas.update()
 
    # ===========================================================================================
 
    global userLetterEntry
    userLetterEntry = Entry(hangman)
    userLetterEntry.focus()
    userLetterEntry.pack()
    userLetterEntryWindow = hangman_welcome_canvas.create_window(330, 542, anchor=NW, window=userLetterEntry)
    submitButton = Button(hangman, text="OK", font=("Proxima Nova Rg", 15), height=1, width=5,
                          command=submitLetterInput)
    submitButtonWindow = hangman_welcome_canvas.create_window(460, 530, anchor=NW, window=submitButton)
    global userLetterChoice
    global userLetterChoiceList
 
 
def retryMultiPlayer():
    retryMultiPlayerButton = Button(hangman, text="Play Again", font=("Proxima Nova Rg", 15), height=1, width=10,
                                    command=play_multi)
    retryMultiPlayerButtonWindow = hangman_welcome_canvas.create_window(100, 550, anchor=NW,
                                                                        window=retryMultiPlayerButton)
 
 
def play_single():
    hangman_welcome_canvas.delete("all")
    hangman_welcome_canvas.create_text(400, 80, text="Single Player Mode", font=("Proxima Nova Rg", 50))
    hangman_welcome_canvas.create_text(400, 150, text="Choose A Category from Below!", font=("Proxima Nova Rg", 30))
 
    commonWords = Button(hangman, text="Common Words", font=("Proxima Nova Rg", 15), height=1, width=10,
                         command=lambda: gamePlay("common_word.txt", "Common Words"))
    commonWords.configure(width=15, activebackground="white", relief=FLAT)
    commonWords_window = hangman_welcome_canvas.create_window(400, 300, anchor=NW, window=commonWords)
    backButtonFunc()
 
    phobias = Button(hangman, text="Phobias", font=("Proxima Nova Rg", 15), height=1, width=10,
                     command=lambda: gamePlay("Phobias.txt", "All Kinds of Phobias"))
    phobias.configure(width=15, activebackground="white", relief=FLAT)
    phobias_window = hangman_welcome_canvas.create_window(200, 300, anchor=NW, window=phobias)
 
    elements = Button(hangman, text="Elements", font=("Proxima Nova Rg", 15), height=1, width=10,
                      command=lambda: gamePlay("elements.txt", "Elements"))
    elements.configure(width=15, activebackground="white", relief=FLAT)
    elements_window = hangman_welcome_canvas.create_window(200, 350, anchor=NW, window=elements)
 
    science = Button(hangman, text="Scientific Words", font=("Proxima Nova Rg", 15), height=1, width=10,
                     command=lambda: gamePlay("science_word.txt", "Scientific Words"))
    science.configure(width=15, activebackground="white", relief=FLAT)
    science_window = hangman_welcome_canvas.create_window(400, 350, anchor=NW, window=science)
 
    secretLevel = Button(hangman, text="Credits", font=("Proxima Nova Rg", 15), height=1, width=4,
                         command=lambda: gamePlay("secretlevel.txt", "SWEAR WORDS!"))
    secretLevel.configure(width=5, activebackground="white", relief=FLAT)
    secretLevel_window = hangman_welcome_canvas.create_window(40, 550, anchor=NW, window=secretLevel)
 
 
def retryButton():
    retryButton = Button(hangman, text="Retry", font=("Proxima Nova Rg", 15), height=1, width=5,
                         command=lambda: play_single())
    retryButtonWindow = hangman_welcome_canvas.create_window(40, 550, anchor=NW, window=retryButton)
 
 
def gamePlay(category, title):
 
    hangman_welcome_canvas.delete("all")
    hangman_welcome_canvas.create_text(400, 80, text=title, font=("Proxima Nova Rg", 50))
    backButtonChooseCategoryFunc()
    draw_background()
 
    global correctGuessesList
    correctGuessesList = []
    global wrongGuessesList
 
    global total_guesses
    global wrongGuessesNum
    wrongGuessesList = []
 
    total_guesses = 6
 
    wrongGuessesNum = 0
 
    # random_word("common_word.txt")
    turn_word_to_list(category)
    retryButton()
 
    def submitInput():
        global acceptable_answers
 
        acceptable_answers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                              'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
 
        global userInput
        userInput = userEntry.get()
        # print(userInput)
        userEntry.delete(0, END)
        userEntry.insert(0, "")
        userInputList = list(userInput)
 
        if userInput.upper() not in acceptable_answers:
            hangman_welcome_canvas.create_text(200, 450, text="Invalid Input! Try again", font=("Proxima Nova Rg", 15))
 
 
        elif len(userInputList) != 1:
            invalid = hangman_welcome_canvas.create_text(200, 450, text="Invalid Input! Try again",
                                                         font=("Proxima Nova Rg", 15))
 
        elif userInput.upper() in wrongGuessesList:
            # invalid.pack_forget()
            hangman_welcome_canvas.create_text(200, 450, text="You've entered this letter already and it is wrong.",
                                               font=("Proxima Nova Rg", 15))
        elif userInput.lower() in correctGuessesList:
            hangman_welcome_canvas.create_text(200, 450, text="You've entered this letter already and it is correct",
                                               font=("Proxima Nova Rg", 15))
        else:
            if userInput.lower() in game_word:
                indices = []
                offset = 0
                # print(correctGuessesList)
                # print(game_word)
                for theLetter in range(game_word.count(userInput)):
                    indices.append(game_word.index(userInput, offset))
                    offset = indices[-1] + 1
                #  index = game_word.index(userInput) +1
                if len(indices) > 1:
 
                    for num in indices:
                        index = num + 1
                        new_count1 = letter_count - index
                        correctGuessesList.append(userInput.lower())
                        new_x_coordinate = x_coordinate
                        new_x_coordinate = x_coordinate - 30 * new_count1
                        hangman_welcome_canvas.create_text(new_x_coordinate, 495, text=userInput,
                                                           font=("Proxima Nova Rg", 15))
 
                elif len(indices) == 1:
                    correctGuessesList.append(userInput.lower())
                    index = indices[0] + 1
                    # print(indices)
                    num2 = 0
                    new_count = letter_count - index
                    # print(new_count)
                    new_x_coordinate = x_coordinate
                    new_x_coordinate = x_coordinate - 30 * new_count
                    # print(new_x_coordinate)
 
                    hangman_welcome_canvas.create_text(new_x_coordinate, 495, text=userInput,
                                                       font=("Proxima Nova Rg", 15))
 
                if len(correctGuessesList) == len(game_word):
                    hangman_welcome_canvas.delete("all")
                    hangman_welcome_canvas.create_text(400, 300, text="YOU WIN!", font=("Proxima Nova Rg", 72),
                                                       justify="center")
                    backButtonFunc()
 
            else:
                # wrongGuessesNum += 1
                wrongGuessesList.append(userInput.upper())
 
                if len(wrongGuessesList) == 1:
 
                    hangman_welcome_canvas.create_circle(398, 200, 30, fill="black")
                    hangman_welcome_canvas.update()
 
                elif len(wrongGuessesList) == 2:
 
                    hangman_welcome_canvas.create_line(398, 230, 398, 330, fill="black", width=5)
                    hangman_welcome_canvas.update()
 
                elif len(wrongGuessesList) == 3:
 
                    hangman_welcome_canvas.create_line(398, 250, 360, 290, fill="black", width=5)
                    hangman_welcome_canvas.update()
 
                elif len(wrongGuessesList) == 4:
 
                    hangman_welcome_canvas.create_line(398, 250, 436, 290, fill="black", width=5)
                    hangman_welcome_canvas.update()
 
                elif len(wrongGuessesList) == 5:
 
                    hangman_welcome_canvas.create_line(398, 330, 360, 370, fill="black", width=5)
                    hangman_welcome_canvas.update()
 
                elif len(wrongGuessesList) == 6:
 
                    hangman_welcome_canvas.create_line(398, 330, 436, 370, fill="black", width=5)
                    hangman_welcome_canvas.delete("all")
                    hangman_welcome_canvas.create_text(400, 300, text="GAME OVER!", font=("Proxima Nova Rg", 72),
                                                       justify="center")
                    hangman_welcome_canvas.create_text(400, 500, text="The word was: {0}".format(word),
                                                       font=("Proxima Nova Rg", 30), justify="center")
                    retryButton()
                    backButtonFunc()
                    hangman_welcome_canvas.update()
 
    hangman_welcome_canvas.create_text(250, 550, text="Enter a letter here:", font=("Proxima Nova Rg", 15))
    userEntry = Entry(hangman)
    userEntry.focus()
    userEntry.pack()
    userEntryWindow = hangman_welcome_canvas.create_window(330, 542, anchor=NW, window=userEntry)
    submitButton = Button(hangman, text="OK", font=("Proxima Nova Rg", 15), height=1, width=5, command=submitInput)
    submitButtonWindow = hangman_welcome_canvas.create_window(460, 530, anchor=NW, window=submitButton)
    # print(game_word)
 
 
def showCredits():
    hangman_welcome_canvas.delete("all")
    hangman_welcome_canvas.create_text(400, 70, text="HANGMAN", font=("ProximaNova-Bold", 85), justify="center")
    hangman_welcome_canvas.create_text(400, 150, text="Executive Producer", font=("ProximaNova-Bold", 20),
                                       justify="center")
    hangman_welcome_canvas.create_text(400, 180, text="Emily Song", font=("Proxima Nova Rg", 20), justify="center")
    hangman_welcome_canvas.create_text(400, 210, text="Graphics & GUI", font=("Proxima Nova Rg bold", 20),
                                       justify="center")
    hangman_welcome_canvas.create_text(400, 250, text="Elisa\nRay Xu", font=("Proxima Nova Rg", 20), justify="center")
    hangman_welcome_canvas.create_text(400, 300, text="Word Libraries", font=("ProximaNova-Bold", 20), justify="center")
    hangman_welcome_canvas.create_text(400, 330, text="Tyler", font=("Proxima Nova Rg", 20), justify="center")
    hangman_welcome_canvas.create_text(400, 370, text="Coding", font=("ProximaNova-Bold", 20), justify="center")
    hangman_welcome_canvas.create_text(400, 400, text="Emily Song, Ray Xu, Elisa Carrilo, Tyler N.",
                                       font=("Proxima Nova Rg", 20), justify="center")
    hangman_welcome_canvas.create_text(400, 510, text="Thank you\nfor playing!", font=("ProximaNova-Bold", 60),
                                       justify="center")
    hangman_welcome_canvas.create_text(400, 400, text="Emily Song, Ray Xu, Elisa Carrilo, Tyler N.",
                                       font=("Proxima Nova Rg", 20), justify="center")
    backButtonFunc()
 
 
def backButtonFunc():
    backButton = Button(hangman, text="Back", font=("Proxima Nova Rg", 15), height=1, width=5,
                        command=lambda: [hangman_welcome_canvas.delete("all"), main_interface()])
    backButton.configure(width=5, activebackground="white", relief=FLAT)
    backButtonWindow = hangman_welcome_canvas.create_window(700, 550, anchor=NW, window=backButton)
 
 
def backButtonChooseCategoryFunc():
    backButton = Button(hangman, text="Back", font=("Proxima Nova Rg", 15), height=1, width=5,
                        command=lambda: [hangman_welcome_canvas.delete("all"), play_single()])
    backButton.configure(width=5, activebackground="white", relief=FLAT)
    backButtonWindow = hangman_welcome_canvas.create_window(700, 550, anchor=NW, window=backButton)
 
 
def main_interface():
    hangman_welcome_canvas.create_text(400, 80, text="Welcome to HANGMAN!", font=("ProximaNova-Bold", 50))
    hangman_welcome_canvas.create_text(400, 170, text="Choose a Game Mode",
                                       font=("Proxima Nova Rg", 42))
    #hangman_welcome_canvas.create_text(400, 580, text="Made by: Emily, Ray, Elisa, Tyler. August 2017",
     #                                  font=("Proxima Nova Rg", 13))
 
    singlePlayerButton = Button(hangman, text="Single Player", font=("Proxima Nova Rg", 30), height=1, width=20,
                                command=play_single)
    singlePlayerButton.configure(width=20, activebackground="white", relief=FLAT)
    singlePlayerButton_window = hangman_welcome_canvas.create_window(150, 230, anchor=NW, window=singlePlayerButton)
 
    multiPlayerButton = Button(hangman, text="Multi-Player", font=("Proxima Nova Rg", 30), height=1, width=20,
                               command=play_multi)
    multiPlayerButton.configure(width=20, activebackground="white", relief=FLAT)
    multiPlayerButton_window = hangman_welcome_canvas.create_window(150, 330, anchor=NW, window=multiPlayerButton)
 
    quitButton = Button(hangman, text="Exit", font=("Proxima Nova Rg", 30), height=1, width=20, command=hangman.destroy)
    quitButton.configure(width=20, activebackground="white", relief=FLAT)
    quitButton_window = hangman_welcome_canvas.create_window(150, 430, anchor=NW, window=quitButton)
 
    creditsButton = Button(hangman, text="Credits", font=("Proxima Nova Rg", 15), height=1, width=5,
                           command=showCredits)
    creditsButton.configure(width=5, activebackground="white", relief=FLAT)
    creditsButton_window = hangman_welcome_canvas.create_window(700, 550, anchor=NW, window=creditsButton)
 
 
hangman = tk.Tk()
hangman.wm_title("Hangman")
hangman_welcome_canvas = tk.Canvas(hangman, width=800, height=600, borderwidth=2, highlightthickness=1, bg="#ffffff")
hangman_welcome_canvas.pack()
main_interface()
hangman.mainloop()
