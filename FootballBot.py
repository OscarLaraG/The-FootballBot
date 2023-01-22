import discord

import TopScorer
from bs4 import BeautifulSoup
# ^ Imports necessary libraries/packages ^


def Top_Scorer(message):
    # If the message is "?TopScorer"
    #owered_messsage = message.lower()

    if message.content == '?TopScorer':
        player_name = TopScorer.first_player_data
        golden_boot = (f'The Top scorer is: {player_name}' )
        return golden_boot


def run_discord_bot():
    token_ = 'MTA2MDM5ODE2MTMxMjYyNDY5MA.GtO36j.PaL8Iz4Go_O3XcK7rhsbLeV3DptgC1Fm4g0fkg'
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

    client.run(token_)




