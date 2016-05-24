from riot_api_request_handler import requestHandler

class challengerList:
    def __init__(self, region):
        self.__region = requestHandler(region)
        self.update()

    def update(self):
        self.__challengers = self.__region.lookupChallengers({'type': 'RANKED_SOLO_5x5'})

    def getChallengers(self):
        return self.__challengers