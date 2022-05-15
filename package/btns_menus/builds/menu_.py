from btns_menus.builds.abc import *
from btns_menus.errors import ButtonException

import discord
from typing import *
from discord import ui
from discord.components import SelectOption


class SDropMenu:
    def __init__(self, *,
                 custom_id: str = None,
                 placeholder: Optional[str] = None,
                 min_values: int = 1,
                 max_values: int = 1,
                 options: List[SelectOption] = None,
                 disabled: bool = False,
                 row: Optional[int] = None,
                 content: Optional[str] = None,
                 response: Optional[Union[str, discord.Embed]] = None,
                 rewrite: bool = False,
                 ephemeral: bool = False,
                 hidden: bool = False,
                 author: discord.Member = None,
                 verify: bool = True
                 ):
        """
        It is a decorator used to create a **DropMenu** overwriting ui.Select

        :param custom_id: Unique ID of the Button
        :param placeholder: A short placeholder for DropMenu
        :param min_values: Limiting the user to select atleast minimum options in DropMenu
        :param max_values: Limiting the user to select atmost maximum options in DropMenu
        :param options: Options which are shown in DropMenu and can be selected by interacted user
        :param disabled: It is used to enable/disable the DropMenu, i.e. Preventing user from using it
        :param row: Places the DropMenu in given Row
        :param content: content of the message
        :param response: Sends the message (str, embed) in user channel
        :param rewrite: It is used to send the message by editing the original message rather than sending a new one
        :param ephemeral: It is used to send the message where it's only visible to interacted user or to all
        :param hidden:  It hides the Button from View
        :param author: Interaction User
        :param verify: It is used to make the func to check for author parameter or not

        :returns: DropMenu
        """

        if response is None:
            if content is not None:
                response = content
                content = None

        self.kwargs = {
            "author": author,
            "custom_id": custom_id,
            "placeholder": placeholder,
            "min_values": min_values,
            "max_values": max_values,
            "options": options,
            "disabled": disabled,
            "row": row,
            "content": content,
            "response": response,
            "rewrite": rewrite,
            "ephemeral": ephemeral,
            "hidden": hidden,
            "verify": verify,
            "queries": [],
            "func": None,
            "coro_func": None,
            "predicate": None
        }

        self.after_: Optional[dict] = None
        self.selected_values: Optional[Union[str, List]] = None
        self.interaction: Optional[discord.Interaction] = None

    def update_one(self, details, option: str):
        if option not in self.kwargs.keys():
            raise ButtonException(f"Invalid option `--{option}`")
        else:
            self.kwargs[option] = details

    def update(self, **options):
        for key in options:
            if key not in self.kwargs.keys():
                raise ButtonException(f"Invalid option `--{key}`")
            else:
                self.kwargs[key] = options[key]

    @property
    def args(self) -> Dict:
        """
        It's a property used to get kwargs of the DropMenu

        - Aliases: ['args', 'kwargs']

        :returns: Dict
        """

        return self.kwargs

    @property
    def author(self) -> Optional[discord.Member]:
        """
        It's a property used to get author of the DropMenu

        :returns: user: discord.Member (or) None
        """

        return self.kwargs['author']

    @property
    def placeholder(self) -> Optional[str]:
        """
        It's a property used to get placeholder of the DropMenu

        :returns:
        """

        return self.kwargs['placeholder']

    @property
    def id(self) -> Optional[str]:
        """
        It's a property used to get ID of the DropMenu

        :returns: custom_id: str (or) None
        """

        return self.kwargs['custom_id']

    @property
    def is_ephemeral(self) -> bool:
        """
        It's a property used to check whether it's ephemeral or not

        :returns: ephemeral: bool , i.e [True, False]
        """

        return self.kwargs['ephemeral']

    @property
    def hidden(self) -> bool:
        """
        It's a property used to get hidden parm of the DropMenu

        :returns: hidden: bool, i.e [True, False]
        """
        return self.kwargs['hidden']

    @property
    def queries(self) -> Optional[List]:
        """
        It's a property used to get all queries of the DropMenu

        :returns: queries: List (or) None
        """

        return self.kwargs['queries']

    def after_response(self, **options):
        """
        It's an event type function which changes the provided options after option (on-select) of the DropMenu

        :param options: takes variables
        :returns: None
        """

        kwargs = {}
        if len(options) >= 1:
            for key in options:
                if key not in self.kwargs.keys():
                    raise ButtonException(f"Invalid option `--{key}`")
                else:
                    kwargs.update({key: options[key]})

            self.after_ = kwargs

    @property
    def after_resp(self) -> Optional[Dict]:
        """
        It's a property used to get all options which are to be changed after option (on-select) of the DropMenu

        :returns: Dict (or) None
        """

        return self.after_

    async def add_coro_func(self, function, *args, **kwargs):
        """
        It's an asynchronous function which stores same function type
        and adds the func to DropMenu for execution after getting an option selected

        :param function: takes asynchronous function
        :param args: takes args of the function provided by a user
        :param kwargs: takes kwargs of the function provided by a user
        :returns: None
        """

        self.kwargs['coro_func'] = lambda: function(*args, **kwargs)

    def add_func(self, function, *args, **kwargs):
        """
        It's a function which stores same function type and
        adds the func to DropMenu for execution after getting an option selected

        :param function: takes a function
        :param args: takes args of the function provided by a user
        :param kwargs: takes kwargs of the function provided by a user
        :returns: None
        """

        self.kwargs['func'] = lambda: function(*args, **kwargs)

    def add_query(self, *query: Tuple[str, Union[str, discord.Embed]]):
        """
        It's an event type function used to add queries for the DropMenu

        :param query: takes option-name and response
        :returns: None
        """

        for query in query:
            queries_: list = self.kwargs['queries']
            queries_.append(query)

    def add_queries(self, *queries: Tuple[List[str], Union[str, discord.Embed]]):
        """
        It's an event type function used to add queries for the DropMenu

        :param queries: takes option-name and response
        :returns: None
        """

        for query_ in queries:
            queries_: list = self.kwargs['queries']
            queries_.append(query_)

    @staticmethod
    def convert_resp(content: str, values: list):
        """
        It's not a reusable function

        Used for formatting the provided content with respective values

        :param content: takes content/ message
        :param values: selected values of the DropMenu
        :returns: None
        """

        count = 1
        max_count = len(values) + 5
        while count <= max_count:
            if "{values}" in content:
                try:
                    content = content.replace("{values}", ", ".join(values))
                except ButtonException:
                    raise ButtonException(
                        "Format key not Found\nTry this formatters: `{values}`, `{{values[index]}}`")
            elif "{{values[" in content:
                try:
                    x = content.index("{{")
                    y = content.index("}}")

                    index: int = int(
                        content[content.index("[") + 1: content.index("]")])
                    content = content.replace(
                        f"{content[x: y + 2]}", values[index])
                except ButtonException:
                    raise ButtonException(
                        "Format key not Found\nTry this formatters: `{values}`, `{{values[index]}}`")
                except IndexError:
                    raise IndexError(
                        f"list index out of range (len(values) = {len(values)})")
            count += 1

        return content

    def pred_decorator(self, method: str, cache: Any, /, error_msg: Any = None):
        self.kwargs["predicate"] = {"method": method,
                                    "cache": cache, "error_msg": error_msg}

    def is_owner(self, error_msg: Union[str, discord.Embed] = None):
        """
        It's used to check whether the interaction user is the owner of interaction guild

        :param error_msg: Sends a message to the user (Interaction.User) if the condition not satisfies
        :return: None
        """

        self.pred_decorator("is_owner", None, error_msg=error_msg)

    def has_any_role(self, *roles: Union[int, str], error_msg: Union[str, discord.Embed] = None):
        """
        It's used to check whether the interaction user has any one of the mentioned roles of interaction guild

        :param roles: Takes either ID's or Name's of the roles of interaction guild
        :param error_msg: Sends a message to the user (Interaction.User) if the condition not satisfies
        :return: None
        """

        self.pred_decorator("has_any_role", roles, error_msg=error_msg)

    def has_roles(self, *roles: Union[int, str], error_msg: Union[str, discord.Embed] = None):
        """
        It's used to check whether the interaction user has the mentioned roles of interaction guild

        :param roles: Takes either ID's or Name's of the roles of interaction guild
        :param error_msg: Sends a message to the user (Interaction.User) if the condition not satisfies
        :return: None
        """

        self.pred_decorator("has_roles", roles, error_msg=error_msg)

    def has_permissions(self, *, error_msg: Union[str, discord.Embed] = None, **perms: bool):
        """
        It's used to check whether the interaction user has the mentioned permissions of the interaction guild/ channel

        :param error_msg: Sends a message to the interaction user if the condition not satisfies
        :param perms: Takes the permissions flags (discord.Permissions.VALID_FLAGS)
        :return: None
        """

        self.pred_decorator("has_permissions", perms, error_msg=error_msg)

    def is_author(self, /, error_msg: Union[str, discord.Embed] = None):
        """
        It's used to check whether the interaction user and SButton.author are same or not

        :param error_msg: Sends a message to the interaction user if the condition not satisfies
        :return: None
        """

        self.pred_decorator("is_author", self.author, error_msg=error_msg)

    def is_any_user(self, *users: Union[str, int], error_msg: Union[str, discord.Embed] = None):
        """
        It's used to check whether the interaction user is in mentioned users or not

        :param users: Takes either ID's or Name's of the members of interaction guild
        :param error_msg: Sends a message to the interaction user if the condition not satisfies
        :return: None
        """

        self.pred_decorator("is_any_user", users, error_msg=error_msg)


class Menu(ui.Select):
    def __init__(self, root: Callable, menu: SDropMenu):
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

    async def callback(self, interaction: discord.Interaction):
        self.menu.interaction = interaction
        checked = check_for_Invoker(self.menu, interaction)
        if self.menu_args["predicate"] is not None:
            predicate_cache = self.menu_args["predicate"]
            checked = await predicate_permsChecker(interaction, predicate_cache["method"], predicate_cache["cache"],
                                                   predicate_cache['error_msg'])
        if checked:
            self.menu.selected_values = self.values

            if self.menu_args['coro_func'] is not None:
                func = self.menu_args['coro_func']
                await func()

            if self.menu_args['func'] is not None:
                func = self.menu_args['func']
                func()

            if self.menu_args['response'] is None:
                resp = SDropMenu.convert_resp(
                    "Options: ' {values} ' has been selected !", self.values)
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

            if get_queries is not None:
                resp_ = get_queries
            else:
                resp_ = None

            menu_ = self.root()
            view_ = menu_.view()

            if self.menu_args['rewrite']:
                if resp_ is not None:
                    if is_embed(resp_):
                        resp_.description = SDropMenu.convert_resp(
                            resp_.description, self.values)
                        await interaction.message.edit(content=self.menu_args['content'] or '', embed=resp_, view=view_)
                    else:
                        resp_ = SDropMenu.convert_resp(resp_, self.values)
                        await interaction.message.edit(content=resp_, embed=None, view=view_)
                else:
                    if is_embed(resp):
                        resp.description = SDropMenu.convert_resp(
                            resp.description, self.values)
                        await interaction.message.edit(content=self.menu_args['content'] or '', embed=resp, view=view_)
                    else:
                        resp = SDropMenu.convert_resp(resp, self.values)
                        await interaction.message.edit(content=resp, embed=None, view=view_)
            else:
                await interaction.message.edit(view=view_)
                if resp_ is not None:
                    if is_embed(resp_):
                        resp_.description = SDropMenu.convert_resp(
                            resp_.description, self.values)
                        await interaction.response.send_message(content=self.menu_args['content'], embed=resp_,
                                                                ephemeral=emph_)
                    else:
                        resp_ = SDropMenu.convert_resp(resp_, self.values)
                        await interaction.response.send_message(content=resp_, ephemeral=emph_)
                else:
                    if is_embed(resp):
                        resp.description = SDropMenu.convert_resp(
                            resp.description, self.values)
                        await interaction.response.send_message(content=self.menu_args['content'] or '',
                                                                embed=resp, ephemeral=emph_)
                    else:
                        resp = SDropMenu.convert_resp(resp, self.values)
                        await interaction.response.send_message(content=resp, ephemeral=emph_)
