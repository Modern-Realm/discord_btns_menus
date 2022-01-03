import discord
from typing import *
from discord import utils

MISSING = utils.MISSING
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
