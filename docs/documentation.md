# Documentation for <u> pycord-btns-menus </u>

[![Generic badge](https://img.shields.io/badge/vLatest-0.1.2-gold.svg)](https://shields.io/)

# Quick Start

## Installation

Python 3.6 or higher is required !

```shell
# Linux/macOS
  python3 -m pip install -U pycord-btns-menus

# Windows
  # Method-1:
    py -3 -m pip install -U pycord-btns-menus
    # or
    python -m pip install -U pycord-btns-menus
  # Method-2:
    pip install pycord-btns-menus
```

<p style="font-weight: bold;"><span style="color: red;">Note: </span>
Make sure to install <a href="https://pypi.org/project/py-cord/">
<u> py-cord</u></a> package
</p>

<hr/>

## Sample Usage

Create a file with '.py ' extension, Like: <u> **main.py** </u>

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

    btn1 = SButton(label="Hello", response="Hello have a nice day !")

    view_ = Button(user, btn1).view()
    await ctx.send("click here !", view=view_)


if __name__ == "__main__":
    client.run('token')

```

<hr/>
