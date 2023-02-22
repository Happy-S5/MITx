# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
from platform import python_version
import functools

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    oxfordDict = {}

    with open("OxfordDictionaryAnsi.txt", "r") as f:
        for line in f:
            line = line.strip().split(" ",1)
            word = ''.join(line[0:1])
            definition = line[:2]
            #print (word)
            #definition = line[1]
            #print (definition)    

                    #count =+ 1
            oxfordDict[word] = definition
            
     
    print("  ", len(oxfordDict), "words loaded.")
    return oxfordDict

def keywordValue(oxfordDict):
    
    
    value = oxfordDict[secretWord]
    
    return value
    
def chooseWord(oxfordDict):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    
    """
    key = random.choice(list(oxfordDict.keys()))
    value = oxfordDict[key]
    
    return key, value
# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
oxfordDict = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    list1 =[]
    secretWord = secretWord.lower()
    ans = [x for x in lettersGuessed if x in secretWord]
    
    ans = sorted(ans)
    #print('The letters guessed are', ans)
    list1[:0] = secretWord
    list1 = set(list1)
    list1 = list(list1)
    list1 = sorted(list1)
    #print('The secret word is:', list1)
    
    
    if ans == list1: 
        return True
    else: 
        return False  
  
  

  


    
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    count = 0
    Hang = []
    secretWordList = []
    secretWordList[:0] = secretWord.lower()
    secretWordList1 = secretWordList[:]
     
    Hang = [' _ ' for x in secretWordList1]
   
    for e in lettersGuessed: 
        count = 0
        for i in secretWordList1: 
            count = secretWordList1.index(i)
            if e == i: 
                Hang[count] = e 
                secretWordList1[count]='*'
                temp = i
                count = 0
    Hang = ''.join(Hang)
    
                     
    return Hang   
  
    

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    
    alphabetList = [] #Declare the lists
    alphabetList1 = []
    alphabet = "abcdefghijklmnopqrstuvwxyz-à"
    alphabetList[:0] = alphabet #Mkae the string into a list
    length = len(alphabetList)
   
    #List comprehension. Think of not in as exclude. 
    alphabetList1 = ''.join([x for x in alphabetList if x not in lettersGuessed])
    
    return alphabetList1
    
    

def hangman(secretWord, value):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    
    secretWord = secretWord.lower()
    guesses = 8
    lettersGuessed = [] 
    Guess = ''
    wordGuessed = None
    GoodGuess = ''
    
    print("Current Python Version-", python_version())
    print("Welcome to the game of Hagman!")
    print("I am thinking of a word that is", len(secretWord), "letters long!")
    print("_ _ _ _ _ _ _ _ _ _")
        
    while guesses > 0:
        
        
        print('You have', guesses, 'left!')
        print('Available letters: ', getAvailableLetters(lettersGuessed))
        Guess = input('Please guess a letter: ')
        Guess = Guess.lower()
        
        if Guess in lettersGuessed: 
            print("Oops! You have already Guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
            print("_ _ _ _ _ _ _ _ _ _")
            
        if Guess not in lettersGuessed:
            lettersGuessed.append(Guess)
            
            if Guess in secretWord: 
                
                print('Good guess!:', getGuessedWord(secretWord, lettersGuessed))
                
                print("_ _ _ _ _ _ _ _ _ _")
                
                
                if isWordGuessed(secretWord, lettersGuessed) == True: 
                    print('Congratulations, you won!')
                    break
                   
                 
            elif Guess not in secretWord:
                guesses -= 1
                print('Oops! That letter is not in my word: ', getGuessedWord(secretWord, lettersGuessed))
                print('_ _ _ _ _ _ _ _ _ _')
                
            if guesses == 0: 
                print ('Sorry, you ran out of guesses. The word was', secretWord)
                
                #print('The definition of the word is:', value)
    print('The definition of the word is:', value)
    
                




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

#secretWord= 'self-sealing'
#value = "Yo lean on"
secretWord, value = chooseWord(oxfordDict)
hangman(secretWord, value)


