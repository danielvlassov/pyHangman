# Word Guessing game
# Hangman type game where you guessed the hidden letters in a word. 5 strikes, and you're out!
# Daniel Vlassov
# 10/9/2020

# imports random
import random

UPPERCASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
LOWERCASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# init getWord function 
def getWord(masterList):
    # choice = random integer choice of the master list, with range of 0 to length of the masterlist minus one, to account for index.
	choice = random.randint(0,(len(masterList)-1))
	#returns the choice to function call
	return choice
# end indent

# init instruct function
def instruct():
	# prints a list of instructions
	print(" ")
	print(" ")
	print("You will be given a randomly generated word.")
	print("You have up to 5 incorrect guesses before you fail.")
	print("To win, guess all the letters right!")
	print("")
	# Takes user input in form of enter to act as a buffer when read, then executes the optionRedirect() function call
	input("Press Enter to return to the main menu.\t")
	optionRedirect()
#end indent

#init optionRedirect function
def optionRedirect():
    # Prints the welcome screen with options 
    print("")
    print("Welcome to Word Guesser!")
    print("")
    print("1: Play!")
    print("2: Display Instructions.")
    print("3: Quit.")
    print("")
	# option = the result of the chosen option to run the program (1,2 or 3)
    option = (input(" Please select option \n  | 1 | 2 | 3 | and \n     press Enter!\n\n\t\t> "))
	# if option == 1, then call play() function
    if option == "1":
	    play()
	#end indent
	# elif option is 2, call the instruct() function
    elif option == "2":
        instruct()
	#end indent
	# elif option is 3, then quit the program.
    elif option == "3":
		#quit placeholder
        pass
	#end indent
	# all else, prints Invaild Entry and to try again, calling optionRedirect()
    else:
        print("")
        print("")
        print(" >>> Invaild Entry. Try Again. <<< ")
        print("")
        print("")
        optionRedirect()
#end indent

# init the checkIndex() function (checks which index it's in)
def checkIndex(tempGuess, wordInit):
    # start indent
    matchingIndices = []
    for i in range(0, len(wordInit)):
        # start indent
        if wordInit[i] == tempGuess:
            # start indent
            matchingIndices = matchingIndices + [i]
    # end indent
    return matchingIndices
# end indent

# init loser() function
def loser(wordInit,printClean,guessCur,guessMax):
    # start indent
    # prints that you ran out of tries, the correct word, the ones you had guessed, and an option to play again if pressed enter on the input, clears 8 new lines
    print("")
    print("Sorry! You ran out of tries!")
    print("The word was:",wordInit)
    print("You had the following guessed:", printClean)
    print("Better luck next time!")
    input("Press enter to return to the main menu!")
    print("\n"*8)
    # calls optionRedirect() function
    optionRedirect()
# end indent

# init winner() function
def winner(printClean, guessCur, wordInit, guessMax):
    # start indent
     # prints that you won the game, the word, your wrong attempts, and an option to play again if pressed enter on the input, clears 8 new lines
    print("")
    print("You have won the hangman game!")
    print("You successfully guessed:",wordInit,"with",guessCur,"wrong attempt(s)!")
    input("Press enter to play again!\n")
    print("\n"*8)
    # calls optionRedirect() function
    optionRedirect()
# end indent

#init the guessing() function 
def guessing(guessed, wordInit):
    # Maximum number of guesses before the game sends you the loser() function
    guessMax = 5
    # Counter of wrong attempts init
    guessCur = 0
    # init notGuessed var set to True (changes to False if winner)
    notGuessed = True
    # guessBank init stores the guessed letters
    guessBank = []
    # while current guessers is less than maximum guesser and the word isnt guessed, cont.
    while guessCur < guessMax and notGuessed:
        # prints an empty line
        print("")
        # init printClean var to convert list to a string
        printClean = ""
        # for itiration in range of (0 to length of guessed var)
        for i in range(0, len(guessed)):
            # adds each element of guessed and a space to the string each while itiration
            printClean += guessed[i] + " "
        # prints the clean line
        print(printClean)
        # tempGuess stores the temporary letter guess of the user
        tempGuess = input("What is your guess?:\t")
        # if tempGuess is an uppercase letter, we set it to a lowercase equivalent
        if checkIndex(tempGuess, UPPERCASE):
            tempGuess = LOWERCASE[checkIndex(tempGuess, UPPERCASE)[0]]
        if tempGuess not in LOWERCASE and tempGuess not in UPPERCASE:
            # prints that youre doing something wrong >:)
            print("")
            print("You did something wrong, not me!")
            print("Check to make sure you're only entering one character and no symbols or anything!")


        # if tempGuess is in the word chosen, continue
        elif tempGuess in wordInit:
            # adds tempGuess to the guessBank
            guessBank += tempGuess
            # calls checkIndex() function with the tempGuess and wordInit, and returns
            # matching indicies to replace later
            matchingIndices = checkIndex(tempGuess, wordInit)
            # for loop of each index itiration of matchingIndices
            for index in matchingIndices:
                # sets the index of guessed with matching indices to the guessed letter
                guessed[index] = tempGuess
            # prints the line Correct!
            print("Correct!")
            # Once all letters are guessed, *'s disappear, changing notguessed to false and calling the winner() function
            if "*" not in guessed:
                notGuessed = False
                winner(printClean, guessCur, wordInit, guessMax)
        # elif tempGuess is not in wordInit and tempGuess is not stored in guessBank
        elif tempGuess not in wordInit and tempGuess not in guessBank:
            # adds tempGuess to the guessbank
            guessBank += tempGuess
            # adds one to the current guesses variable
            guessCur += 1
            # prints Incorrect! and tries remaining
            print("Incorrect! You have",guessMax - guessCur,"incorrect guesses remaining!")
            # if guessCur is equal to 2, it drops a hint to the user with the first letter
            if guessCur == 2:
                # prints the hint
                print("Hint! The first letter is:",wordInit[0])
            # if guessCur is equal to guessMax
            if guessCur == guessMax:
                # calls loser() function, loop stops repeating from the while loop itself
                loser(wordInit,printClean,guessCur,guessMax)
        # elif tempGuess not in wordInit and not in the guessBank
        elif tempGuess not in wordInit and tempGuess in guessBank:
            # prints that you already guessed the letter and prints the letter
            print("")
            print("You already guessed the letter! This letter being",tempGuess,"!")
            print("")
        # all else
        else:
            # prints that youre doing something wrong >:)
            print("")
            print("You did something wrong, not me!")
            print("Check to make sure you're only entering one character and no symbols or anything!")



# end indent
# init play function
def play():
	# init masterList of words
	masterList = ['dad','computer','bag','poppy','demon']
	# wordInit is the str of the grabbed list of masterList
	wordInit = str(masterList[getWord(masterList)])
	# init word list
	word = []
	# init guessed list with one "*"
	guessed = ["*"] * len(wordInit)
	# print your word has x ammount of letters, good luck
	print("")
	print("Your word has",(len(wordInit)),"letters! Good Luck!")
	# calls guessing function with guessed and wordInit
	guessing(guessed, wordInit)
# end indent
# init menu function

optionRedirect()