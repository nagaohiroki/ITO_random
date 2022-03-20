import discord
import random


token = ''
command = '/ito'
intents = discord.Intents.all()
client = discord.Client(intents=intents)


def ito_random(players, card_num):
    card = range(1, 101)
    rand = random.sample(card, len(card))
    txt = ''
    i = 0
    for player in players:
        num = rand[card_num * i : card_num * (i + 1)]
        txt += f'<@{player}> ||{num}||\n'
        i += 1
    return txt


@client.event
async def on_ready():
    print('ITO bot login')


@client.event
async def on_message(message):
    if message.author.bot:
        return
    content = message.content
    if content.startswith(command) == False:
        return
    num = 1
    num_str = content.replace(command, '')
    if num_str != '':
        num = int(num_str)
    entry_member = []
    for member in message.guild.members:
        if member.bot == False and member.status == discord.Status.online:
            entry_member.append(member.id)
    await message.channel.send(ito_random(entry_member, num))


client.run(token)
