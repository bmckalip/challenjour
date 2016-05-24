from riot_api_request_handler import RequestHandler
from matchList import Matchlist

class Summoner:
    def __init__(self, summonerID, region):
        self.__summonerID = summonerID
        self.__region = region
        self.__request = RequestHandler(self.__region)
        self.__summoner = self.__request.lookupSummonerById(self.__summonerID)[str(self.__summonerID)]
        self.__summonerName = self.__summoner['name']
        self.__matchlist = Matchlist(self.__summonerID, self.__region)

    def getID(self):
        return self.__summonerID

    def getName(self):
        return self.__summonerName

    def getRegion(self):
        return self.__region

    def getMatches(self):
        return self.__matchlist