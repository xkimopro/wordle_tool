
import string, random, functools
from collections import OrderedDict,Counter
from functions import *

def isHeterogram(word):
    letter_counter = Counter(list(word))
    for cnt in letter_counter.values(): 
        if cnt > 1: return False
    return True    


def updateScoresDecorator(func):
        @functools.wraps(func)
        def wrapper_decorator(*args, **kwargs):
            value = func(*args, **kwargs)
            args[0].updateScores() 
            return value
        return wrapper_decorator


class Game:
    def __init__(self):
        with open("words.txt") as df:
            all_words = df.read().split()
            self.all_words = all_words   
            self.five_letter_words = all_words
            self.freq,self.five_letter_words_scores = {},{}
            self.uppercase_letters = string.ascii_uppercase
            self.correct_letters_wrong_positions, self.correct_letters_correct_positions, self.removed_letters = [],[],[]
            self.updateScores()
        

    @updateScoresDecorator
    def removeLetter(self, letter):
        self.removed_letters.append(letter)
        new_five_letter_words = list(filter(lambda w: letter not in list(w), self.five_letter_words))
        self.five_letter_words = new_five_letter_words

    @updateScoresDecorator
    def correctLetterCorrectPosition(self, letter, pos):
        letter_pos_tuple = (letter,pos)
        self.correct_letters_correct_positions.append(letter_pos_tuple)
        new_five_letter_words = list(filter(lambda w: list(w)[pos] == letter, self.five_letter_words))
        self.five_letter_words = new_five_letter_words
    
    @updateScoresDecorator
    def correctLetterWrongPosition(self, letter, pos):
        letter_pos_tuple = (letter,pos)
        self.correct_letters_wrong_positions.append(letter_pos_tuple)
        new_five_letter_words = list(filter(lambda word: self.correctLetterWrongPositionChecker(letter, pos, word) , self.five_letter_words))
        self.five_letter_words = new_five_letter_words

    def correctLetterWrongPositionChecker(self, letter, pos, word): 
        if list(word)[pos] == letter: return False
        for l in list(word): 
            if l == letter: return True

    @updateScoresDecorator
    def secondLetterNotInPosition(self,letter, pos):
        new_five_letter_words = list(filter(lambda w: letter != list(w)[pos], self.five_letter_words))
        self.five_letter_words = new_five_letter_words

    def wordScore(self, word ):
        score = 0
        for letter in list(word): score += self.freq[letter]
        return score



    def getLetterFrequencyFiveLetterWords(self,):
        uppercase_letters_count = {u : 0 for u in self.uppercase_letters}
        for word in self.five_letter_words:
            letters = list(word)
            for letter in letters: uppercase_letters_count[letter] += 1
        self.freq = OrderedDict(uppercase_letters_count)

    
    def updateScores(self, ):
        self.getLetterFrequencyFiveLetterWords()
        five_letter_words_scores = {w : self.wordScore(w) for w in self.five_letter_words}
        sorted_tuples = sorted(five_letter_words_scores.items(), key=lambda item: item[1], reverse=True)
        self.five_letter_words_scores = {k: v for k, v in sorted_tuples}

    def sampleFiveLetterWords(self, n ):
        random.shuffle(self.five_letter_words)
        for i , word in enumerate(self.five_letter_words):
            print(word)
            if i == n-1: break
        print()

    def sampleFiveLetterScores(self, n, heterogram):
        times = 0
        words = []
        for word, score in self.five_letter_words_scores.items():
            if n == times: break
            if not isHeterogram(word) and heterogram: continue
            print(word + " " + str(score))
            words.append(word)
            times+=1
        print()
        return words
        

    def testingFunction(self,):
        print("Test")
        return "Test"
