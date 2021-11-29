# Package Name: pycord-btns-menus

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Generic badge](https://img.shields.io/badge/Python-3.6-<COLOR>.svg)](https://shields.io/)
[![PyPi license](https://badgen.net/pypi/license/pip/)](https://pypi.com/project/pip/)

# Features:

<hr>

### 1. Buttons (ui.Button)

### 2. DropMenus (ui.Select)

### 3. Combined usage of Buttons & DropMenus

<hr>

# Sample Usage

Create a file with '.py ' extension, Like: <u> main.py </u>

```python
from btns_menus.Buttons import *
from btns_menus.DropMenu import *

import discord
from discord.ext import commands

intents = discord.Intents.all()

client = commands.Bot(command_prefix="&", intents=intents)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("&help - phoenix"))
    print("Bot is Ready !")


@client.command()
async def test(ctx):
    user = ctx.author

    btn1 = SButton(label="Hello")
    btn2 = SButton(label="Bye")

    view_ = DuoButton(user, btn1, btn2).view()
    await ctx.send("click here !", view=view_)


if __name__ == "__main__":
    client.run('token')

```

# Example for <u>Buttons</u>:

