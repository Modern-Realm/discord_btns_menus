from btns_menus.Buttons import SButton, SingleButton, DuoButton, TrioButton
import os
import discord
from discord import utils, ButtonStyle
from discord.ext import commands

intents = discord.Intents.all()

command_prefix = "&"
client = commands.Bot(command_prefix=command_prefix, intents=intents,
                      status=discord.Status.online, activity=discord.Game(f"{command_prefix}help - phoenix"))


@client.command()
async def normal_button(ctx):
    btn = SButton(label='Hello')

    view_ = SingleButton(ctx.author, btn).view()
    await ctx.send("Normal button", view=view_)


@client.command()
async def responsive_button(ctx):
    user = ctx.author
    btn1 = SButton(label="Hello", response=f"Hello {user}, have a nice day !")
    btn2 = SButton(label="Bye", response=f"Bye {user}, see you soon !")

    view_ = DuoButton(user, btn1, btn2).view()
    await ctx.send("Responsive buttons", view=view_)


@client.command()
async def color_buttons(ctx):
    btn1 = SButton(label="A", style=ButtonStyle.primary)
    btn2 = SButton(label="B", style=ButtonStyle.secondary)
    btn3 = SButton(label="C", style=ButtonStyle.green)

    view_ = TrioButton(ctx.author, btn1, btn2, btn3).view()
    await ctx.send("Color Buttons", view=view_)


@client.command()
async def buttons_by_rows(ctx):
    btn1 = SButton(label="1", row=0)
    btn2 = SButton(label="1", row=1)
    btn3 = SButton(label="1", row=2)

    view_ = TrioButton(ctx.author, btn1, btn2, btn3).view()
    await ctx.send("Buttons by rows", view=view_)


@client.command()
async def disable_button(ctx):
    user = ctx.author
    btn1 = SButton(label="Disable Button", disabled=True)
    btn2 = SButton(label="Hello", response=f"Hello {user}")

    view_ = DuoButton(user, btn1, btn2).view()
    await ctx.send("Disable Button", view=view_)


@client.command()
async def onclick_disable_button(ctx):
    user = ctx.author
    btn1 = SButton(label="display name", response=user.display_name)

    btn2 = SButton(label="discriminator", response=user.discriminator)
    btn2.after_response(disabled=True)

    view_ = DuoButton(user, btn1, btn2).view()
    await ctx.send("Click the button to make it disabled", view=view_)


@client.command()
async def hidden_button(ctx):
    user = ctx.author
    btn1 = SButton(label="username", response=user.display_name, hidden=True)
    btn2 = SButton(label="discriminator", response=user.discriminator)

    view_ = DuoButton(user, btn1, btn2).view()
    await ctx.send("Hidden buttons", view=view_)


@client.command()
async def onclick_hide_button(ctx):
    user = ctx.author
    btn1 = SButton(label="display name", response=user.display_name)

    btn2 = SButton(label="discriminator", response=user.discriminator)
    btn2.after_response(hidden=True)

    view_ = DuoButton(user, btn1, btn2).view()
    await ctx.send("Click the button to make it hidden", view=view_)


@client.command()
async def adding_button_func(ctx):
    user = ctx.author
    btn1 = SButton(label="display name", response=user.display_name)
    btn2 = SButton(label="discriminator", response=user.discriminator)

    def hello():
        print(f"{user} has clicked 'discriminator' button !")

    btn2.add_func(hello)
    view_ = DuoButton(user, btn1, btn2).view()
    await ctx.send("adding function to button", view=view_)


@client.command()
async def adding_button_coro_func(ctx):
    user = ctx.author
    btn1 = SButton(label="Verify", response="verified", style=ButtonStyle.green)
    btn2 = SButton(label="Delete Menu", delete_msg=True)

    async def hello():
        await user.send(f"Verification successful in **{ctx.guild.name}** Server")

    await btn2.add_coro_func(hello)
    view_ = DuoButton(user, btn1, btn2).view()
    await ctx.send("adding asynchronous function to button", view=view_)


@client.command()
async def updating_button(ctx):
    user = ctx.author
    btn1 = SButton(label="name", response=user.name)

    def btn1_callback(button1, button2):
        button1.update(disabled=True)
        button2.update(disabled=False)

    btn2 = SButton(label="discriminator", response=user.discriminator)

    def btn2_callback(button1, button2):
        button1.update(disabled=False)
        button2.update(disabled=True)

    btn1.add_func(btn1_callback, btn1, btn2)
    btn2.add_func(btn2_callback, button1=btn1, button2=btn2)

    view_ = DuoButton(user, btn1, btn2).view()
    await ctx.send("Updating buttons using functions", view=view_)


@client.command()
async def reaction_role_button(ctx):
    user = ctx.author
    role = utils.get(ctx.guild.roles, id=ROLE_ID)  # Make sure to mention the ROLE_ID

    reaction_btn = SButton(label="Verify", response="Verified !", ephemeral=True, verify_=False)

    async def give_role():
        await user.add_roles(role)

    await reaction_btn.add_coro_func(give_role)

    view_ = SingleButton(user, reaction_btn, timeout=None).view()
    await ctx.send("Click the below button to get verified !", view=view_)


if __name__ == '__main__':
    client.run(TOKEN)
