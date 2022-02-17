from flask import Flask, request
from game_service import GameService
import json

app = Flask(__name__)

game_service = GameService()
    

@app.route('/')
def home():
    return "Welcome To a Wordle Helper Api"


@app.route('/api/words')
def getWordsRoute():
    return game_service.getAllWords()

@app.route('/api/active_words')
def getActiveWordsRoute():
    return game_service.getActiveWords()


@app.route('/api/move', methods=['POST'])
def doMoveRoute():
    request_data = request.get_json()
    res = game_service.doMove(request_data)
    return json.dumps(res)


@app.route('/api/restart', methods=['POST'])
def doRestartRoute():
    res = game_service.restartGame()
    return json.dumps(res)

@app.route('/api/words_rated/<n>')
def getWordsRatedRoute(n):
    res = game_service.getWordsRated(100)
    return json.dumps(res)
