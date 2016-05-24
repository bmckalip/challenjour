from challengerList import challengerList
from matchList import matchlist
from matchStats import matchStats
import mysql.connector as mariadb
from summoner import summoner

#do this for all supported regions
regions = ['na', 'euw', 'kr']
connection = mariadb.connect(user='', password='', database='')
cursor = connection.cursor()

for region in regions:
    #update list of challengers
    players = challengerList('na')
    challengers = players.getChallengers()

    #update list of challenger matchlists
    for challenger in challengers:
        player = summoner(challenger['playerOrTeamId'], region)
        matchlist = matchlist(player)
        matchIDs = matchlist.getMatchlistIDs()

        localMatches = []
        for matchID in matchIDs:
            if matchID not in localMatches:
                stats = matchStats(matchID, region)



