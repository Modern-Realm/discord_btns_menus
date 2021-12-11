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
        if not self.btn1.hidden:
            view_.add_item(Btn(self.root_, self.btn1))

        return view_


class DuoButton:
    def __init__(self, author: discord.Member, button1: SButton, button2: SButton,
                 /, timeout: float = DEFAULT_TIMEOUT):
        self.author = author
        self.timeout = timeout

        self.btns = [button1, button2]
        for btn_ in self.btns:
            if btn_.author is None:
                btn_.update(author=self.author)

        self.root_ = lambda: DuoButton(self.author, self.btns[0], self.btns[1], timeout=self.timeout)

    def view(self) -> ui.View:
        view_ = ui.View(timeout=self.timeout)
        for btn_ in self.btns:
            if not btn_.hidden:
                view_.add_item(Btn(self.root_, btn_))

        return view_


class TrioButton:
    def __init__(self, author: discord.Member, button1: SButton, button2: SButton, button3: SButton,
                 /, timeout: float = DEFAULT_TIMEOUT):
        self.author = author
        self.timeout = timeout

        self.btns = [button1, button2, button3]
        for btn_ in self.btns:
            if btn_.author is None:
                btn_.update(author=self.author)

        self.root_ = lambda: TrioButton(self.author, self.btns[0], self.btns[1], self.btns[2], timeout=self.timeout)

    def view(self) -> ui.View:
        view_ = ui.View(timeout=self.timeout)
        for btn_ in self.btns:
            if not btn_.hidden:
                view_.add_item(Btn(self.root_, btn_))

        return view_


class QuartetButton:
    def __init__(self, author: discord.Member, button1: SButton, button2: SButton, button3: SButton, button4: SButton,
                 /, timeout: float = DEFAULT_TIMEOUT):
        self.author = author
        self.timeout = timeout

        self.btns = [button1, button2, button3, button4]
        for btn_ in self.btns:
            if btn_.author is None:
                btn_.update(author=self.author)

        self.root_ = lambda: QuartetButton(self.author, self.btns[0], self.btns[1],
                                           self.btns[2], self.btns[3], timeout=self.timeout)

    def view(self) -> ui.View:
        view_ = ui.View(timeout=self.timeout)
        for btn_ in self.btns:
            if not btn_.hidden:
                view_.add_item(Btn(self.root_, btn_))

        return view_


class QuintetButton:
    def __init__(self, author: discord.Member, button1: SButton, button2: SButton,
                 button3: SButton, button4: SButton, button5: SButton,
                 /, timeout: float = DEFAULT_TIMEOUT):
        self.author = author
        self.timeout = timeout

        self.btns = [button1, button2, button3, button4, button5]
        for btn_ in self.btns:
            if btn_.author is None:
                btn_.update(author=self.author)

        self.root_ = lambda: QuintetButton(self.author, self.btns[0], self.btns[1], self.btns[2],
                                           self.btns[3], self.btns[4], timeout=self.timeout)

    def view(self) -> ui.View:
        view_ = ui.View(timeout=self.timeout)
        for btn_ in self.btns:
            if not btn_.hidden:
                view_.add_item(Btn(self.root_, btn_))

        return view_


class MultiButton:
    def __init__(self, author: discord.Member, buttons: List[SButton], /, timeout: float = DEFAULT_TIMEOUT):
        self.author = author
        self.timeout = timeout
        self.btns = buttons

        for btn_ in self.btns:
            if btn_.author is None:
                btn_.update(author=self.author)

        self.root_ = lambda: MultiButton(self.author, self.btns, timeout=self.timeout)

    def view(self) -> ui.View:
        view_ = ui.View(timeout=self.timeout)
        for btn_ in self.btns:
            if not btn_.hidden:
                view_.add_item(Btn(self.root_, btn_))

        return view_
