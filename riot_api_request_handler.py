import requests

class RequestHandler:
    def __init__(self, region):
        self.__api_key = open('api_key.txt', 'r').read()
        self.__regions = ('na', 'euw', 'kr')


        if region in self.__regions:
            self.__riot_api_url = 'https://' + region + '.api.pvp.net/api/lol/' + region
        else:
            #default to na
            self.__riot_api_url = 'https://na.api.pvp.net/api/lol/na'

#public functions
    def lookupSummonerByName(self, summonerName, params={}):
        url = self.__createURL('/v1.4/summoner/by-name/' + str(summonerName))
        return self.__executeRequest(url, params)

    def lookupSummonerById(self, summonerId, params={}):
        url = self.__createURL('/v1.4/summoner/' + str(summonerId))
        return self.__executeRequest(url, params)

    def lookupChallengers(self, params={}):
        url = self.__createURL('/v2.5/league/challenger')
        return self.__executeRequest(url, params)

    def lookupMatchlist(self, summonerID, params={}):
        url = self.__createURL('/v2.2/matchlist/by-summoner/' + str(summonerID))
        return self.__executeRequest(url, params)


    def lookupMatch(self, matchID, params={}):
        url = self.__createURL('/v2.2/match/' + str(matchID))
        return self.__executeRequest(url, params)


#private functions
    def __createURL(self, method):
        return (self.__riot_api_url + method).replace(' ', '%20') #return the sanatized method with method attached

    def __validateRequest(self, request):
        if request.status_code == 200:
            return True
        else:
            print(request.status_code)
            return False

    def __executeRequest(self, url, params):
        params.update({'api_key': self.__api_key})
        #Validate URL
        if url:
            request = requests.get(url, params) #execute request

        #Validate request
        if self.__validateRequest(request):
            return request.json()



