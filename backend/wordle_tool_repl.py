from os import stat
from game import Game
from functions import *



statistics = Game()

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
