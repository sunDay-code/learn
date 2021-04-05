RIOT_API_KEY = "RGAPI-27d4deaf-181e-46e1-9128-eb0dc7f1bfd4"

REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                  "89.0.4389.114 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": RIOT_API_KEY,
}

REQUEST_URLS = {
    "match": "https://na1.api.riotgames.com/lol/match/v4/matches/{}",
    "account": "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}",
    "matchList": "https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/{}",
}