from btns_menus.Buttons import *
from btns_menus.DropMenus import *
from btns_menus.Combinations import *

import discord
from discord import ButtonStyle, SelectOption


def SOption(*, name: str, embed_: discord.Embed, description: str = None,
            emoji: Union[str, discord.Emoji, discord.PartialEmoji] = None
            ) -> Dict:
    decorator_ = {
        "name": name, "description": description, "embed": embed_, "emoji": emoji
    }
    return decorator_


class Paginator:
    def __init__(self,
                 author: discord.Member,
                 embeds: List[discord.Embed],
                 *,
                 commands_list: List[SOption] = None,
                 buttons: List[SButton] = None,
                 menus: List[SDropMenu] = None,
                 timeout: Union[int, float] = DEFAULT_TIMEOUT
                 ):
        self.author = author
        self.embeds = embeds
        self.cmds_list = commands_list
        self.buttons = [] if buttons is None else buttons
        self.menus = [] if menus is None else menus
        self.timeout = timeout

        self.pages: int = 0

        self.home_btn: Optional[SButton] = None
        self.forward_btn: Optional[SButton] = None
        self.backward_btn: Optional[SButton] = None
        self.delete_menu: Optional[SButton] = None
        self.cmds_menu: Optional[SDropMenu] = None

        self.create_pages()

    def create_pages(self):
        for button_ in self.buttons:
            if button_.id is not None:
                if button_.id.lower() == "home":
                    self.home_btn = button_
                    self.buttons.remove(button_)
                if button_.id.lower() == "forward":
                    self.forward_btn = button_
                    self.buttons.remove(button_)
                if button_.id.lower() == "backward":
                    self.backward_btn = button_
                    self.buttons.remove(button_)
                if button_.id.lower() == "delete":
                    self.delete_menu = button_
                    self.buttons.remove(button_)

        for menu_ in self.menus:
            if menu_.id is not None:
                if menu_.id.lower() in ["commands-list", "cmds-list"]:
                    self.cmds_menu = menu_
                    self.menus.remove(menu_)

        self.home_btn = SButton(label="Home", emoji="🏠", response=self.embeds[0], style=ButtonStyle.green,
                                rewrite=True, disabled=True) if self.home_btn is None else self.home_btn
        self.forward_btn = SButton(label='', emoji="⏩", rewrite=True,
                                   style=ButtonStyle.secondary) if self.forward_btn is None else self.forward_btn
        self.backward_btn = SButton(label='', emoji="⏪", style=ButtonStyle.secondary,
                                    rewrite=True) if self.backward_btn is None else self.backward_btn
        self.delete_menu = SButton(label='Delete Menu', emoji="🗑️", style=ButtonStyle.danger,
                                   delete_msg=True) if self.delete_menu is None else self.delete_menu
        self.cmds_menu = SDropMenu(placeholder="Select any one Module",
                                   rewrite=True) if self.cmds_menu is None else self.cmds_menu

        self.build_pages()

    def build_pages(self):
        def home_page():
            self.pages = 0

            self.home_btn.update(disabled=True)
            self.forward_btn.update(disabled=False)
            self.backward_btn.update(disabled=False)

        def forward_pages():
            self.pages += 1
            if self.pages >= len(self.embeds) - 1:
                self.pages = len(self.embeds) - 1
                self.forward_btn.update(disabled=True)

            self.backward_btn.update(disabled=False)
            self.home_btn.update(disabled=False)
            self.forward_btn.update_one(self.embeds[self.pages], "response")

        def backward_pages():
            self.pages -= 1
            if self.pages <= 0:
                self.pages = 0

                self.home_btn.update(disabled=True)
                self.backward_btn.update(disabled=True)
            else:
                self.backward_btn.update(disabled=False)
                self.home_btn.update(disabled=False)

            self.forward_btn.update(disabled=False)
            self.backward_btn.update_one(self.embeds[self.pages], "response")

        if self.cmds_list is not None:
            options = []
            for option in self.cmds_list:
                opt_ = SelectOption(label=option['name'], description=option['description'], emoji=option['emoji'])
                options.append(opt_)

            self.cmds_menu.update(options=options)
            for option in self.cmds_list:
                self.cmds_menu.add_query((option['name'], option['embed']))

            if self.cmds_menu.kwargs['func'] is None and self.cmds_menu.kwargs['coro_func'] is None:
                def reset_view():
                    self.home_btn.update(disabled=False)
                    self.forward_btn.update(disabled=True)
                    self.backward_btn.update(disabled=True)

                self.cmds_menu.add_func(reset_view)

            self.menus.insert(0, self.cmds_menu)

        if self.home_btn.kwargs['func'] is None and self.home_btn.kwargs['coro_func'] is None:
            self.home_btn.add_func(home_page)
        if self.forward_btn.kwargs['func'] is None and self.forward_btn.kwargs['coro_func'] is None:
            self.forward_btn.add_func(forward_pages)
        if self.backward_btn.kwargs['func'] is None and self.backward_btn.kwargs['coro_func'] is None:
            self.backward_btn.add_func(backward_pages)

        created_btns = [self.home_btn, self.forward_btn, self.backward_btn, self.delete_menu]
        for x in range(len(created_btns)):
            self.buttons.insert(x, created_btns[x])

    def view(self) -> ui.View:
        view_ = MultiBtnAndMenu(self.author, self.buttons, self.menus, timeout=self.timeout).view()
        return view_
