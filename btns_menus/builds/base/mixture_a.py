from btns_menus.builds.base.in_build import *

from typing import *
import discord
from discord import ui


class BtnAndDropMenu:
    def __init__(self, author: discord.Member, button1: SButton, menu1: SDropMenu,
                 *, timeout: float = DEFAULT_TIMEOUT):
        self.author = author
        self.timeout = timeout

        self.btn1 = button1
        self.menu1 = menu1

        if self.btn1.author is None:
            self.btn1.update(author=self.author)
        if self.menu1.author is None:
            self.menu1.update(author=self.author)

        self.root_ = lambda: BtnAndDropMenu(self.author, self.btn1, self.menu1, timeout=self.timeout)

    def view(self) -> ui.View:
        view_ = ui.View(timeout=self.timeout)
        view_.add_item(Btn(self.root_, self.btn1))
        view_.add_item(Menu(self.root_, self.menu1))

        return view_


class Btn2AndDropMenu:
    def __init__(self, author: discord.Member, button1: SButton, button2: SButton, menu1: SDropMenu,
                 *, timeout: float = DEFAULT_TIMEOUT):
        self.author = author
        self.timeout = timeout

        self.btn1 = button1
        self.btn2 = button2
        self.menu1 = menu1

        if self.btn1.author is None:
            self.btn1.update(author=self.author)
        if self.btn2.author is None:
            self.btn2.update(author=self.author)
        if self.menu1.author is None:
            self.menu1.update(author=self.author)

        self.root_ = lambda: Btn2AndDropMenu(self.author, self.btn1, self.btn2, self.menu1, timeout=self.timeout)

    def view(self) -> ui.View:
        view_ = ui.View(timeout=self.timeout)
        view_.add_item(Btn(self.root_, self.btn1))
        view_.add_item(Btn(self.root_, self.btn2))
        view_.add_item(Menu(self.root_, self.menu1))

        return view_


class Btn3AndDropMenu:
    def __init__(self, author: discord.Member, button1: SButton,
                 button2: SButton, button3: SButton, menu1: SDropMenu,
                 *, timeout: float = DEFAULT_TIMEOUT):
        self.author = author
        self.timeout = timeout

        self.btn1 = button1
        self.btn2 = button2
        self.btn3 = button3
        self.menu1 = menu1

        if self.btn1.author is None:
            self.btn1.update(author=self.author)
        if self.btn2.author is None:
            self.btn2.update(author=self.author)
        if self.btn3.author is None:
            self.btn3.update(author=self.author)
        if self.menu1.author is None:
            self.menu1.update(author=self.author)

        self.root_ = lambda: Btn3AndDropMenu(self.author, self.btn1, self.btn2,
                                             self.btn3, self.menu1, timeout=self.timeout)

    def view(self) -> ui.View:
        view_ = ui.View(timeout=self.timeout)
        view_.add_item(Btn(self.root_, self.btn1))
        view_.add_item(Btn(self.root_, self.btn2))
        view_.add_item(Btn(self.root_, self.btn3))
        view_.add_item(Menu(self.root_, self.menu1))

        return view_


class Btn4AndDropMenu:
    def __init__(self, author: discord.Member, button1: SButton,
                 button2: SButton, button3: SButton, button4: SButton, menu1: SDropMenu,
                 *, timeout: float = DEFAULT_TIMEOUT):
        self.author = author
        self.timeout = timeout

        self.btn1 = button1
        self.btn2 = button2
        self.btn3 = button3
        self.btn4 = button4
        self.menu1 = menu1

        if self.btn1.author is None:
            self.btn1.update(author=self.author)
        if self.btn2.author is None:
            self.btn2.update(author=self.author)
        if self.btn3.author is None:
            self.btn3.update(author=self.author)
        if self.btn4.author is None:
            self.btn4.update(author=self.author)
        if self.menu1.author is None:
            self.menu1.update(author=self.author)

        self.root_ = lambda: Btn4AndDropMenu(self.author, self.btn1, self.btn2,
                                             self.btn3, self.btn4, self.menu1, timeout=self.timeout)

    def view(self) -> ui.View:
        view_ = ui.View(timeout=self.timeout)
        view_.add_item(Btn(self.root_, self.btn1))
        view_.add_item(Btn(self.root_, self.btn2))
        view_.add_item(Btn(self.root_, self.btn3))
        view_.add_item(Menu(self.root_, self.menu1))

        return view_


class BtnAnd2DropMenu:
    def __init__(self, author: discord.Member, button1: SButton, menu1: SDropMenu, menu2: SDropMenu,
                 *, timeout: float = DEFAULT_TIMEOUT):
        self.author = author
        self.timeout = timeout

        self.btn1 = button1
        self.menu1 = menu1
        self.menu2 = menu2

        if self.btn1.author is None:
            self.btn1.update(author=self.author)
        if self.menu1.author is None:
            self.menu1.update(author=self.author)
        if self.menu2.author is None:
            self.menu2.update(author=self.author)

        self.root_ = lambda: BtnAnd2DropMenu(self.author, self.btn1, self.menu1, self.menu2, timeout=self.timeout)

    def view(self) -> ui.View:
        view_ = ui.View(timeout=self.timeout)
        view_.add_item(Btn(self.root_, self.btn1))
        view_.add_item(Menu(self.root_, self.menu1))
        view_.add_item(Menu(self.root_, self.menu2))

        return view_


class Btn2And2DropMenu:
    def __init__(self, author: discord.Member, button1: SButton, button2: SButton, menu1: SDropMenu, menu2: SDropMenu,
                 *, timeout: float = DEFAULT_TIMEOUT):
        self.author = author
        self.timeout = timeout

        self.btn1 = button1
        self.btn2 = button2
        self.menu1 = menu1
        self.menu2 = menu2

        if self.btn1.author is None:
            self.btn1.update(author=self.author)
        if self.btn2.author is None:
            self.btn2.update(author=self.author)
        if self.menu1.author is None:
            self.menu1.update(author=self.author)
        if self.menu2.author is None:
            self.menu2.update(author=self.author)

        self.root_ = lambda: Btn2And2DropMenu(self.author, self.btn1, self.btn2, self.menu1,
                                              self.menu2, timeout=self.timeout)

    def view(self) -> ui.View:
        view_ = ui.View(timeout=self.timeout)
        view_.add_item(Btn(self.root_, self.btn1))
        view_.add_item(Btn(self.root_, self.btn2))
        view_.add_item(Menu(self.root_, self.menu1))
        view_.add_item(Menu(self.root_, self.menu2))

        return view_


class Btn3And2DropMenu:
    def __init__(self, author: discord.Member, button1: SButton, button2: SButton, button3: SButton,
                 menu1: SDropMenu, menu2: SDropMenu,
                 *, timeout: float = DEFAULT_TIMEOUT):
        self.author = author
        self.timeout = timeout

        self.btn1 = button1
        self.btn2 = button2
        self.btn3 = button3
        self.menu1 = menu1
        self.menu2 = menu2

        if self.btn1.author is None:
            self.btn1.update(author=self.author)
        if self.btn2.author is None:
            self.btn2.update(author=self.author)
        if self.btn3.author is None:
            self.btn3.update(author=self.author)
        if self.menu1.author is None:
            self.menu1.update(author=self.author)
        if self.menu2.author is None:
            self.menu2.update(author=self.author)

        self.root_ = lambda: Btn3And2DropMenu(self.author, self.btn1, self.btn2, self.btn3, self.menu1,
                                              self.menu2, timeout=self.timeout)

    def view(self) -> ui.View:
        view_ = ui.View(timeout=self.timeout)
        view_.add_item(Btn(self.root_, self.btn1))
        view_.add_item(Btn(self.root_, self.btn2))
        view_.add_item(Btn(self.root_, self.btn3))
        view_.add_item(Menu(self.root_, self.menu1))
        view_.add_item(Menu(self.root_, self.menu2))

        return view_


class BtnAnd3DropMenu:
    def __init__(self, author: discord.Member, button1: SButton,
                 menu1: SDropMenu, menu2: SDropMenu, menu3: SDropMenu,
                 *, timeout: float = DEFAULT_TIMEOUT):
        self.author = author
        self.timeout = timeout

        self.btn1 = button1
        self.menu1 = menu1
        self.menu2 = menu2
        self.menu3 = menu3

        if self.btn1.author is None:
            self.btn1.update(author=self.author)
        if self.menu1.author is None:
            self.menu1.update(author=self.author)
        if self.menu2.author is None:
            self.menu2.update(author=self.author)
        if self.menu3.author is None:
            self.menu3.update(author=self.author)

        self.root_ = lambda: BtnAnd3DropMenu(self.author, self.btn1, self.menu1, self.menu2,
                                             self.menu3, timeout=self.timeout)

    def view(self) -> ui.View:
        view_ = ui.View(timeout=self.timeout)
        view_.add_item(Btn(self.root_, self.btn1))
        view_.add_item(Menu(self.root_, self.menu1))
        view_.add_item(Menu(self.root_, self.menu2))
        view_.add_item(Menu(self.root_, self.menu3))

        return view_


class Btn2And3DropMenu:
    def __init__(self, author: discord.Member, button1: SButton, button2: SButton,
                 menu1: SDropMenu, menu2: SDropMenu, menu3: SDropMenu,
                 *, timeout: float = DEFAULT_TIMEOUT):
        self.author = author
        self.timeout = timeout

        self.btn1 = button1
        self.btn2 = button2
        self.menu1 = menu1
        self.menu2 = menu2
        self.menu3 = menu3

        if self.btn1.author is None:
            self.btn1.update(author=self.author)
        if self.btn2.author is None:
            self.btn2.update(author=self.author)
        if self.menu1.author is None:
            self.menu1.update(author=self.author)
        if self.menu2.author is None:
            self.menu2.update(author=self.author)
        if self.menu3.author is None:
            self.menu3.update(author=self.author)

        self.root_ = lambda: BtnAnd3DropMenu(self.author, self.btn1, self.menu1, self.menu2,
                                             self.menu3, timeout=self.timeout)

    def view(self) -> ui.View:
        view_ = ui.View(timeout=self.timeout)
        view_.add_item(Btn(self.root_, self.btn1))
        view_.add_item(Btn(self.root_, self.btn2))
        view_.add_item(Menu(self.root_, self.menu1))
        view_.add_item(Menu(self.root_, self.menu2))
        view_.add_item(Menu(self.root_, self.menu3))

        return view_


class BtnAnd4DropMenu:
    def __init__(self, author: discord.Member, button1: SButton,
                 menu1: SDropMenu, menu2: SDropMenu, menu3: SDropMenu, menu4: SDropMenu,
                 *, timeout: float = DEFAULT_TIMEOUT):
        self.author = author
        self.timeout = timeout

        self.btn1 = button1
        self.menu1 = menu1
        self.menu2 = menu2
        self.menu3 = menu3
        self.menu4 = menu4

        if self.btn1.author is None:
            self.btn1.update(author=self.author)
        if self.menu1.author is None:
            self.menu1.update(author=self.author)
        if self.menu2.author is None:
            self.menu2.update(author=self.author)
        if self.menu3.author is None:
            self.menu3.update(author=self.author)
        if self.menu4.author is None:
            self.menu4.update(author=self.author)

        self.root_ = lambda: BtnAnd4DropMenu(self.author, self.btn1, self.menu1, self.menu2,
                                             self.menu3, self.menu4, timeout=self.timeout)

    def view(self) -> ui.View:
        view_ = ui.View(timeout=self.timeout)
        view_.add_item(Btn(self.root_, self.btn1))
        view_.add_item(Menu(self.root_, self.menu1))
        view_.add_item(Menu(self.root_, self.menu2))
        view_.add_item(Menu(self.root_, self.menu3))
        view_.add_item(Menu(self.root_, self.menu4))

        return view_
