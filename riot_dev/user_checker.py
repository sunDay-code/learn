from protocol.predefined_values import *
import requests
import json


class Match:
    def __init__(self, game_id=""):



class Account:
    def __init__(self, summoner_name=""):
        self._id = ""  # This is also {encryptedSummonerId}
        self._accountId = ""  # This is also {encryptedAccountId}
        self._puuid = ""
        self._name = ""
        self._profileIconId = ""
        self._summonerLevel = ""
        self._matches = []
        self.account_inquiry(summoner_name)
        self.match_inquiry()

    def account_inquiry(self, summoner_name=""):
        if len(summoner_name) < 1:
            print("Summoner Name is required!")
            return

        r = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}".format(summoner_name),
                         headers=REQUEST_HEADERS)
        r_json = json.loads(r.text)
        print(r_json)
        self._name = r_json['name']
        self._id = r_json['id']
        self._accountId = r_json['accountId']
        self._profileIconId = r_json['profileIconId']
        self._summonerLevel = r_json['summonerLevel']
        self._puuid = r_json['puuid']

    def match_inquiry(self):
        r = requests.get("https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/{}".format(self._accountId),
                         headers=REQUEST_HEADERS)
        r_json = json.loads(r.text)
        print(r_json)
        self._matches = r_json['matches']

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
    print(account.account_id)


if __name__ == "__main__":
    _main()