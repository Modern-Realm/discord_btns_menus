# Package Name: <a href='https://pypi.org/project/pycord-btns-menus/'> pycord-btns-menus </a>

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Generic badge](https://img.shields.io/badge/Python-3.6-blue.svg)](https://shields.io/)
[![GitHub license](https://badgen.net/github/license/Naereen/Strapdown.js)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)
[![Windows](https://svgshare.com/i/ZhY.svg)](https://svgshare.com/i/ZhY.svg)

# Features:

<hr/>

### 1. Buttons (ui.Button)

### 2. DropMenus (ui.Select)

### 3. Combined usage of Buttons & DropMenus

<hr/>

# Installation

```shell
# Linux/macOS
  python3 -m pip install -U pycord-btns-menus

# Windows
    #Method-1:
      py -3 -m pip install -U pycord-btns-menus
    #Method-2:
      pip install pycord-btns-menus
```

<hr/>

# How to import module ?

```python
# For buttons:
from btns_menus.Buttons import Button, DuoButton
# with this you can import specific Buttons
# or
from btns_menus.Buttons import *
# with this you can import all types of buttons

# For DropMenus:
from btns_menus.DropMenu import DropMenu, DuoDropMenu
# with this you can import specific DropMenus
# or
from btns_menus.DropMenu import *
# with this you can import all types of DropMenus
```

<hr/>

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

<center>![Buttons-Sample.gif](https://github.com/skrphenix/pycord_btns_menus/blob/main/media/bin/buttons.gif)</center>

<hr/>

# Example for <u>Buttons</u>:
