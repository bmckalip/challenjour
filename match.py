from riot_api_request_handler import RequestHandler
from matchParticipant import MatchParticipant

class Match:
    def __init__(self, matchID, region):
        self.__matchID = matchID
        self.__region = region
        self.__request = RequestHandler(region)
        self.update()

    def update(self):
        self.__matchData = self.__request.lookupMatch(self.__matchID)
        self.__createParticipantList()

    def getStats(self):
        return self.__matchData

    def getId(self):
        return self.__matchID

    def getRegion(self):
        return self.__region

    def __createParticipantList(self):
        self.__participants = []
        for player in self.__matchData['participantIdentities']:
            stats = self.__matchData['participants'][player['participantId'] - 1]
            participant = MatchParticipant(player, stats)
            self.__participants.append(participant)

    def getParticipant(self, summonerId):
        for participant in self.__participants:
            if (participant.getId()) == int(summonerId):
                return participant