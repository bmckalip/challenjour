from riot_api_request_handler import requestHandler

class matchStats:
    def __init__(self, matchID, region):
        self.__matchID = matchID
        self.__region = requestHandler(region)
        self.update()

    def updateStats(self):
        self.__stats = self.__region.lookupMatch(self.__matchID)

    def getStats(self):
        return self.__stats

    