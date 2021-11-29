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

    btn1 = SButton(label="Hello", response="Hello have a nice day !")

    view_ = Button(user, btn1).view()
    await ctx.send("click here !", view=view_)


if __name__ == "__main__":
    client.run('token')

```

<hr/>

# Example for <u>Buttons</u>:

Button type
<a href="https://github.com/skrphenix/pycord_btns_menus/blob/main/btns_menus/Buttons.py">
**DuoButton** </a>

```python
@client.command()
async def test(ctx):
    user: discord.Member = ctx.author
    btn1 = SButton(label="Wave 👋", response=f"Hello {user.mention} have a nice day !")
    btn2 = SButton(label="Bye", response=f"Bye {user.mention} see you later !", style=ButtonStyle.secondary)
    view_ = DuoButton(user, btn1, btn2).view()

    await ctx.send(f"Sample buttons ...", view=view_)
```

<br/>
<p align="center">
    <img src="https://github.com/skrphenix/pycord_btns_menus/blob/main/media/bin/sample_buttons.gif" 
    alt="Button-Samples.gif" height="400" width="300">
</p>

<hr/>

# Examples for <u>DropMenus</u>:

DropMenu type
<a href="https://github.com/skrphenix/pycord_btns_menus/blob/main/btns_menus/DropMenu.py">
**DuoDropMenu** </a>

```python
@client.command()
async def test(ctx):
    user: discord.Member = ctx.author

    menu1 = SDropMenu(placeholder="select one", options=[
        SelectOption(label="username"),
        SelectOption(label="None of the above")
    ])
    menu1.add_query(("username", f"username: {user.name}"))

    menu2 = SDropMenu(placeholder="choose one", options=[
        SelectOption(label="discriminator"),
        SelectOption(label="None of the above")
    ])
    menu2.add_query(("discriminator", f"discriminator: {user.discriminator}"))

    view_ = DuoDropMenu(user, menu1, menu2).view()

    await ctx.send(f"Sample buttons ...", view=view_)
```

<br/>
<p align="center">
    <img src="https://github.com/skrphenix/pycord_btns_menus/blob/main/media/bin/sample_dropmenus.gif"
    alt="DropMenu-Samples.gif" height="400" width="300">
</p>

<hr/>
