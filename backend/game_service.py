import json
from game import *
from responses import *
class GameService:
    
    def __init__(self):
        self.game = Game()
        
    def getAllWords(self):
        words = self.game.all_words
        return json.dumps(words)
    
    def getActiveWords(self):
        words = self.game.five_letter_words
        return json.dumps(words)

    def doMove(self,results_dicts): 
        for key in results_dicts: 
            if key == "gray":
                for letter in results_dicts[key]:
                    self.game.removeLetter(letter)
            if key == "gray2":
                for pair in results_dicts[key]: self.game.secondLetterNotInPosition(pair[0],pair[1])            
            if key == "green":
                for pair in results_dicts[key]: self.game.correctLetterCorrectPosition(pair[0],pair[1])    
            if key == "yellow":
                for pair in results_dicts[key]: self.game.correctLetterWrongPosition(pair[0],pair[1])    
        return move_done_successfully_reponse

    def restartGame(self): 
        self.game = Game() 
        return game_restarted_successfully_reponse

    def getWordsRated(self,n): 
        words = self.game.sampleFiveLetterScores(n,False)
        heterograms = self.game.sampleFiveLetterScores(n,True)
        r = {
            "heterograms" : heterograms,
            "words" : words
        }
        return r