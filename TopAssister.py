import requests

url = "https://footballapi.pulselive.com/football/stats/ranked/players/goal_assist"

querystring = {"page":"0","pageSize":"20","compSeasons":"489","comps":"1","compCodeForActivePlayer":"EN_PR","altIds":"true"}

payload = ""
headers = {
    "authority": "footballapi.pulselive.com",
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
   # "if-none-match": "W/"0b15c9b2c9b8f0518112273805b57135a"",
    "origin": "https://www.premierleague.com",
    "referer": "https://www.premierleague.com/",
   'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

#print(response.text)
data_assister = response.json()

top_assister_data = data_assister["stats"]["content"][0]["owner"]["name"]["display"]

amount_of_assists = data_assister["stats"]["content"][0]["value"]

top_assisters_team = data_assister["stats"]["content"][0]["owner"]["currentTeam"]["name"]

