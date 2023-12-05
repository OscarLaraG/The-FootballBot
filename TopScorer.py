import requests



# We will be using data from the LIVE OFFICIAL premier league site
# get the cURL for our specific section, run it through Postman or Insomnia.


url = "https://footballapi.pulselive.com/football/stats/ranked/players/goals?page=0&pageSize=20&compSeasons=489&comps=1&compCodeForActivePlayer=EN_PR&altIds=true"

payload={}
headers = {
  'authority': 'footballapi.pulselive.com',
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  #'if-none-match': 'W/"0241f65ccf2d5601e7930a7a79731d4e8"',
  'origin': 'https://www.premierleague.com',
  'referer': 'https://www.premierleague.com/',
  'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'cross-site',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
response = requests.request("GET", url, headers=headers, data=payload)

#print(response.text)

data = response.json() #View this in a JSON Formatter to see all the data cleanly


#Stores the top scorer, following the JSON format
first_player_data = data["stats"]["content"][0]["owner"]["name"]["display"]

#Stores the amount of Goals he has scored.
amount_of_goals = data["stats"]["content"][0]["value"]

#Stores the team for the highest scorer 
top_scorers_team = data["stats"]["content"][0]["owner"]["currentTeam"]["name"]

