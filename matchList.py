from riot_api_request_handler import RequestHandler
from match import Match

class Matchlist():
    def __init__(self, summonerId, region):
        self.__summonerId = summonerId
        self.__region = region
        self.__request = RequestHandler(self.__region)
        self.update()

    def update(self):
        matchlist = self.__request.lookupMatchlist(self.__summonerId)['matches']
        self.__matches = []
        for entry in matchlist:
            match = Match(entry['matchId'], self.__region)
            self.__matches.append(match)
            break;

    def getMatches(self):
        return self.__matches

    def getMatchIds(self):
        matchIDs = []
        for match in self.__matches:
            matchIDs.append(match.getId())
        return matchIDs

    def getMatch(self, matchId):
        pass