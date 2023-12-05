import discord

import TopScorer
import TopAssister
import BestKeeper
from bs4 import BeautifulSoup
# ^ Imports necessary libraries/packages ^


def Top_Scorer(message):
    # If the message is "?TopScorer"

    if message.content == '?TopScorer':
        player_name = TopScorer.first_player_data
        goals_scored = TopScorer.amount_of_goals
        curr_team = TopScorer.top_scorers_team
        golden_boot = (f'The Top scorer is: {player_name}, with {goals_scored} goals scored. He plays for {curr_team}.')
        return golden_boot
    

#Function for the assiter.
def Top_Assister(message):

    if message.content == '?TopAssister':
        player_name = TopAssister.top_assister_data
        assists_given = TopAssister.amount_of_assists
        curr_team = TopAssister.top_assisters_team
        golden_assist = (f'The Top assister is: {player_name}, with {assists_given} assists given. He plays for {curr_team}.')
        return golden_assist
    
def Top_Keeper(message):
    if message.content == '?GoldenGlove':
        player_name = BestKeeper.top_GK_data
        CS_Amount = BestKeeper.amount_of_CS
        curr_team = BestKeeper.top_GK_team
        golden_glove = (f'The Goalkeeper with most Clean Sheets is: {player_name}, with {CS_Amount}!. He plays for {curr_team}.')
        return golden_glove

def run_discord_bot():
    token_ = 'MTA2MDM5ODE2MTMxMjYyNDY5MA.Gw7PYS.D3hlxhWD1pTVA1KDRNkeqhkTGkdJhXWNLLVF8k'
    client = discord.Client(intents=discord.Intents.all())

    @client.event
    async def on_ready():
        print('Logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if message.content.startswith('?TopScorer'):
            the_golden_boot = Top_Scorer(message)
            channel = message.channel
            await channel.send(the_golden_boot)

        if message.content.startswith('?TopAssister'):
            the_golden_assist = Top_Assister(message)
            channel = message.channel
            await channel.send(the_golden_assist)
        
        if message.content.startswith('?GoldenGlove'):
            the_golden_glove = Top_Keeper(message)
            channel = message.channel
            await channel.send(the_golden_glove)

    client.run(token_)




