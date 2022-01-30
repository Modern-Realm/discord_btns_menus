from btns_menus.Combinations import *

import discord
from discord import ButtonStyle, SelectOption


def SOption(*, name: str, embed_: discord.Embed, description: str = None,
            emoji: Union[str, discord.Emoji, discord.PartialEmoji] = None
            ) -> Dict:
    """It's a decorator used to overwrite options in discord.ui.Select

    :param name: label for option
    :param embed_: If option is selected, the embed will be sent !
    :param description: Description for the option
    :param emoji: Emoji for the option

    :returns: Dict
    """
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
                 footer: str = None,
                 timeout: Optional[float] = DEFAULT_TIMEOUT
                 ):
        """
        Paginator is used to show users the given embeds in pages format using **navigation Buttons and DropMenus**

        :param author: User who will interact with the Paginator
        :param embeds: The list of embeds that acts as Pages
        :param commands_list: The list of options which are shown as options in a Drop Menu
        :param buttons: List of buttons used to navigate of interact with the pages/embeds
        :param menus: List of Menus used to make a user select options from it
        :param footer: Used to add content into text in footer of discord.Embed
        :param timeout: Timeout of the interaction

        :returns: view: discord.ui.View
        """

        self.author = author
        self.embeds = embeds
        self.cmds_list = commands_list
        self.buttons = [] if buttons is None else buttons
        self.menus = [] if menus is None else menus
        self.timeout = timeout

        self.pages: int = 0

        def footer_for_PG(content: str = None) -> Optional[str]:
            if content is not None:
                conv_content = content.replace("{user}", str(self.author))
                conv_content = conv_content.replace("{username}", self.author.display_name)
                conv_content = conv_content.replace("{pg}", str(self.pages + 1))
                conv_content = conv_content.replace("{total_pgs}", str(len(self.embeds)))
                conv_content = conv_content.replace("{guild}", self.author.guild.name)

                return conv_content
            else:
                return None

        self.footer_for_PG = footer_for_PG
        self.footer = footer

        self.index_for_home = 0
        self.index_for_forward = 1
        self.index_for_backward = 2
        self.index_for_delete = 3
        self.index_for_cmds = 0

        self.home_btn: Optional[SButton] = None
        self.forward_btn: Optional[SButton] = None
        self.backward_btn: Optional[SButton] = None
        self.delete_menu: Optional[SButton] = None
        self.cmds_menu: Optional[SDropMenu] = None

        self.create_pages()

    def create_pages(self):
        buttons_ = []
        for button_ in self.buttons:
            if button_.id is not None:
                if button_.id.lower() == "home":
                    self.home_btn = button_
                    self.index_for_home = self.buttons.index(button_)
                    buttons_.append(button_)
                if button_.id.lower() == "forward":
                    self.forward_btn = button_
                    self.index_for_forward = self.buttons.index(button_)
                    buttons_.append(button_)
                if button_.id.lower() == "backward":
                    self.backward_btn = button_
                    self.index_for_backward = self.buttons.index(button_)
                    buttons_.append(button_)
                if button_.id.lower() == "delete":
                    self.delete_menu = button_
                    self.index_for_delete = self.buttons.index(button_)
                    buttons_.append(button_)

        for btn in buttons_:
            self.buttons.remove(btn)

        for menu_ in self.menus:
            if menu_.id is not None:
                if menu_.id.lower() in ["commands-list", "cmds-list"]:
                    self.cmds_menu = menu_
                    self.index_for_cmds = self.menus.index(menu_)
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

        if self.home_btn.kwargs['response'] is None:
            em = self.embeds[0]
            if len(em.footer.text) == 0 and self.footer is not None:
                em.set_footer(text=self.footer_for_PG(self.footer))
            self.home_btn.update(response=em, rewrite=True)

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

            em = self.embeds[self.pages]
            if len(em.footer.text) == 0 and self.footer is not None:
                em.set_footer(text=self.footer_for_PG(self.footer))
            self.forward_btn.update_one(em, "response")

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

            em = self.embeds[self.pages]
            if len(em.footer.text) == 0 and self.footer is not None:
                em.set_footer(text=self.footer_for_PG(self.footer))
            self.backward_btn.update_one(em, "response")

        if self.cmds_list is not None:
            options = []
            for option in self.cmds_list:
                opt_ = SelectOption(
                    label=option['name'], description=option['description'], emoji=option['emoji'])
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

            self.menus.insert(self.index_for_cmds, self.cmds_menu)

        if self.home_btn.kwargs['func'] is None and self.home_btn.kwargs['coro_func'] is None:
            self.home_btn.add_func(home_page)
        if self.forward_btn.kwargs['func'] is None and self.forward_btn.kwargs['coro_func'] is None:
            self.forward_btn.add_func(forward_pages)
        if self.backward_btn.kwargs['func'] is None and self.backward_btn.kwargs['coro_func'] is None:
            self.backward_btn.add_func(backward_pages)

        created_btns = [self.home_btn, self.forward_btn,
                        self.backward_btn, self.delete_menu]
        stored_indexes = [self.index_for_home, self.index_for_forward,
                          self.index_for_backward, self.index_for_delete]
        for x in range(len(created_btns)):
            self.buttons.insert(stored_indexes[x], created_btns[x])

    def view(self) -> ui.View:
        """:returns: discord.ui.View"""

        view_ = MultiBtnAndMenu(self.author, self.buttons,
                                self.menus, timeout=self.timeout).view()
        return view_
