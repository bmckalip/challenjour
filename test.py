from summoner import Summoner
from riot_api_request_handler import RequestHandler

region = 'na'
name = 'bmc'
request = RequestHandler(region)
player = request.lookupSummonerByName(name)
print(player)

playerId = (player[name])['id']
summoner = Summoner(playerId, region)
#print(summoner.getName())