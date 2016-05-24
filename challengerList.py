from riot_api_request_handler import RequestHandler

class ChallengerList:
    def __init__(self, region):
        self.__request = RequestHandler(region)
        self.update()

    def update(self):
        self.__challengers = self.__request.lookupChallengers({'type': 'RANKED_SOLO_5x5'})

    def getChallengers(self):
        return self.__challengers