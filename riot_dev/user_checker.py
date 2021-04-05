from protocol.predefined_values import *
import requests
import queue
# import json

maps_json = requests.get("http://static.developer.riotgames.com/docs/lol/maps.json").json()
print(maps_json)


class Match:
    def __init__(self, game_id=-1):
        self._gameId = game_id
        self._platformId = ""
        self._gameDuration = 0
        self._gameMode = ""
        self._map_id = 0
        self.match_inquiry()

    def match_inquiry(self):
        if self._gameId < 0:
            print("Match Id is required!")
            return
        r = requests.get(REQUEST_URLS['match'].format(self._gameId),
                         headers=REQUEST_HEADERS)
        r_json = r.json()
        print(r_json)
        self._platformId = r_json['platformId']
        self._gameDuration = r_json['gameDuration']
        self._gameMode = r_json['gameMode']
        self._map_id = r_json['mapId']

    @property
    def map(self):
        for item in maps_json:
            if item['mapId'] == self._map_id:
                return item['mapName']
        return None


class Account:
    def __init__(self, summoner_name=""):
        self._id = ""  # This is also {encryptedSummonerId}
        self._accountId = ""  # This is also {encryptedAccountId}
        self._puuid = ""
        self._name = summoner_name
        self._profileIconId = ""
        self._summonerLevel = ""
        self._matches = []
        self.account_inquiry()
        self.matches_inquiry()

    def account_inquiry(self):
        if len(self._name) < 1:
            print("Summoner Name is required!")
            return

        r = requests.get(REQUEST_URLS['account'].format(self._name),
                         headers=REQUEST_HEADERS)
        r_json = r.json()
        print("account: ", r_json)
        try:
            self._id = r_json['id']
            self._accountId = r_json['accountId']
            self._profileIconId = r_json['profileIconId']
            self._summonerLevel = r_json['summonerLevel']
            self._puuid = r_json['puuid']
        except Exception as e:
            print("Exception Found: {}".format(e))

    def matches_inquiry(self):
        r = requests.get(REQUEST_URLS['matchList'].format(self._accountId),
                         headers=REQUEST_HEADERS)
        r_json = r.json()
        print(r_json)
        self._matches = r_json['matches']
        print("Matches: ", self._matches)

    @property
    def matches(self):
        return self._matches

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def account_id(self):
        return self._accountId

    @property
    def profile_icon_id(self):
        return self._profileIconId

    @property
    def summoner_level(self):
        return self._summonerLevel

    @property
    def puuid(self):
        return self._puuid


def _main():
    account = Account("II Elaiña II")
    print(account.matches)
    for item in account.matches:
        match = Match(item['gameId'])


if __name__ == "__main__":
    _main()