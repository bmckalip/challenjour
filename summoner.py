from riot_api_request_handler import requestHandler

class summoner:
    def __init__(self, summonerID, region):
        self.__summonerID = summonerID
        self.__region = region
        self.__rh = requestHandler(self.__region)
        self.__name =  self.__rh.lookupSummoner(self.__summonerID)

    def getID(self):
        return self.__summonerID
    def getName(self):
        return  self.__name
    def getRegion(self):
        return self.__region