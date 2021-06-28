import discord
import asyncio

client = discord.Client()

token = "ODU5MDgxMTQ4OTUyODcwOTMz.YNnfqg.e9cCETraR3SbLT-NYWtsFRFfS14"

@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다.')
    game = discord.Game('무한성')
    await client.change_presence(status=discord.Status.online, activity=game)


client.run(token)