import requests

#Use postman or insomnia, get the request AFTER CURL. generate code in python REQUESTS.

url = "https://footballapi.pulselive.com/football/stats/ranked/players/clean_sheet?page=0&pageSize=10&compSeasons=489&comps=1&compCodeForActivePlayer=EN_PR&positions=GOALKEEPER&altIds=true"

payload = {}
headers = {
  'authority': 'footballapi.pulselive.com',
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'origin': 'https://www.premierleague.com',
  'referer': 'https://www.premierleague.com/',
  'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'cross-site',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

#print(response.text)

data_keeper = response.json()

top_GK_data = data_keeper["stats"]["content"][1]["owner"]["name"]["display"]

amount_of_CS = data_keeper["stats"]["content"][0]["value"]

top_GK_team = data_keeper["stats"]["content"][1]["owner"]["currentTeam"]["name"]
