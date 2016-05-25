class MatchParticipant:
    def __init__(self, identity, stats):
        self.__summonerId = identity['player']['summonerId']
        self.__data = stats

    def __init(self, participant):
        self.___summonerId = participant.getId()
        self.__data = participant.getData()

    def getId(self):
        return self.__summonerId

    def getData(self):
        return self.__data

    def getRunes(self):
        return self.__data['runes']

    def getMasteries(self):
        return self.__data['masteries']

    def getStats(self, stat=None):
        if stat is None:
            return self.__data['stats']
        else:
            return self.__data['stats'][stat]

    def getTimeline(self,):
        return self.__data['timeline']

    def getChampionId(self,):
        return self.__data['championId']

    def getSummonerSpellIds(self,):
        return (self.__data['spell1Id'], self.__data['spell2Id'])