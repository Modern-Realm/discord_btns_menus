from typing import *


class ButtonException(Exception):
    pass


class MissingAdminPerms(ButtonException):
    def __init__(self):
        super().__init__("To interact with this button, you should be the Guild Owner !")


class MissingPerms(ButtonException):
    def __init__(self, perms: List[str]):
        error_ = f"To interact with this Button/Menu, you need {', '.join(perms)} perm(s)"
        super().__init__(error_)


class MissingRoles(ButtonException):
    def __init__(self, roles: List[str]):
        error_ = f"To interact with this Button/Menu, you need {', '.join(roles)} role(s)"
        super().__init__(error_)


class MissingAnyRole(ButtonException):
    def __init__(self, roles: List[str]):
        error_ = f"To interact with this Button/Menu, you need any one of the this {', '.join(roles)} role(s)"
        super().__init__(error_)


class InvalidInteractionUser(ButtonException):
    def __init__(self, current_user: str):
        error_ = f"Only the {current_user} can access/use this Button/Menu"
        super().__init__(error_)


class NotInUsers(ButtonException):
    def __init__(self, users: List[str]):
        error_ = f"Only the {', '.join(users)} user(s) can access/use this Button/Menu"
        super().__init__(error_)
