from riot_api_request_handler import RequestHandler
from match import Match

class Matchlist():
    def __init__(self, summoner):
        self.__summoner = summoner
        self.__request = RequestHandler(self.__summoner.getRegion())
        self.update()

    def update(self):
        matchlist = self.__request.lookupMatchlist(self.__summoner.getID())['matches']
        self.__matches = []
        for entry in matchlist:
            match = Match(entry['matchId'], self.__summoner.getRegion())
            self.__matches.append(match)

    def getMatches(self):
        return self.__matches

    def getMatchIds(self):
        matchIDs = []
        for match in self.__matches:
            matchIDs.append(match.getId())
        return matchIDs

    def getMatch(self, matchId):
        pass