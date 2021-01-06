import discord
import os
import requests
import json

client = discord.Client();

def get_quote():
  response = requests.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,racist&type=single")
  json_data = json.loads(response.text)
  joke = json_data["joke"]
  return(joke)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hey there!')

    if message.content.startswith('$joke'):
      quote = get_quote()
      await message.channel.send(quote)

client.run(os.getenv('TOKEN'))