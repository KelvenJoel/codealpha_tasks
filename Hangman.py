"""
            TASK ONE: HANGMAN GAME
User gives a list of words
A random word is generated from the list
User then guesses the word one letter at a time. User can guess any letter at any position(ie. we're not following an order)
However, once a letter is guessed, it'll apply to all its occurrences 
User has a total of 6 attempts for the whole word(not 6 lives per letter)
"""
import random
def word_list_func():
    """Take a list of words from user & Return a random word"""
    #Print welcome msg and ask of user's name
    print("\t\t\t\t\t----HANGMAN GAME----")
    
    while True: #Check for alphabet inputs
        try:
            no_of_words = int(input("How many words do you want to add:--> "))
        except ValueError:
            print("Numbers only: Alphabets/spaces not allowed\n")
        else:
            word_list = []
            for i in range(no_of_words):#Take n-words
                if i == 0:# if 1st word, use 1st not 1th
                    word = input(f"Enter the {i+1}st word:--> ").lower()
                elif i== 1:
                    word = input(f"Enter the {i+1}nd word:--> ").lower()
                elif i == 2:
                    word = input(f"Enter the {i+1}rd word:--> ").lower()
                else:
                    word = input(f"Enter the {i+1}th word:--> ").lower()
                word_list.append(word)

            random_word = random.choice(word_list) #Choose a random word from the word list
            
            return random_word#return in a function ends the function even if the 'return' is under a loop
    
def display_current_state(pairing_list):
    """
    Take a 2D list input.Iterate through the list and store the 2nd item of each iteration in another 
    list. Return the current state of user's guesses
    """
    present_list = []
    for position_guess,letter_guess in pairing_list: 
        present_list.append(letter_guess)
    return "".join(present_list)

def count_attempt(guess,attempts):
    """
    Take the guess letter user makes and the current number of attempts made.
    Keep track of any incorrect or unallowed guesses.
    Return number of attempts made
    """
    attempts += 1#Write a proper code for the attempt
    if len(guess) != 1:#User doesn't guess a letter at a time
        print(f"Oops!!\nYou entered {len(guess)} characters")
        print("You can only enter a letter at a time!!")
        print(f"You have made {attempts}/6 incorrect attempts")
    else:#User guessed one letter but letter not in random word
        print(f"'{guess}' not in the hidden word")
        if guess.isdigit(): #if user guess is a number and  we assume none of the words have a number in them
            print("Numbers are not allowed")
        print(f"You have made {attempts}/6 incorrect attempts")#Tell user the number of attempts he has made for a wrong guess
    return attempts

def actual_game(random_word):
    attempts = 0
    guess = ""
    current_state = "_"*len(random_word)
    pairing_random_word = list(enumerate(random_word))#Pair each letter in the random word with its index
    #pairing_current_state = list(enumerate(current_state))#Enumerate or zip won't let you change the dashes because they give tuples
    pairing_current_state = []
    
    #We want to pair positions(indices) with letters so we that we can CHANGE dashes to letters:
    #Enumerate or zip won't let you change the dashes because they give tuples
    i=0
    for j in current_state:
        pairing_current_state.append([i,j])
        i+=1
   
    print("_ "*len(random_word)) #Print dashes to represent unguessed letters
    while not(attempts >= 6 or ( current_state== random_word)): #Stop loop if more than 6 attempts or guess is right
        #Or is false when both are false. Nor is false when one is true and true when both are false
        #Note when to use ! and not
        guess = input("Guess a letter(one-letter at a time):--> ").lower()

        #Check if the guess letter is in the random word. If so, position of guess in the random word should 
        #have the same letter as that in current state. 
        #change the dash in that position to the guessed letter
        #if len(guess) > 1:#Handle moments when user guesses more than
        if len(guess) != 1:
            attempts = count_attempt(guess,attempts)
            current_state = display_current_state(pairing_current_state)
        elif guess in random_word: 
            for position_random,letter_random in pairing_random_word:#Getting the position of the guessed letter
                if guess==letter_random:
                    for position_guess,letter_guess in pairing_current_state:
                        pairing_current_state[position_random][1]= guess

            current_state = display_current_state(pairing_current_state)

        else:#Guessed letter not in word
            attempts = count_attempt(guess,attempts)
            current_state = display_current_state(pairing_current_state)

        print(f"{current_state}\n")

    #Print a congratulatory msg or otherwise
    if attempts >= 6:
        print(f"You lost. All 6 lives lost!\nThe hidden word is '{random_word}'")
    elif current_state == random_word:
        print(f"You won. The hidden word is '{random_word}'")

actual_game(word_list_func())
