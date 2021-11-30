# Package Name: <a href='https://pypi.org/project/pycord-btns-menus/'> pycord-btns-menus </a>

#### A responsive package for Buttons, DropMenus and Combinations

##### • This module makes the process a lot easier !

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Generic badge](https://img.shields.io/badge/Python-3.6-blue.svg)](https://shields.io/)
[![GitHub license](https://badgen.net/github/license/Naereen/Strapdown.js)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)
[![Windows](https://svgshare.com/i/ZhY.svg)](https://svgshare.com/i/ZhY.svg)

### Join [Support Server](https://discord.gg/GVMWx5EaAN) for more guidance !

<hr/>

# Features:

<hr/>

### 1. Buttons

### 2. DropMenus

### 3. Combinations (Usage of both Buttons & DropMenus)

<hr/>

# Installation

Python 3.6 or higher is required !

```shell
# Linux/macOS
  python3 -m pip install -U pycord-btns-menus

# Windows
  # Method-1:
    py -3 -m pip install -U pycord-btns-menus
  # Method-2:
    pip install pycord-btns-menus
```

<p style="font-weight: bold;"><span style="color: red;">Note: </span>
Make sure to install <a href="https://pypi.org/project/py-cord/">
<u> py-cord</u></a> package
</p>

<hr/>

# Upgrading Package/ Module

```shell
# Linux/macOS
  python3 -m pip uninstall pycord-btns-menus -y
  python3 -m pip install pycord-btns-menus

# Windows
  # Method-1:
    py -3 -m pip uninstall pycord-btns-menus -y
    py -3 -m pip install pycord-btns-menus
  # Method-2:
    pip uninstall pycord-btns-menus -y
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
from btns_menus.DropMenu import DropMenu, DuoDropMenu, BtnAndDropMenu
# with this you can import specific DropMenus
# or
from btns_menus.DropMenu import *
# with this you can import all types of DropMenus and Combinations
```

<hr/>

# Sample Usage

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

# Example for <u>Buttons</u>:

Button type
<a href="https://github.com/skrphenix/pycord_btns_menus/blob/main/btns_menus/Buttons.py">
**DuoButton** </a> , for more samples go
to <a href="https://github.com/skrphenix/pycord_btns_menus/blob/main/Examples/buttons.py">
Examples/Buttons</a>

```python
@client.command()
async def test(ctx):
    user: discord.Member = ctx.author
    btn1 = SButton(label="Wave 👋", response=f"Hello {user.mention} have a nice day !")
    btn2 = SButton(label="Bye", response=f"Bye {user.mention} see you later !", style=ButtonStyle.secondary)
    view_ = DuoButton(user, btn1, btn2).view()

    await ctx.send(f"Sample buttons ...", view=view_)
```

### Preview:

<p align="center">
    <img src="https://github.com/skrphenix/pycord_btns_menus/blob/main/media/bin/sample_buttons.gif" 
    alt="Button-Samples.gif" height="400" width="300">
</p>

<hr/>

# Examples for <u>DropMenus</u>:

DropMenu type
<a href="https://github.com/skrphenix/pycord_btns_menus/blob/main/btns_menus/DropMenu.py">
**DuoDropMenu** </a>, for more samples go
to <a href="https://github.com/skrphenix/pycord_btns_menus/blob/main/Examples/drop_menus.py">
Examples/DropMenus</a>

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

### Preview:

<p align="center">
    <img src="https://github.com/skrphenix/pycord_btns_menus/blob/main/media/bin/sample_dropmenus.gif"
    alt="DropMenu-Samples.gif" height="400" width="300">
</p>

<hr/>

# Buttons & DropMenus combination [![Generic badge](https://img.shields.io/badge/STATUS-BETA-lime.svg)](https://shields.io/)

##### • In this feature you can make & send Buttons and DropMenus together

##### • For more examples for mixture of btns & menus go to <u><a href="https://github.com/skrphenix/pycord_btns_menus/blob/main/Examples/combinations.py">Examples/combinations</a></u>

<br/>

## Examples for <u>combinations</u>

Usage of both Buttons and DropMenus at once ...

```python
@client.command()
async def test(ctx):
    user: discord.Member = ctx.author

    btn1 = SButton(label="Delete Menu", style=ButtonStyle.danger, delete_msg=True)
    menu1 = SDropMenu(placeholder="Select one", options=[
        SelectOption(label="About Python", value="python")
    ])
    menu1.add_query(("python", "Python is a widely-used, interpreted, object-oriented and"
                               " high-level programming language with dynamic semantics, used for general-purpose programming.\n"
                               "It was created by Guido van Rossum, and first released on February 20, 1991."))

    view_ = BtnAndDropMenu(user, btn1, menu1).view()

    await ctx.send(f"Sample buttons & Menus combinations ...", view=view_)
```

### Preview:

<p align="center">
    <img src="https://github.com/skrphenix/pycord_btns_menus/blob/main/media/bin/sample_combinations.gif"
    alt="Sample-Combinations.gif" height="400" width="300">
</p>

<hr/>

# Example for <u>MultiButtons</u>

Button type
<a href="https://github.com/skrphenix/pycord_btns_menus/blob/main/btns_menus/Buttons.py">
**MultiButton** </a> , for more samples go
to <a href="https://github.com/skrphenix/pycord_btns_menus/blob/main/btns_menus/Buttons.py">
Examples/Buttons</a>

The Process for <a href="https://github.com/skrphenix/pycord_btns_menus/blob/main/btns_menus/DropMenu.py">
**MultiDropMenu**</a> will be the same ...

```python
@client.command()
async def test(ctx):
    user: discord.Member = ctx.author
    user_avatar = user.display_avatar or user.default_avatar

    btn1 = SButton(label="username", style=ButtonStyle.primary, response=user.name)
    btn2 = SButton(label="discriminator", style=ButtonStyle.secondary, response=user.discriminator)
    btn4 = SButton(label="Avatar", style=ButtonStyle.secondary, response=str(user_avatar), ephemeral=True)
    btn3 = SButton(label="Server Name", style=ButtonStyle.secondary, response=user.guild.name)
    btn5 = SButton(label="Display Name", style=ButtonStyle.secondary, response=user.display_name)
    btn6 = SButton(label="Delete Menu", style=ButtonStyle.danger, delete_msg=True)

    buttons = [btn1, btn2, btn3, btn4, btn5, btn6]

    view_ = MultiButton(user, buttons).view()

    await ctx.send(f"Sample Usage of Multi Buttons ...", view=view_)
```

### Preview:

<p align="center">
    <img src=""
    alt="Sample-Combinations.gif" height="400" width="300">
</p>

<hr/>
