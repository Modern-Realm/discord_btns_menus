import discord
from typing import *
from datetime import datetime
import asyncio
from discord import utils, ui, ButtonStyle
from discord.components import SelectOption, Button

MISSING = utils.MISSING
DEFAULT_TIMEOUT: float = 180.0


class StructureOfButton(Button):
    def __init__(self,
                 *,
                 label: str,
                 custom_id: Optional[str] = None,
                 disabled: bool = False,
                 style: ButtonStyle = ButtonStyle.primary,
                 url: Optional[str] = None,
                 emoji: Optional[Union[str, discord.Emoji, discord.PartialEmoji]] = None,
                 row: Optional[int] = None,
                 response: Optional[Union[str, discord.Embed]] = None,
                 rewrite: bool = False,
                 ephemeral: bool = False,
                 delete_msg: bool = False,
                 hidden: bool = False,
                 author: discord.Member = None,
                 verify_: bool = True):
        self.kwargs = {
            "author": author,
            "label": label,
            "custom_id": custom_id,
            "disabled": disabled,
            "style": style,
            "url": url,
            "emoji": emoji,
            "row": row,
            "response": response,
            "rewrite": rewrite,
            "ephemeral": ephemeral,
            "delete_msg": delete_msg,
            "hidden": hidden,
            "verify": verify_,
            "func": None,
            "coro_func": None
        }

        self.after_: Optional[dict] = None

    def update_one(self, details, option: str):
        if option not in self.kwargs.keys():
            raise ValueError(f"Invalid option `--{option}`")
        else:
            self.kwargs[option] = details

    def update(self, **options):
        for key in options:
            if key not in self.kwargs.keys():
                raise ValueError(f"Invalid option `--{key}`")
            else:
                self.kwargs[key] = options[key]

    @property
    def args(self) -> Dict:
        return self.kwargs

    @property
    def author(self) -> discord.Member:
        return self.kwargs['author']

    @property
    def name(self) -> str:
        return self.kwargs['label']

    @property
    def id(self) -> str:
        return self.kwargs['custom_id']

    @property
    def is_ephemeral(self) -> bool:
        return self.kwargs['ephemeral']

    @property
    def hidden(self) -> bool:
        return self.kwargs['hidden']

    def after_response(self, **options):
        kwargs = {}
        if len(options) >= 1:
            for key in options:
                if key not in self.kwargs.keys():
                    raise ValueError(f"Invalid option `--{key}`")
                else:
                    kwargs.update({key: options[key]})

            self.after_ = kwargs

    async def add_coro_func(self, function, *args):
        self.kwargs['coro_func'] = lambda: function(*args)

    def add_func(self, function, *args):
        self.kwargs['func'] = lambda: function(*args)

    @property
    def after_resp(self) -> Optional[Dict]:
        return self.after_


SButton = StructureOfButton


class Btn(ui.Button):
    def __init__(self, root: ClassVar, button: SButton):
        self.root = root
        self.btn = button
        self.btn_args = self.btn.args

        super().__init__(
            label=self.btn_args['label'], custom_id=self.btn_args['custom_id'],
            disabled=self.btn_args['disabled'],
            style=self.btn_args['style'], url=self.btn_args['url'], emoji=self.btn_args['emoji'],
            row=self.btn_args['row']
        )

    async def callback(self, interaction):
        checked = check_for_Invoker(self.btn, interaction)
        if checked:
            if self.btn_args['response'] is None:
                resp = f"Button ' {self.btn.name} ' has been clicked !"
            else:
                resp = self.btn_args['response']

            if self.btn.after_resp is not None:
                for key in self.btn.after_resp:
                    self.btn.update_one(self.btn.after_resp[key], key)

            if self.btn_args['delete_msg']:
                return await interaction.message.delete()

            if self.btn_args['coro_func'] is not None:
                func = self.btn_args['coro_func']
                await func()

            if self.btn_args['func'] is not None:
                func = self.btn_args['func']
                func()

            emph_ = self.btn.is_ephemeral
            btn_ = self.root()
            view_ = btn_.view()
            if self.btn_args['rewrite']:
                if is_embed(resp):
                    await interaction.message.edit(content="", embed=resp, view=view_)
                else:
                    await interaction.message.edit(content=resp, embed=None, view=view_)
            else:
                await interaction.message.edit(view=view_)
                if is_embed(resp):
                    await interaction.response.send_message(content="", embed=resp, ephemeral=emph_)
                else:
                    await interaction.response.send_message(content=resp, ephemeral=emph_)


class StructureOfDropMenu:
    def __init__(self, *,
                 custom_id: str = MISSING,
                 placeholder: Optional[str] = None,
                 min_values: int = 1,
                 max_values: int = 1,
                 options: List[SelectOption] = None,
                 disabled: bool = False,
                 row: Optional[int] = None,
                 response: Optional[Union[str, discord.Embed]] = None,
                 rewrite: bool = False,
                 ephemeral: bool = False,
                 hidden: bool = False,
                 author: discord.Member = None,
                 verify_: bool = True
                 ):

        if options is None:
            raise ValueError(
                "Invalid Form Body\nIn builds.1.builds.0.options: This field is required `--options`")

        self.kwargs = {
            "author": author,
            "custom_id": custom_id,
            "placeholder": placeholder,
            "min_values": min_values,
            "max_values": max_values,
            "options": options,
            "disabled": disabled,
            "row": row,
            "response": response,
            "rewrite": rewrite,
            "ephemeral": ephemeral,
            "hidden": hidden,
            "verify": verify_,
            "queries": [],
            "func": None,
            "coro_func": None
        }

        self.after_: Optional[dict] = None
        self.selected_values: Optional[str, List] = None

    def update_one(self, details, option: str):
        if option not in self.kwargs.keys():
            raise ValueError(f"Invalid option `--{option}`")
        else:
            self.kwargs[option] = details

    def update(self, **options):
        for key in options:
            if key not in self.kwargs.keys():
                raise ValueError(f"Invalid option `--{key}`")
            else:
                self.kwargs[key] = options[key]

    @property
    def args(self) -> Dict:
        return self.kwargs

    @property
    def author(self) -> Optional[discord.Member]:
        return self.kwargs['author']

    @property
    def name(self) -> Optional[str]:
        return self.kwargs['label']

    @property
    def id(self) -> str:
        return self.kwargs['custom_id']

    @property
    def is_ephemeral(self) -> bool:
        return self.kwargs['ephemeral']

    @property
    def hidden(self) -> bool:
        return self.kwargs['hidden']

    @property
    def queries(self) -> List:
        return self.kwargs['queries']

    def after_response(self, **options):
        kwargs = {}
        if len(options) >= 1:
            for key in options:
                if key not in self.kwargs.keys():
                    raise ValueError(f"Invalid option `--{key}`")
                else:
                    kwargs.update({key: options[key]})

            self.after_ = kwargs

    @property
    def after_resp(self) -> Optional[Dict]:
        return self.after_

    async def add_coro_func(self, function, *args):
        self.kwargs['coro_func'] = lambda: function(*args)

    def add_func(self, function, *args):
        self.kwargs['func'] = lambda: function(*args)

    def add_query(self, *query: Tuple[str, Union[str, discord.Embed]]):
        for query in query:
            queries_: list = self.kwargs['queries']
            queries_.append(query)

    def add_queries(self, *queries: Tuple[List[str], Union[str, discord.Embed]]):
        for query_ in queries:
            queries_: list = self.kwargs['queries']
            queries_.append(query_)

    @staticmethod
    def convert_resp(content: str, values: list):
        count = 1
        max_count = len(values) + 5
        while (count <= max_count):
            if "{values}" in content:
                try:
                    content = content.replace("{values}", ", ".join(values))
                except ValueError:
                    raise ValueError("Format key not Found\nTry this formatters: `{values}`, `{{values[index]}}`")
            elif "{{values[" in content:
                try:
                    x = content.index("{{")
                    y = content.index("}}")

                    index: int = int(content[content.index("[") + 1: content.index("]")])
                    content = content.replace(f"{content[x: y + 2]}", values[index])
                except ValueError:
                    raise ValueError("Format key not Found\nTry this formatters: `{values}`, `{{values[index]}}`")
                except IndexError:
                    raise IndexError(f"list index out of range (len(values) = {len(values)})")
            count += 1

        return content


SDropMenu = StructureOfDropMenu


class Menu(ui.Select):
    def __init__(self, root: ClassVar, menu: SDropMenu):
        self.root = root
        self.menu = menu
        self.menu_args = menu.args
        super().__init__(
            custom_id=self.menu_args['custom_id'], placeholder=self.menu_args['placeholder'],
            min_values=self.menu_args['min_values'], max_values=self.menu_args['max_values'],
            options=self.menu_args['options'], disabled=self.menu_args['disabled'], row=self.menu_args['row']
        )

    def query_conditions(self, queries) -> Union[str, discord.Embed, None]:
        values_ = self.values
        for val, response_ in queries:
            if isinstance(val, list):
                if sorted(val) == sorted(values_):
                    return response_
            else:
                for value_ in values_:
                    if val == value_:
                        return response_

        return None

    async def callback(self, interaction):
        checked = check_for_Invoker(self.menu, interaction)

        if checked:
            self.menu.selected_values = self.values

            if self.menu_args['response'] is None:
                resp = SDropMenu.convert_resp("Options: ' {values} ' has been selected !", self.values)
            else:
                resp = self.menu_args['response']

            if self.menu.after_resp is not None:
                for key in self.menu.after_resp:
                    self.menu.update_one(self.menu.after_resp[key], key)

            if len(self.menu.queries) >= 1:
                get_queries = self.query_conditions(self.menu.queries)
            else:
                get_queries = None

            emph_ = self.menu.is_ephemeral

            if self.menu_args['coro_func'] is not None:
                func = self.menu_args['coro_func']
                await func()

            if self.menu_args['func'] is not None:
                func = self.menu_args['func']
                func()

            if get_queries is not None:
                resp_ = get_queries
            else:
                resp_ = None

            menu_ = self.root()
            view_ = menu_.view()

            if self.menu_args['rewrite']:
                if resp_ is not None:
                    if is_embed(resp_):
                        resp_.description = SDropMenu.convert_resp(resp_.description, self.values)
                        await interaction.message.edit(content=' ', embed=resp_, view=view_)
                    else:
                        resp_ = SDropMenu.convert_resp(resp_, self.values)
                        await interaction.message.edit(content=resp_, embed=None, view=view_)
                else:
                    if is_embed(resp):
                        resp.description = SDropMenu.convert_resp(resp.description, self.values)
                        await interaction.message.edit(content=' ', embed=resp, view=view_)
                    else:
                        resp = SDropMenu.convert_resp(resp, self.values)
                        await interaction.message.edit(content=resp, embed=None, view=view_)
            else:
                await interaction.message.edit(view=view_)
                if resp_ is not None:
                    if is_embed(resp_):
                        resp_.description = SDropMenu.convert_resp(resp_.description, self.values)
                        await interaction.response.send_message(embed=resp_)
                    else:
                        resp_ = SDropMenu.convert_resp(resp_, self.values)
                        await interaction.response.send_message(content=resp_)
                else:
                    if is_embed(resp):
                        resp.description = SDropMenu.convert_resp(resp.description, self.values)
                        await interaction.response.send_message(content=' ', embed=resp, ephemeral=emph_)
                    else:
                        resp = SDropMenu.convert_resp(resp, self.values)
                        await interaction.response.send_message(content=resp, ephemeral=emph_)


def is_embed(response):
    if isinstance(response, discord.Embed):
        return True
    else:
        return False


def check_for_Invoker(component: Union[SButton, SDropMenu], interaction) -> bool:
    args_ = component.args
    type_ = args_['verify']
    if type_:
        if interaction.user == component.author:
            return True
        else:
            return False
    else:
        return True


def embed(context: str, color=0xffff00, timestamp: bool = False) -> discord.Embed:
    present_time = datetime.utcnow() if timestamp else None
    em = discord.Embed(description=context, color=discord.Color(color), timestamp=present_time)
    return em


def rich_embed(_title: str, description: str, color=0xffff00, timestamp: bool = False) -> discord.Embed:
    present_time = datetime.utcnow() if timestamp else None
    em = discord.Embed(title=_title, description=description, color=discord.Color(color), timestamp=present_time)
    return em

# This codes can also be usable ....

# async def call_coro_function(function, *args, **kwargs):
#     return await function(*args, **kwargs)
#

# def call_function(function, *args, **kwargs):
#     return function(*args, **kwargs)
