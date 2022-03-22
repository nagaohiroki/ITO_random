import discord
import random
import os
import codecs


intents = discord.Intents.all()
client = discord.Client(intents=intents)


def random_theme(num):
    with codecs.open('theme.txt', 'r', 'cp932') as file:
        lines = file.readlines()
        if len(lines) < num:
            return ''
        card = range(len(lines))
        card = random.sample(card, len(card))
        picks = card[0:num]
        txt = ''
        for pick in picks:
            txt += f'{lines[pick]}'
        return txt


def ito_random(players, card_num):
    card = range(1, 101)
    card = random.sample(card, len(card))
    txt = ''
    i = 0
    for player in players:
        num = card[card_num * i : card_num * (i + 1)]
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
    command = '/ito'
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
    await message.channel.send(random_theme(2) + ito_random(entry_member, num))


client.run(os.environ['ITO_BOT_TOKEN'])
