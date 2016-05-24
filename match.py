from riot_api_request_handler import RequestHandler

class Match:
    def __init__(self, matchID, region):
        self.__matchID = matchID
        self.__region = region
        self.__request = RequestHandler(region)
        self.update()

    def __init__(self, match):
        self.__matchID = match.getId()
        self.__region = match.getRegion()
        self.__request = RequestHandler(self.__region)
        self.update()

    def update(self):
        self.__stats = self.__request.lookupMatch(self.__matchID)

    def getStats(self):
        return self.__stats

    def getId(self):
        return self.__matchID

    def getRegion(self):
        return self.__region
