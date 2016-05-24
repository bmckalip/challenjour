from challengerList import ChallengerList
from match import Match
from summoner import Summoner

#do this for all supported regions
regions = ['na', 'euw', 'kr']

for region in regions:
    #update list of challengers
    players = ChallengerList('na')
    challengers = players.getChallengers()

    #update list of challenger matchlists
    for challenger in challengers['entries']:
        player = Summoner(challenger['playerOrTeamId'], region)
        matchlist = player.getMatches()
        matchIDs = matchlist.getMatchIds()

        localMatches = []
        for matchID in matchIDs:
            if matchID not in localMatches:
                match = Match(matchID, region)
                print(match.getStats())
            break
        break
    break



