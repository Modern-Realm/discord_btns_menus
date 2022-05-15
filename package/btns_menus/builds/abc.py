from btns_menus.errors import MissingPerms, MissingRoles, MissingAdminPerms, MissingAnyRole
from btns_menus.errors import InvalidInteractionUser, NotInUsers

import discord
import threading
import asyncio

from asyncio.coroutines import iscoroutinefunction
from typing import Any, Union, Callable, Optional
from discord import utils

DEFAULT_TIMEOUT: Union[int, float] = 180.0


def is_embed(response: Any) -> bool:
    """
    Checks whether the type of response is str (or) embed

    :param response: takes str (or) embed
    :return: bool, i.e [True, False]
    """
    return isinstance(response, discord.Embed)


def check_for_Invoker(component, interaction: discord.Interaction) -> bool:
    """
    Checks whether the author of the component and interaction are same or not

    :param component: Takes either button: SButton or dropmenu: SDropMenu
    :param interaction: Takes interaction type discord.Interaction
    :return: bool, i.e [True, False]
    """

    args_ = component.args
    type_ = args_['verify']
    if type_:
        if interaction.user == component.author:
            return True
        else:
            return False
    else:
        return True


async def has_permissions(interaction: discord.Interaction, **perms: bool):
    invalid = set(perms) - set(discord.Permissions.VALID_FLAGS)
    if invalid:
        raise TypeError(f"Invalid permission(s): {', '.join(invalid)}")

    async def predicate(user):
        ch = interaction.channel
        permissions = ch.permissions_for(user)
        missing = [perm for perm, value in perms.items() if getattr(permissions, perm) != value]
        if not missing:
            return True, None
        else:
            return False, missing

    return await predicate(interaction.user)


def get_role(guild: discord.Guild, context: Union[str, int]) -> Optional[discord.Role]:
    if isinstance(context, int):
        role = utils.get(guild.roles, id=int(context))
    else:
        role = utils.get(guild.roles, name=str(context))

    return role


def get_user(guild: discord.Guild, context: Union[str, int]) -> Optional[discord.Member]:
    if isinstance(context, int):
        member = utils.get(guild.members, id=int(context))
    else:
        member = utils.get(guild.members, name=str(context))

    return member


async def send_error_msg(interaction: discord.Interaction, error: Union[str, discord.Embed]):
    if is_embed(error):
        try:
            await interaction.response.send_message(embed=error, ephemeral=True)
        except:
            await interaction.followup.send(embed=error, ephemeral=True)
    else:
        try:
            await interaction.response.send_message(content=error, ephemeral=True)
        except:
            await interaction.followup.send(content=error, ephemeral=True)


async def predicate_permsChecker(interaction: discord.Interaction, method: str, context: Any,
                                 error_msg: Union[discord.Embed, str] = None) -> bool:
    user = interaction.user
    guild = user.guild

    if method == "is_owner":
        if user == guild.owner:
            return True
        else:
            if error_msg is None:
                raise MissingAdminPerms()
            else:
                await send_error_msg(interaction, error_msg)
    if method == "has_any_role":
        roles_ = [get_role(guild, role) for role in context]
        tag_ = False
        for gvn_role in roles_:
            if gvn_role in user.roles:
                tag_ = True
                break
        if not tag_:
            if error_msg is None:
                raise MissingAnyRole([role.name for role in roles_])
            else:
                await send_error_msg(interaction, error_msg)
        else:
            return True
    if method == "has_roles":
        roles_ = [get_role(guild, role) for role in context]
        tag_ = True
        for gvn_role in roles_:
            if gvn_role not in user.roles:
                tag_ = False
                break
        if not tag_:
            if error_msg is None:
                raise MissingRoles([role.name for role in roles_])
            else:
                await send_error_msg(interaction, error_msg)
        else:
            return True
    if method == "has_permissions":
        check_, missing_ = await has_permissions(interaction, **context)
        if check_ is True:
            return True
        else:
            if error_msg is None:
                raise MissingPerms(missing_)
            else:
                await send_error_msg(interaction, error_msg)
    if method == "is_author":
        if user == context:
            return True
        else:
            if error_msg is None:
                raise InvalidInteractionUser(context.name)
            else:
                await send_error_msg(interaction, error_msg)
    if method == "is_any_user":
        context = [get_user(guild, user) for user in context]
        if user in context:
            return True
        else:
            if error_msg is None:
                raise NotInUsers([user.name for user in context])
            else:
                await send_error_msg(interaction, error_msg)

    return False


def run_async(target: Callable, *args, **kwargs):
    class RunThread(threading.Thread):
        def __init__(self, func: Callable):
            self.func = func
            self.args = args
            self.kwargs = kwargs
            self.result = None

            super().__init__()

        def run(self):
            if iscoroutinefunction(self.func):
                self.result = asyncio.run(self.func(*self.args, **self.kwargs))
            else:
                self.result = self.func(*self.args, **self.kwargs)

    thread = RunThread(target)
    thread.start()
    thread.join()
    return thread.result
