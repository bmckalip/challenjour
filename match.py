from riot_api_request_handler import RequestHandler

class Match:
    def __init__(self, matchID, region):
        self.__matchID = matchID
        self.__region = region
        self.__request = RequestHandler(region)
        self.update()

    def update(self):
        self.__stats = self.__request.lookupMatch(self.__matchID)
        self.__createParticipantList()

    def getStats(self):
        return self.__stats

    def getId(self):
        return self.__matchID

    def getRegion(self):
        return self.__region

    def __createParticipantList(self):
        self.__participants = []
        for participant in self.__stats['participantIdentities']:
            self.__participants.append(participant)

        self.__participantStats = []
        for stat in self.__stats['participants']:
            self.__participantStats.append(stat)

    def __findParticipant(self, summonerId):
        for participant in self.__participants:
            if (participant['player'])['summonerId'] == int(summonerId):
                return self.__participantStats[participant['participantId']]

    def getParticipant(self, summonerId):
        return self.__findParticipant(summonerId)

    def getParticipantRunes(self, summonerId):
        return self.__findParticipant(summonerId)['runes']

    def getParticipantMasteries(self, summonerId):
        return self.__findParticipant(summonerId)['masteries']

    def getParticipantStats(self, summonerId):
        return self.__findParticipant(summonerId)['stats']

    def getParticipantTimeline(self, summonerId):
        return self.__findParticipant(summonerId)['timeline']

    def getParticipantChampionId(self, summonerId):
        return self.__findParticipant(summonerId)['championId']

    def getParticipantSummonerSpellIds(self, summonerId):
        return (self.__findParticipant(summonerId)['spell1Id'], self.__findParticipant(summonerId)['spell2Id'])
