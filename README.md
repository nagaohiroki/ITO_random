# ITO_random

this is discord bot.

## Setup

MacOS
```
sudo python3 -m pip install -U "discord.py[voice]"
sudo python3 -m pip install gspread oauth2client
export ITO_BOT_TOKEN=token
```

Windows
```
python -m pip install -U "discord.py[voice]"
python -m pip install gspread oauth2client
SETX /M ITO_BOT_TOKEN "token"
```

## Discrod Setting

https://discordpy.readthedocs.io/ja/latest/discord.html

MyApplications -> SETTINGS/Bot -> Privileged Gateway Intents
enable [PRESENCE INTENT] and [SERVER MEMBERS INTENT]


## Launch


MacOS
```
python3 ito.py
```

Windows
```
python ito.py
```

## Message

a card

```
/ito
```

two cards

```
/ito2
```