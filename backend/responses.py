import json

class success():
    def __init__(self,msg):
        self.resp = {
            'error_code' : 0,
            'msg' : msg
        }
    
class fail():
    def __init__(self,msg):
        self.resp = {
            'error_code' : 1,
            'msg' : msg
        }
        return json.dumps(self.resp)


move_done_successfully_reponse = success('Move done successfully').resp
game_restarted_successfully_reponse = success('Game restarted successfully').resp

