###############################################################################################
scrabbleScores = [ ["a", 1], ["b", 3], ["c", 3], ["d", 2], ["e", 1], 
                 ["f", 4], ["g", 2], ["h", 4], ["i", 1], ["j", 8], 
                 ["k", 5], ["l", 1], ["m", 3], ["n", 1], ["o", 1], ["p", 3], 
                 ["q", 10], ["r", 1], ["s", 1], ["t", 1], ["u", 1], ["v", 4], 
                 ["w", 4], ["x", 8], ["y", 4], ["z", 10] ]
##The letterCheck function checks to see if the string entered as input
##is a number or a letter. The function returns True if the input is a letter,
##False if it is a number by using try. 
def letterCheck(letter):
    '''This function checks to see if the input is a number or word'''
    try:
        float(letter)
        return True
    except ValueError: #the exception is added as the program crashes here
        return False#with the help of the exception it can bypass the error. 

##This is the new letterScore  which is made to work with filter. It takes
##in the letter entered as the input and computes the value from a given list.
##In this case the list given with the score is scrabbleScores. The final output
##is determined by the score computed by the list. 
def letterScore(letter, scoreList):
    '''Takes in input as letter and returns the score'''
    if scoreList == [] or letter == "" or letterCheck(letter) == True:
        return 0
    elif len(letter) >= 2: 
        return 0
    else:
        lettervalue = filter(lambda x: x[0][0] == letter, scoreList)
        return lettervalue [0][1]
            ##To check if the input is a number or letter:
            ##>>> letterScore("2", scrabbleScores)
            ##0
            ##>>> letterScore("a", scrabbleScores)
            ##1
###### 
##This is the modified wordScore. It uses map and reduce to compute the score of a
##word entered. The final output is determined by the score of the word computed from
##the given list. It uses the letterScore function to compute the score. 
def wordScore(word, scoreList):
    ''''redefines the wordScore function to work with map, reduce and lambda. Takes in a word and
computes its score.'''
    if word:
        score = map(lambda x: letterScore(x[0], scoreList), word)
        return reduce(lambda a,b: a+b, score)
            ##To check if the wordScore works:
            ##>>> wordScore("spam", scrabbleScores)
            ##8
            ##>>> wordScore("22", scrabbleScores)
            ##0
###### 
Dictionary = ["a", "am", "at", "apple", "bat", "bar", "babble", "can", "foo", "spam", "spammy",
              "zzyzva"]
####
#list comprehensions:
words = [x for x in Dictionary]
twoLetterWords = [x for x in Dictionary if len(x)==2]
lengths = [len(x) for x in Dictionary]
#
####
##The counter function checks to see if any of the letters in the word entered as the
##input exist in the rack. In the case where it does, it adds 1 to the variable count
##otherwise, it just ignores it. The output is the sum of count at the end. 
def counter(theRack, S):
    '''The function checks to see if the letters in a word match
    any letters in the rack, adds 1 if it exists.'''
    count = 0
    if S:
        if S[0] in theRack:
            return 1 + count + (counter(theRack, S[1:]))
        else:
            return count + (counter(theRack, S[1:]))
    else:
            return 0
##The TrueOrfalse function uses the counter function to check if the sum of count
##is equal to the length of the word. It returns true, if the length is equal,
##false for vice versa. 
def TrueOrFalse(Count, Word):
    '''Compares the output of counter and the length of the word.'''
    if Count:
        if Count == len(Word):
            return True
        else:
            return False
    else:
        return False
##addValue function takes in a list of words and returns them side by side with their
##respective wordScore.
def addValue(List):
    '''Takes input as a list of words and returns them with the wordScore'''
    if List:
        return [[List[0]] + [wordScore(List[0], scrabbleScores)]] + addValue(List[1:])
    else:
        return []
##After that, the scoreList filters through the dictionary using the counter function and
##TrueOrFalse function. For the words that returned true, the function adds them to a
##different list (in this case it is the goodList). The ones that returned false are ignored.
##The goodList is returned as final output. 
def scoreList(Rack):
    '''filters through the dictionary and using the counter function and
    the TrueOrFalse function.'''
    goodList = filter(lambda x: TrueOrFalse(counter(Rack, x),x) is True, words)
    return addValue(goodList)
##Results for scoreList-
##>>> scoreList(["a", "s", "m", "t", "p"])
##[['a', 1], ['am', 4], ['at', 2], ['spam', 8]]
##>>> scoreList(["a", "s", "m", "o", "f", "o"])
##[['a', 1], ['am', 4], ['foo', 6]]
def bestWord(Rack):
    '''takes as input a Rack and returns the highest possible scoring word from that
    Rack and its score.'''
    scorelist = scoreList(Rack)
    return reduce(lambda x,y: x if x[1] > y[1] else y, scorelist)
##Results for bestWord-
##>>> bestWord(["a", "s", "m", "t", "p"])
##['spam', 8]
##>>> bestWord(["a", "s", "m", "o", "f", "o"])
##['foo', 6]
###############################################################################################



        
