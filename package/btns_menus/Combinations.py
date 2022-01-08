from btns_menus.builds.abc import *
from btns_menus.builds.button_ import SButton, Btn
from btns_menus.builds.menu_ import SDropMenu, Menu

from typing import *
import discord
from discord import ui


class BtnAndDropMenu:
    def __init__(self, author: discord.Member, button1: SButton, menu1: SDropMenu,
                 *, timeout: Optional[float] = DEFAULT_TIMEOUT):
        """
        Responsive Buttons and DropMenus

        :param author: Interaction User
        :param button1: takes button type SButton
        :param menu1: takes dropmenu type SDropMenu
        :param timeout: Interaction Timeout

        :returns: view: discord.ui.View
        """

        self.author = author
        self.timeout = timeout

        self.btn1 = button1
        self.menu1 = menu1

        self.components = [self.btn1, self.menu1]
        for component_ in self.components:
            if component_.author is None:
                component_.update(author=self.author)

        self.root_ = lambda: BtnAndDropMenu(
            self.author, self.btn1, self.menu1, timeout=self.timeout)

    def view(self) -> ui.View:
        """:returns: discord.ui.View"""

        view_ = ui.View(timeout=self.timeout)
        for component_ in self.components:
            if not component_.hidden:
                if isinstance(component_, SButton):
                    view_.add_item(Btn(self.root_, component_))
                else:
                    view_.add_item(Menu(self.root_, component_))

        return view_


class Btn2AndDropMenu:
    def __init__(self, author: discord.Member, button1: SButton, button2: SButton, menu1: SDropMenu,
                 *, timeout: Optional[float] = DEFAULT_TIMEOUT):
        """
        Responsive Buttons and DropMenus

        :param author: Interaction User
        :param button1: takes button type SButton
        :param button2: takes button type SButton
        :param menu1: takes Dropmenu type SDropMenu
        :param timeout: Interaction Timeout

        :returns: view: discord.ui.View
        """

        self.author = author
        self.timeout = timeout

        self.btn1 = button1
        self.btn2 = button2
        self.menu1 = menu1

        self.components = [self.btn1, self.btn2, self.menu1]
        for component_ in self.components:
            if component_.author is None:
                component_.update(author=self.author)

        self.root_ = lambda: Btn2AndDropMenu(
            self.author, self.btn1, self.btn2, self.menu1, timeout=self.timeout)

    def view(self) -> ui.View:
        """:returns: discord.ui.View"""

        view_ = ui.View(timeout=self.timeout)
        for component_ in self.components:
            if not component_.hidden:
                if isinstance(component_, SButton):
                    view_.add_item(Btn(self.root_, component_))
                else:
                    view_.add_item(Menu(self.root_, component_))

        return view_


class Btn3AndDropMenu:
    def __init__(self, author: discord.Member, button1: SButton,
                 button2: SButton, button3: SButton, menu1: SDropMenu,
                 *, timeout: Optional[float] = DEFAULT_TIMEOUT):
        """
        Responsive Buttons and DropMenus

        :param author: Interaction User
        :param button1: takes button type SButton
        :param button2: takes button type SButton
        :param button3: takes button type SButton
        :param menu1: takes dropmenu type SDropMenu
        :param timeout: Interaction Timeout

        :returns: view: discord.ui.View
        """

        self.author = author
        self.timeout = timeout

        self.btn1 = button1
        self.btn2 = button2
        self.btn3 = button3
        self.menu1 = menu1

        self.components = [self.btn1, self.btn2, self.btn3, self.menu1]
        for component_ in self.components:
            if component_.author is None:
                component_.update(author=self.author)

        self.root_ = lambda: Btn3AndDropMenu(self.author, self.btn1, self.btn2,
                                             self.btn3, self.menu1, timeout=self.timeout)

    def view(self) -> ui.View:
        view_ = ui.View(timeout=self.timeout)
        for component_ in self.components:
            if not component_.hidden:
                if isinstance(component_, SButton):
                    view_.add_item(Btn(self.root_, component_))
                else:
                    view_.add_item(Menu(self.root_, component_))

        return view_


class Btn4AndDropMenu:
    def __init__(self, author: discord.Member, button1: SButton,
                 button2: SButton, button3: SButton, button4: SButton, menu1: SDropMenu,
                 *, timeout: Optional[float] = DEFAULT_TIMEOUT):
        """
        Responsive Buttons and DropMenus

        :param author: Interaction User
        :param button1: takes button type SButton
        :param button2: takes button type SButton
        :param button3: takes button type SButton
        :param button4: takes button type SButton
        :param menu1: takes dropmenu type SDropMenu
        :param timeout: Interaction Timeout

        :returns: view: discord.ui.View
        """

        self.author = author
        self.timeout = timeout

        self.btn1 = button1
        self.btn2 = button2
        self.btn3 = button3
        self.btn4 = button4
        self.menu1 = menu1

        self.components = [self.btn1, self.btn2,
                           self.btn3, self.btn4, self.menu1]
        for component_ in self.components:
            if component_.author is None:
                component_.update(author=self.author)

        self.root_ = lambda: Btn4AndDropMenu(self.author, self.btn1, self.btn2,
                                             self.btn3, self.btn4, self.menu1, timeout=self.timeout)

    def view(self) -> ui.View:
        """:returns: discord.ui.View"""

        view_ = ui.View(timeout=self.timeout)
        for component_ in self.components:
            if not component_.hidden:
                if isinstance(component_, SButton):
                    view_.add_item(Btn(self.root_, component_))
                else:
                    view_.add_item(Menu(self.root_, component_))

        return view_


class BtnAnd2DropMenu:
    def __init__(self, author: discord.Member, button1: SButton, menu1: SDropMenu, menu2: SDropMenu,
                 *, timeout: Optional[float] = DEFAULT_TIMEOUT):
        """
        Responsive Buttons and DropMenus

        :param author: Interaction User
        :param button1: takes button type SButton
        :param menu1: takes dropmenu type SDropMenu
        :param menu2: takes dropmenu type SDropMenu
        :param timeout: Interaction Timeout

        :returns: view: discord.ui.View
        """

        self.author = author
        self.timeout = timeout

        self.btn1 = button1
        self.menu1 = menu1
        self.menu2 = menu2

        self.components = [self.btn1, self.menu1, menu2]
        for component_ in self.components:
            if component_.author is None:
                component_.update(author=self.author)

        self.root_ = lambda: BtnAnd2DropMenu(
            self.author, self.btn1, self.menu1, self.menu2, timeout=self.timeout)

    def view(self) -> ui.View:
        """:returns: discord.ui.View"""

        view_ = ui.View(timeout=self.timeout)
        for component_ in self.components:
            if not component_.hidden:
                if isinstance(component_, SButton):
                    view_.add_item(Btn(self.root_, component_))
                else:
                    view_.add_item(Menu(self.root_, component_))

        return view_


class Btn2And2DropMenu:
    def __init__(self, author: discord.Member, button1: SButton, button2: SButton, menu1: SDropMenu, menu2: SDropMenu,
                 *, timeout: Optional[float] = DEFAULT_TIMEOUT):
        """
        Responsive Buttons and DropMenus

        :param author: Interaction User
        :param button1: takes button type SButton
        :param button2: takes button type SButton
        :param menu1: takes dropmenu type SDropMenu
        :param menu2: takes dropmenu type SDropMenu
        :param timeout: Interaction Timeout

        :returns: view: discord.ui.View
        """

        self.author = author
        self.timeout = timeout

        self.btn1 = button1
        self.btn2 = button2
        self.menu1 = menu1
        self.menu2 = menu2

        self.components = [self.btn1, self.btn2, self.menu1, self.menu2]
        for component_ in self.components:
            if component_.author is None:
                component_.update(author=self.author)

        self.root_ = lambda: Btn2And2DropMenu(self.author, self.btn1, self.btn2, self.menu1,
                                              self.menu2, timeout=self.timeout)

    def view(self) -> ui.View:
        """:returns: discord.ui.View"""

        view_ = ui.View(timeout=self.timeout)
        for component_ in self.components:
            if not component_.hidden:
                if isinstance(component_, SButton):
                    view_.add_item(Btn(self.root_, component_))
                else:
                    view_.add_item(Menu(self.root_, component_))

        return view_


class Btn3And2DropMenu:
    def __init__(self, author: discord.Member, button1: SButton, button2: SButton, button3: SButton,
                 menu1: SDropMenu, menu2: SDropMenu,
                 *, timeout: Optional[float] = DEFAULT_TIMEOUT):
        """
        Responsive Buttons and DropMenus

        :param author: Interaction User
        :param button1: takes button type SButton
        :param button2: takes button type SButton
        :param button3: takes button type SButton
        :param menu1: takes dropmenu type SDropMenu
        :param menu2: takes dropmenu type SDropMenu
        :param timeout: Interaction Timeout

        :returns: view: discord.ui.View
        """

        self.author = author
        self.timeout = timeout

        self.btn1 = button1
        self.btn2 = button2
        self.btn3 = button3
        self.menu1 = menu1
        self.menu2 = menu2

        self.components = [self.btn1, self.btn2,
                           self.btn3, self.menu1, self.menu2]
        for component_ in self.components:
            if component_.author is None:
                component_.update(author=self.author)

        self.root_ = lambda: Btn3And2DropMenu(self.author, self.btn1, self.btn2, self.btn3, self.menu1,
                                              self.menu2, timeout=self.timeout)

    def view(self) -> ui.View:
        """:returns: discord.ui.View"""

        view_ = ui.View(timeout=self.timeout)
        for component_ in self.components:
            if not component_.hidden:
                if isinstance(component_, SButton):
                    view_.add_item(Btn(self.root_, component_))
                else:
                    view_.add_item(Menu(self.root_, component_))

        return view_


class BtnAnd3DropMenu:
    def __init__(self, author: discord.Member, button1: SButton,
                 menu1: SDropMenu, menu2: SDropMenu, menu3: SDropMenu,
                 *, timeout: Optional[float] = DEFAULT_TIMEOUT):
        """
        Responsive Buttons and DropMenus

        :param author: Interaction User
        :param button1: takes button type SButton
        :param menu1: takes dropmenu type SDropMenu
        :param menu2: takes dropmenu type SDropMenu
        :param menu3: takes dropmenu type SDropMenu
        :param timeout: Interaction Timeout

        :returns: view: discord.ui.View
        """

        self.author = author
        self.timeout = timeout

        self.btn1 = button1
        self.menu1 = menu1
        self.menu2 = menu2
        self.menu3 = menu3

        self.components = [self.btn1, self.menu1, self.menu2, self.menu3]
        for component_ in self.components:
            if component_.author is None:
                component_.update(author=self.author)

        self.root_ = lambda: BtnAnd3DropMenu(self.author, self.btn1, self.menu1, self.menu2,
                                             self.menu3, timeout=self.timeout)

    def view(self) -> ui.View:
        """:returns: discord.ui.View"""

        view_ = ui.View(timeout=self.timeout)
        for component_ in self.components:
            if not component_.hidden:
                if isinstance(component_, SButton):
                    view_.add_item(Btn(self.root_, component_))
                else:
                    view_.add_item(Menu(self.root_, component_))

        return view_


class Btn2And3DropMenu:
    def __init__(self, author: discord.Member, button1: SButton, button2: SButton,
                 menu1: SDropMenu, menu2: SDropMenu, menu3: SDropMenu,
                 *, timeout: Optional[float] = DEFAULT_TIMEOUT):
        """
        Responsive Buttons and DropMenus

        :param author: Interaction User
        :param button1: takes button type SButton
        :param button2: takes button type SButton
        :param menu1: takes dropmenu type SDropMenu
        :param menu2: takes dropmenu type SDropMenu
        :param menu3: takes dropmenu type SDropMenu
        :param timeout: Interaction Timeout

        :returns: view: discord.ui.View
        """

        self.author = author
        self.timeout = timeout

        self.btn1 = button1
        self.btn2 = button2
        self.menu1 = menu1
        self.menu2 = menu2
        self.menu3 = menu3

        self.components = [self.btn1, self.btn2,
                           self.menu1, self.menu2, self.menu3]
        for component_ in self.components:
            if component_.author is None:
                component_.update(author=self.author)

        self.root_ = lambda: BtnAnd3DropMenu(self.author, self.btn1, self.menu1, self.menu2,
                                             self.menu3, timeout=self.timeout)

    def view(self) -> ui.View:
        """:returns: discord.ui.View"""

        view_ = ui.View(timeout=self.timeout)
        for component_ in self.components:
            if not component_.hidden:
                if isinstance(component_, SButton):
                    view_.add_item(Btn(self.root_, component_))
                else:
                    view_.add_item(Menu(self.root_, component_))

        return view_


class BtnAnd4DropMenu:
    def __init__(self, author: discord.Member, button1: SButton,
                 menu1: SDropMenu, menu2: SDropMenu, menu3: SDropMenu, menu4: SDropMenu,
                 *, timeout: Optional[float] = DEFAULT_TIMEOUT):
        """
        Responsive Buttons and DropMenus

        :param author: Interaction User
        :param button1: takes button type SButton
        :param menu1: takes dropmenu type SDropMenu
        :param menu2: takes dropmenu type SDropMenu
        :param menu3: takes dropmenu type SDropMenu
        :param menu4: takes dropmenu type SDropMenu
        :param timeout: Interaction Timeout

        :returns: view: discord.ui.View
        """

        self.author = author
        self.timeout = timeout

        self.btn1 = button1
        self.menu1 = menu1
        self.menu2 = menu2
        self.menu3 = menu3
        self.menu4 = menu4

        self.components = [self.btn1, self.menu1,
                           self.menu2, self.menu3, self.menu4]
        for component_ in self.components:
            if component_.author is None:
                component_.update(author=self.author)

        self.root_ = lambda: BtnAnd4DropMenu(self.author, self.btn1, self.menu1, self.menu2,
                                             self.menu3, self.menu4, timeout=self.timeout)

    def view(self) -> ui.View:
        """:returns: discord.ui.View"""

        view_ = ui.View(timeout=self.timeout)
        for component_ in self.components:
            if not component_.hidden:
                if isinstance(component_, SButton):
                    view_.add_item(Btn(self.root_, component_))
                else:
                    view_.add_item(Menu(self.root_, component_))

        return view_


class MultiBtnAndDropMenu:
    def __init__(self, author: discord.Member, buttons: List[SButton], menus: List[SDropMenu],
                 *, timeout: Optional[float] = DEFAULT_TIMEOUT):
        """
        Responsive Buttons and DropMenus

        :param author: Interaction User
        :param buttons: takes List of button type SButton
        :param menus: takes List of dropmenu type SDropMenu
        :param timeout: Interaction Timeout

        :returns: view: discord.ui.View
        """

        self.author = author
        self.timeout = timeout
        self.btns: List = buttons
        self.menus: List = menus

        components: List = self.btns + self.menus
        for component_ in components:
            if component_.author is None:
                component_.update(author=self.author)

        self.root_ = lambda: MultiBtnAndDropMenu(
            self.author, self.btns, self.menus, timeout=self.timeout)

    def view(self) -> ui.View:
        """:returns: discord.ui.View"""

        view_ = ui.View(timeout=self.timeout)
        for btn_ in self.btns:
            if not btn_.hidden:
                view_.add_item(Btn(self.root_, btn_))

        for menu_ in self.menus:
            if not menu_.hidden:
                view_.add_item(Menu(self.root_, menu_))

        return view_


MultiBtnAndMenu = MultiBtnAndDropMenu


class MultiBtnsAndMenus:
    def __init__(self, author: discord.Member, components: List[Union[SButton, SDropMenu]],
                 *, timeout: Optional[float] = DEFAULT_TIMEOUT):
        """
        🌟 Full Flexibility

        Responsive Buttons and DropMenus

        :param author: Interaction User
        :param components: Takes List of components (both buttons and drop menus)
        :param timeout: Interaction Timeout

        :returns: view: discord.ui.View
        """

        self.author = author
        self.timeout = timeout
        self.components = components

        for component in self.components:
            if component.author is None:
                component.update(author=self.author)

        self.root_ = lambda: MultiBtnsAndMenus(
            self.author, self.components, timeout=self.timeout)

    def view(self) -> ui.View:
        """:returns: discord.ui.View"""

        view_ = ui.View(timeout=self.timeout)
        for component in self.components:
            if not component.hidden:
                if isinstance(component, SButton):
                    view_.add_item(Btn(self.root_, component))
                elif isinstance(component, SDropMenu):
                    view_.add_item(Menu(self.root_, component))
                else:
                    raise ValueError("The given components are Invalid !")

        return view_
