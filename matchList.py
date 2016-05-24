from challengerList import challengerList
from riot_api_request_handler import requestHandler
from summoner import summoner

class matchlist:
    def __init__(self, summoner):
        self.__summonerID = summoner.getID()
        self.__region = summoner.getRegion()
        self.update()

    def update(self):
        self.__matchlist = self.__region.lookupMatchlist(self.__summonerID)['matches']

    def getMatchlist(self):
        return self.__matchlist

    def getMatchlistIDs(self):
        matchIDs = []
        for match in self.__matchlist:
            matchIDs.append(match['matchId'])
        return matchIDs