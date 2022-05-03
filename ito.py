import discord
import random
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials


intents = discord.Intents.all()
client = discord.Client(intents=intents)


def random_theme_from_spreadsheet():
    scope =['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open("ITO_theme").sheet1
    lists = sheet.get_all_records()
    rand = random.randrange(len(lists))
    card = lists[rand]
    return f"{card['themeA']}\n{card['themeB']}\n"


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
    await message.channel.send(random_theme_from_spreadsheet() + ito_random(entry_member, num))


client.run(os.environ['ITO_BOT_TOKEN'])
