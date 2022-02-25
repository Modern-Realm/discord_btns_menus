from btns_menus.DropMenus import SDropMenu, SingleDropMenu, DuoDropMenu, TrioDropMenu
import discord
import os

from typing import Optional
from discord import SelectOption
from discord import utils, ButtonStyle
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix="$", intents=intents, status=discord.Status.online)


@client.command()
async def normal_menu(ctx):
    user = ctx.author
    menu = SDropMenu(placeholder="Select any one",
                     options=[
                         SelectOption(label="Hello"),
                         SelectOption(label="Bye")
                     ])

    view_ = SingleDropMenu(user, menu)
    await ctx.send("Normal Menu", view=view_)


@client.command()
async def responsive_menu(ctx):
    user = ctx.author
    menu = SDropMenu(placeholder="Select any one",
                     options=[
                         SelectOption(label="Hello"),
                         SelectOption(label="Bye")
                     ])
    menu.add_query(("Hello", f"{user.mention} hello !"), ("Bye", f"{user.mention} bye !"))

    view_ = SingleDropMenu(user, menu).view()
    await ctx.send("Normal Menu", view=view_)


@client.command()
async def emoji_menu(ctx):
    user = ctx.author

    options = [
        SelectOption(label="Red", emoji="🔴"),
        SelectOption(label="Blue", emoji="🔵"),
        SelectOption(label="Orange", emoji="🟠"),
        SelectOption(label="Yellow", emoji="🟡")
    ]
    menu = SDropMenu(placeholder="Select more than one option", options=options, min_values=2, max_values=len(options))
    menu.add_queries((['Red', 'Orange'], "Selected bright colors: **{values}**"),
                     (['Blue', 'Yellow'], "Selected light colors: **{values}**"))

    view_ = SingleDropMenu(user, menu).view()
    await ctx.send("", view=view_)


@client.command()
async def menus_by_rows(ctx):
    user = ctx.author
    options = [
        SelectOption(label="A"),
        SelectOption(label="B"),
        SelectOption(label="C")
    ]

    menu1 = SDropMenu(placeholder="Menu 1", options=options, row=3)
    menu2 = SDropMenu(placeholder="Menu 2", options=options, row=2)
    menu3 = SDropMenu(placeholder="Menu 3", options=options, row=1)

    view_ = TrioDropMenu(user, menu1, menu2, menu3).view()
    await ctx.send("Menus By Rows", view=view_)


@client.command()
async def disable_menu(ctx):
    user = ctx.author
    options = [
        SelectOption(label="A"),
        SelectOption(label="B"),
        SelectOption(label="C")
    ]
    menu1 = SDropMenu(placeholder="This menu is disabled !", options=options, disabled=True)

    menu2 = SDropMenu(placeholder="Select a option", options=options, response="Selected: {{values[0]}}")
    menu2.after_response(disabled=True)

    view_ = DuoDropMenu(user, menu1, menu2).view()
    await ctx.send("Disable Menus", view=view_)


@client.command()
async def disable_menus(ctx):
    user = ctx.author
    options = [
        SelectOption(label="A"),
        SelectOption(label="B"),
        SelectOption(label="C")
    ]
    menu1 = SDropMenu(placeholder="This menu is disabled !", options=options, disabled=True)

    menu2 = SDropMenu(placeholder="Select a option", options=options, response="Selected: {{values[0]}}")
    menu2.after_response(disabled=True, placeholder="Menu disabled")

    view_ = DuoDropMenu(user, menu1, menu2).view()
    await ctx.send("Disable Menus", view=view_)


@client.command()
async def hidden_menu(ctx):
    user = ctx.author
    options = [
        SelectOption(label="A"),
        SelectOption(label="B"),
        SelectOption(label="C")
    ]
    menu1 = SDropMenu(placeholder="This menu is disabled !", options=options, hidden=True)

    menu2 = SDropMenu(placeholder="Select a option", options=options, response="Selected: {{values[0]}}")
    menu2.after_response(hidden=True)

    view_ = DuoDropMenu(user, menu1, menu2).view()
    await ctx.send("Hidden Menus", view=view_)


@client.command()
async def adding_menu_func(ctx):
    user = ctx.author
    options1 = [
        SelectOption(label="A"),
        SelectOption(label="B")
    ]

    options2 = [
        SelectOption(label="C"),
        SelectOption(label="D")
    ]

    menu1 = SDropMenu(placeholder="Select one option", options=options1)

    def menu_callback(menu: SDropMenu):
        menu.update(options=options2)

    menu1.add_func(menu_callback, menu1)

    view_ = SingleDropMenu(user, menu1).view()
    await ctx.send("Adding function to menu", view=view_)


@client.command()
async def adding_menu_coro_func(ctx):
    user = ctx.author
    options = [
        SelectOption(label="channel"),
        SelectOption(label="guild"),
        SelectOption(label="owner")
    ]

    menu1 = SDropMenu(placeholder="Select one option", options=options)

    async def menu_callback(menu: SDropMenu):
        interaction = menu.interaction
        values = menu.selected_values
        if values[0] == "channel":
            menu.update(response=str(interaction.channel.mention))
        elif values[0] == "guild":
            menu.update(response=str(interaction.guild.name))
        else:
            menu.update(response=str(interaction.guild.owner))

    await menu1.add_coro_func(menu_callback, menu1)
    # await menu1.add_coro_func(menu_callback, menu=menu1)

    view_ = SingleDropMenu(user, menu1).view()
    await ctx.send("Adding asynchronous function to menu", view=view_)


# This is for Alpha Users only ( >=v0.2.3 )
@client.command()
async def reaction_role_menu(ctx):
    user = ctx.author
    role1 = utils.get(ctx.guild.roles, id=ROLE_ID)  # Make sure to mention the ROLE_ID
    role2 = utils.get(ctx.guild.roles, id=ROLE_ID)  # Make sure to mention the ROLE_ID
    role3 = utils.get(ctx.guild.roles, id=ROLE_ID)  # Make sure to mention the ROLE_ID

    options = [
        SelectOption(label="Role-1"),
        SelectOption(label="Role-2"),
        SelectOption(label="Role-3")
    ]

    reaction_menu = SDropMenu(placeholder="Get your roles", options=options, ephemeral=True, verify=False)

    async def give_role():
        interaction = reaction_menu.interaction
        menu_user = interaction.user

        value = reaction_menu.selected_values[0]
        if value == "Role-1":
            role = role1
        elif value == "Role-2":
            role = role2
        else:
            role = role3

        await menu_user.add_roles(role)
        reaction_menu.update(response=f"Added {role.mention} !")

    await reaction_menu.add_coro_func(give_role)

    view_ = SingleDropMenu(user, reaction_menu, timeout=None).view()
    await ctx.send("Click the below menu to get roles !", view=view_)


if __name__ == '__main__':
    client.run(TOKEN)  # Pass the token here
