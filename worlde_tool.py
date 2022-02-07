from os import stat
from game import Game
from functions import *


dictionary_file = "words.txt"

with open(dictionary_file) as df:
    five_letter_words = df.read().split()
    statistics = Game(five_letter_words)

    while True:
        input_line = input()
        for command in input_line.split():
            
            if 'sample' in command:
                statistics.sampleFiveLetterScores(20, heterogram=True)
                continue
            
            if 'Gray' in command and not 'Gray2' in command:
                char = insideParentheses(command)
                statistics.removeLetter(char)
                continue
            
            else:
                char, pos = getCharPos(command)
                
                if 'Green' in command:
                    statistics.correctLetterCorrectPosition(char,pos)
                    
                if 'Yellow' in command:
                    statistics.correctLetterWrongPosition(char,pos)
                
                if 'Gray2' in command:
                    statistics.secondLetterNotInPosition(char,pos)
            
              
            if input_line[-1] == ';': statistics.sampleFiveLetterScores(20, heterogram=True)









    








    # statistics.removeLetter('H')
    # statistics.correctLetterCorrectPosition('T', 4)
    # statistics.correctLetterWrongPosition('I', 1)
    
    
    # statistics.removeLetter('F')
    # statistics.removeLetter('L')
    # statistics.removeLetter('N')

    # statistics.correctLetterCorrectPosition('I', 2)
    # statistics.sampleFiveLetterWords(100)




