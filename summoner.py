from riot_api_request_handler import RequestHandler
from matchList import Matchlist

class Summoner:
    def __init__(self, summonerID, region):
        self.__summonerID = summonerID
        self.__region = region
        self.__request = RequestHandler(self.__region)
        self.__summonerName = self.__request.lookupSummonerById(self.__summonerID)[self.__summonerID]['name']
        self.__matchlist = Matchlist(self)

    def getID(self):
        return self.__summonerID

    def getName(self):
        return self.__summonerName

    def getRegion(self):
        return self.__region

    def getMatches(self):
        return self.__matchlist