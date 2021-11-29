from btns_menus.builds.base.in_build import *

from typing import *
import discord
from discord import ui


class SingleButton:
    def __init__(self, author: discord.Member, button1: SButton, /, timeout: float = DEFAULT_TIMEOUT):
        self.author = author
        self.timeout = timeout

        self.btn1 = button1

        if self.btn1.author is None:
            self.btn1.update(author=self.author)

        self.root_ = lambda: SingleButton(self.author, self.btn1, timeout=self.timeout)

    def view(self) -> ui.View:
        view_ = ui.View(timeout=self.timeout)
        view_.add_item(Btn(self.root_, self.btn1))

        return view_


class DuoButton:
    def __init__(self, author: discord.Member, button1: SButton, button2: SButton,
                 /, timeout: float = DEFAULT_TIMEOUT):
        self.author = author
        self.timeout = timeout

        self.btn1 = button1
        self.btn2 = button2

        if self.btn1.author is None:
            self.btn1.update(author=self.author)
        if self.btn2.author is None:
            self.btn2.update(author=self.author)

        self.root_ = lambda: DuoButton(self.author, self.btn1, self.btn2, timeout=self.timeout)

    def view(self) -> ui.View:
        view_ = ui.View(timeout=self.timeout)
        view_.add_item(Btn(self.root_, self.btn1))
        view_.add_item(Btn(self.root_, self.btn2))

        return view_


class TrioButton:
    def __init__(self, author: discord.Member, button1: SButton, button2: SButton, button3: SButton,
                 /, timeout: float = DEFAULT_TIMEOUT):
        self.author = author
        self.timeout = timeout

        self.btn1 = button1
        self.btn2 = button2
        self.btn3 = button3

        if self.btn1.author is None:
            self.btn1.update(author=self.author)
        if self.btn2.author is None:
            self.btn2.update(author=self.author)
        if self.btn3.author is None:
            self.btn3.update(author=self.author)

        self.root_ = lambda: TrioDropMenu(self.author, self.btn1, self.btn2, self.btn3, timeout=self.timeout)

    def view(self) -> ui.View:
        view_ = ui.View(timeout=self.timeout)
        view_.add_item(Btn(self.root_, self.btn1))
        view_.add_item(Btn(self.root_, self.btn2))
        view_.add_item(Btn(self.root_, self.btn3))

        return view_


class QuartetButton:
    def __init__(self, author: discord.Member, button1: SButton, button2: SButton, button3: SButton, button4: SButton,
                 /, timeout: float = DEFAULT_TIMEOUT):
        self.author = author
        self.timeout = timeout

        self.btn1 = button1
        self.btn2 = button2
        self.btn3 = button3
        self.btn4 = button4

        if self.btn1.author is None:
            self.btn1.update(author=self.author)
        if self.btn2.author is None:
            self.btn2.update(author=self.author)
        if self.btn3.author is None:
            self.btn3.update(author=self.author)
        if self.btn4.author is None:
            self.btn4.update(author=self.author)

        self.root_ = lambda: QuartetButton(self.author, self.btn1, self.btn2,
                                           self.btn3, self.btn4, timeout=self.timeout)

    def view(self) -> ui.View:
        view_ = ui.View(timeout=self.timeout)
        view_.add_item(Btn(self.root_, self.btn1))
        view_.add_item(Btn(self.root_, self.btn2))
        view_.add_item(Btn(self.root_, self.btn3))
        view_.add_item(Btn(self.root_, self.btn4))

        return view_


class QuintetButton:
    def __init__(self, author: discord.Member, button1: SButton, button2: SButton,
                 button3: SButton, button4: SButton, button5: SButton,
                 /, timeout: float = DEFAULT_TIMEOUT):
        self.author = author
        self.timeout = timeout

        self.btn1 = button1
        self.btn2 = button2
        self.btn3 = button3
        self.btn4 = button4
        self.btn5 = button5

        if self.btn1.author is None:
            self.btn1.update(author=self.author)
        if self.btn2.author is None:
            self.btn2.update(author=self.author)
        if self.btn3.author is None:
            self.btn3.update(author=self.author)
        if self.btn4.author is None:
            self.btn4.update(author=self.author)
        if self.btn5.author is None:
            self.btn5.update(author=self.author)

        self.root_ = lambda: QuintetButton(self.author, self.btn1, self.btn2, self.btn3,
                                           self.btn4, self.btn5, timeout=self.timeout)

    def view(self) -> ui.View:
        view_ = ui.View(timeout=self.timeout)
        view_.add_item(Btn(self.root_, self.btn1))
        view_.add_item(Btn(self.root_, self.btn2))
        view_.add_item(Btn(self.root_, self.btn3))
        view_.add_item(Btn(self.root_, self.btn4))
        view_.add_item(Btn(self.root_, self.btn5))

        return view_
