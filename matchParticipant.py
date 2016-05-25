class MatchParticipant:
    def __init__(self, identity, stats):
        self.__summonerId = identity['player']['summonerId']
        self.__data = stats
        self.__publicQueriableStats = [
            "unrealKills",
            "totalDamageTaken",
            "pentaKills",
            "sightWardsBoughtInGame",
            "winner",
            "magicDamageDealt",
            "wardsKilled",
            "largestCriticalStrike",
            "trueDamageDealt",
            "doubleKills",
            "physicalDamageDealt",
            "tripleKills",
            "deaths",
            "firstBloodAssist",
            "magicDamageDealtToChampions",
            "assists",
            "visionWardsBoughtInGame",
            "totalTimeCrowdControlDealt",
            "champLevel",
            "physicalDamageTaken",
            "totalDamageDealt",
            "largestKillingSpree",
            "inhibitorKills",
            "minionsKilled",
            "towerKills",
            "physicalDamageDealtToChampions",
            "quadraKills",
            "goldSpent",
            "totalDamageDealtToChampions",
            "goldEarned",
            "neutralMinionsKilledTeamJungle",
            "firstBloodKill",
            "firstTowerKill",
            "wardsPlaced",
            "trueDamageDealtToChampions",
            "killingSprees",
            "firstInhibitorKill",
            "totalScoreRank",
            "totalUnitsHealed",
            "kills",
            "firstInhibitorAssist",
            "totalPlayerScore",
            "neutralMinionsKilledEnemyJungle",
            "magicDamageTaken",
            "largestMultiKill",
            "totalHeal",
            "objectivePlayerScore",
            "firstTowerAssist",
            "trueDamageTaken",
            "neutralMinionsKilled",
            "combatPlayerScore",
            "items"
            ]
        self.__stats = self.__data['stats']
        self.__items = {'items': [self.__stats['item0'],
                                  self.__stats['item1'],
                                  self.__stats['item2'],
                                  self.__stats['item3'],
                                  self.__stats['item4'],
                                  self.__stats['item5'],
                                  self.__stats['item6']
                                  ]
                        }

        self.__stats.update(self.__items)

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
            return self.__stats
        else:
            if stat in self.__publicQueriableStats:
                return self.__stats[stat]
    def getItems(self):
        return self.stats['items']

    def getTimeline(self,):
        return self.__data['timeline']

    def getChampionId(self,):
        return self.__data['championId']

    def getSummonerSpellIds(self,):
        return (self.__data['spell1Id'], self.__data['spell2Id'])