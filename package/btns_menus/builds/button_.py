from btns_menus.builds.abc import *
from btns_menus.errors import ButtonException

import discord
from typing import *
from discord import ui, ButtonStyle


class SButton:
    def __init__(self,
                 *,
                 label: str = None,
                 custom_id: Optional[str] = None,
                 disabled: bool = False,
                 style: ButtonStyle = ButtonStyle.secondary,
                 url: Optional[str] = None,
                 emoji: Optional[Union[str, discord.Emoji, discord.PartialEmoji]] = None,
                 row: Optional[int] = None,
                 content: Optional[str] = None,
                 response: Optional[Union[str, discord.Embed]] = None,
                 rewrite: bool = False,
                 ephemeral: bool = False,
                 delete_msg: bool = False,
                 hidden: bool = False,
                 author: discord.Member = None,
                 verify: bool = True):
        """
        It is a decorator used to create a **Button** overwriting ui.Button

        :param label: Label of the Button
        :param custom_id: Unique ID of the Button
        :param disabled: It is used to enable/disable the Button, i.e. Preventing user from using it
        :param style: Color of the Button
        :param url: Onclick Redirects to the given url
        :param emoji: Emoji for the Button
        :param row: Places the Button in given Row
        :param content: content of the message
        :param response: Sends the message (str/ embed) in user channel
        :param rewrite: It is used to send the message by editing the original message rather than sending a new one
        :param ephemeral: It is used to send the message where it's only visible to interacted user or to all
        :param delete_msg: Deletes the original message
        :param hidden: It hides the Button from View
        :param author: Interaction User
        :param verify: It is used to make the func to check for author parameter or not

        :returns: Button
        """

        if response is None:
            if content is not None:
                response = content
                content = None

        self.kwargs = {
            "author": author,
            "label": label,
            "custom_id": custom_id,
            "disabled": disabled,
            "style": style,
            "url": url,
            "emoji": emoji,
            "row": row,
            "content": content,
            "response": response,
            "rewrite": rewrite,
            "ephemeral": ephemeral,
            "delete_msg": delete_msg,
            "hidden": hidden,
            "verify": verify,
            "func": None,
            "coro_func": None,
            "predicate": None
        }

        self.after_: Optional[dict] = None
        self.interaction: Optional[discord.Interaction] = None

    def update_one(self, details: Any, option: str):
        """
        Updates the option of the **Button**

        :param details: Takes any datatype for updating
        :param option: The option which should be overwritten

        :returns: None
        """

        if option not in self.kwargs.keys():
            raise ButtonException(f"Invalid option `--{option}`")
        else:
            self.kwargs[option] = details

    def update(self, **options):
        """
        Updates the options of the **Button*

        :param options: takes variables

        :returns: None
        """

        for key in options:
            if key not in self.kwargs.keys():
                raise ButtonException(f"Invalid option `--{key}`")
            else:
                self.kwargs[key] = options[key]

    @property
    def args(self) -> Dict:
        """
        It's a property used to get kwargs of the button

        - Aliases: ['args', 'kwargs']

        :returns: Dict
        """

        return self.kwargs

    @property
    def author(self) -> Optional[discord.Member]:
        """
        It's a property used to get author of the button

        :returns: user: discord.Member (or) None
        """

        return self.kwargs['author']

    @property
    def name(self) -> Optional[str]:
        """
        It's a property used to get label of the button

        :returns: name: str
        """

        return self.kwargs['label'] or self.kwargs['emoji']

    @property
    def id(self) -> Optional[str]:
        """
        It's a property used to get ID of the button

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
        It's a property used to get hidden parm of the button

        :returns: hidden: bool, i.e [True, False]
        """

        return self.kwargs['hidden']

    def after_response(self, **options):
        """
        It's an event type function which changes the provided options after button ( onclick )

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

    async def add_coro_func(self, function, *args, **kwargs):
        """
        It's an asynchronous function which stores same function type
        and adds the func to button for execution after getting clicked

        :param function: takes asynchronous function
        :param args: takes args of the function provided by a user
        :param kwargs: takes kwargs of the function provided by a user
        :returns: None
        """

        self.kwargs['coro_func'] = lambda: function(*args, **kwargs)

    def add_func(self, function, *args, **kwargs):
        """
        It's a function which stores same function type and adds the func to button for execution after getting clicked

        :param function: takes a function
        :param args: takes args of the function provided by a user
        :param kwargs: takes kwargs of the function provided by a user
        :returns: None
        """

        self.kwargs['func'] = lambda: function(*args, **kwargs)

    @property
    def after_resp(self) -> Optional[Dict]:
        """
        It's a property used to get a dictionary of options which are to be changed after button click

        :returns: Dict (or) None
        """

        return self.after_

    def pred_decorator(self, method: str, cache: Any, /, error_msg: Any = None):
        self.kwargs["predicate"] = {"method": method, "cache": cache, "error_msg": error_msg}

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


class Btn(ui.Button):
    def __init__(self, root: Callable, button: SButton):
        self.root = root
        self.btn = button
        self.btn_args = self.btn.args

        super().__init__(
            label=self.btn_args['label'], custom_id=self.btn_args['custom_id'],
            disabled=self.btn_args['disabled'],
            style=self.btn_args['style'], url=self.btn_args['url'], emoji=self.btn_args['emoji'],
            row=self.btn_args['row']
        )

    async def callback(self, interaction: discord.Interaction):
        self.btn.interaction = interaction
        checked = check_for_Invoker(self.btn, interaction)
        if self.btn_args["predicate"] is not None:
            predicate_cache = self.btn_args["predicate"]
            checked = await predicate_permsChecker(interaction, predicate_cache["method"], predicate_cache["cache"],
                                                   predicate_cache['error_msg'])
        if checked:
            if self.btn_args['coro_func'] is not None:
                func = self.btn_args['coro_func']
                await func()

            if self.btn_args['func'] is not None:
                func = self.btn_args['func']
                func()

            if self.btn_args['response'] is None:
                resp = f"Button ' {self.btn.name} ' has been clicked !"
            else:
                resp = self.btn_args['response']

            if self.btn.after_resp is not None:
                for key in self.btn.after_resp:
                    self.btn.update_one(self.btn.after_resp[key], key)

            if self.btn_args['delete_msg']:
                return await interaction.message.delete()

            emph_ = self.btn.is_ephemeral
            btn_ = self.root()
            view_ = btn_.view()
            if self.btn_args['rewrite']:
                if is_embed(resp):
                    await interaction.message.edit(content=self.btn_args['content'] or "", embed=resp, view=view_)
                else:
                    await interaction.message.edit(content=resp, embed=None, view=view_)
            else:
                await interaction.message.edit(view=view_)
                if is_embed(resp):
                    await interaction.response.send_message(content=self.btn_args['content'] or "",
                                                            embed=resp, ephemeral=emph_)
                else:
                    await interaction.response.send_message(content=resp, ephemeral=emph_)
