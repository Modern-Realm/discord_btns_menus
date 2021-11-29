from btns_menus.builds.base.in_build import *

from typing import *
import discord
from discord import ui


class SingleDropMenu:
    def __init__(self, author: discord.Member, drop_menu1: SDropMenu, /, timeout: float = DEFAULT_TIMEOUT):
        self.author = author
        self.timeout = timeout

        self.menu1 = drop_menu1

        if self.menu1.author is None:
            self.menu1.update_one(self.author, "author")

        self.root_ = lambda: SingleDropMenu(self.author, self.menu1, timeout=self.timeout)

    def view(self) -> ui.View:
        view_ = ui.View(timeout=self.timeout)
        view_.add_item(Menu(self.root_, self.menu1))

        return view_


class DuoDropMenu:
    def __init__(self, author: discord.Member, drop_menu1: SDropMenu, drop_menu2: SDropMenu,
                 /, timeout: float = DEFAULT_TIMEOUT):
        self.author = author
        self.timeout = timeout

        self.menu1 = drop_menu1
        self.menu2 = drop_menu2

        if self.menu1.author is None:
            self.menu1.update_one(self.author, "author")
        if self.menu2.author is None:
            self.menu2.update_one(self.author, "author")

        self.root_ = lambda: DuoDropMenu(self.author, self.menu1, self.menu2, timeout=self.timeout)

    def view(self) -> ui.View:
        view_ = ui.View(timeout=self.timeout)
        view_.add_item(Menu(self.root_, self.menu1))
        view_.add_item(Menu(self.root_, self.menu2))

        return view_


class TrioDropMenu:
    def __init__(self, author: discord.Member, drop_menu1: SDropMenu, drop_menu2: SDropMenu, drop_menu3: SDropMenu,
                 /, timeout: float = DEFAULT_TIMEOUT):
        self.author = author
        self.timeout = timeout

        self.menu1 = drop_menu1
        self.menu2 = drop_menu2
        self.menu3 = drop_menu3

        if self.menu1.author is None:
            self.menu1.update_one(self.author, "author")
        if self.menu2.author is None:
            self.menu2.update_one(self.author, "author")
        if self.menu3.author is None:
            self.menu3.update_one(self.author, "author")

        self.root_ = lambda: TrioDropMenu(self.author, self.menu1, self.menu2, self.menu3, timeout=self.timeout)

    def view(self) -> ui.View:
        view_ = ui.View(timeout=self.timeout)
        view_.add_item(Menu(self.root_, self.menu1))
        view_.add_item(Menu(self.root_, self.menu2))
        view_.add_item(Menu(self.root_, self.menu3))

        return view_


class QuartetDropMenu:
    def __init__(self, author: discord.Member, drop_menu1: SDropMenu, drop_menu2: SDropMenu,
                 drop_menu3: SDropMenu, drop_menu4: SDropMenu,
                 /, timeout: float = DEFAULT_TIMEOUT):
        self.author = author
        self.timeout = timeout

        self.menu1 = drop_menu1
        self.menu2 = drop_menu2
        self.menu3 = drop_menu3
        self.menu4 = drop_menu4

        if self.menu1.author is None:
            self.menu1.update_one(self.author, "author")
        if self.menu2.author is None:
            self.menu2.update_one(self.author, "author")
        if self.menu3.author is None:
            self.menu3.update_one(self.author, "author")
        if self.menu4.author is None:
            self.menu4.update_one(self.author, "author")

        self.root_ = lambda: QuartetDropMenu(self.author, self.menu1, self.menu2, self.menu3, self.menu4,
                                             timeout=self.timeout)

    def view(self) -> ui.View:
        view_ = ui.View(timeout=self.timeout)
        view_.add_item(Menu(self.root_, self.menu1))
        view_.add_item(Menu(self.root_, self.menu2))
        view_.add_item(Menu(self.root_, self.menu3))
        view_.add_item(Menu(self.root_, self.menu4))

        return view_


class QuintetDropMenu:
    def __init__(self, author: discord.Member, drop_menu1: SDropMenu, drop_menu2: SDropMenu,
                 drop_menu3: SDropMenu, drop_menu4: SDropMenu, drop_menu5: SDropMenu,
                 /, timeout: float = DEFAULT_TIMEOUT):
        self.author = author
        self.timeout = timeout

        self.menu1 = drop_menu1
        self.menu2 = drop_menu2
        self.menu3 = drop_menu3
        self.menu4 = drop_menu4
        self.menu5 = drop_menu5

        if self.menu1.author is None:
            self.menu1.update_one(self.author, "author")
        if self.menu2.author is None:
            self.menu2.update_one(self.author, "author")
        if self.menu3.author is None:
            self.menu3.update_one(self.author, "author")
        if self.menu4.author is None:
            self.menu4.update_one(self.author, "author")
        if self.menu5.author is None:
            self.menu5.update_one(self.author, "author")

        self.root_ = lambda: QuintetDropMenu(self.author, self.menu1, self.menu2, self.menu3,
                                             self.menu4, self.menu5, timeout=self.timeout)

    def view(self) -> ui.View:
        view_ = ui.View(timeout=self.timeout)
        view_.add_item(Menu(self.root_, self.menu1))
        view_.add_item(Menu(self.root_, self.menu2))
        view_.add_item(Menu(self.root_, self.menu3))
        view_.add_item(Menu(self.root_, self.menu4))
        view_.add_item(Menu(self.root_, self.menu5))

        return view_
