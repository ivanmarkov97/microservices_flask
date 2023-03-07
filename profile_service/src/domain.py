import typing as t
from dataclasses import dataclass


@dataclass
class UserMainInfo:
    login: str
    name: str

    def to_dict(self) -> t.Dict[str, str]:
        return {
            'name': self.name,
            'login': self.login
        }


@dataclass
class UserAdditionalInfo:
    number_of_friends: int

    def to_dict(self) -> t.Dict[str, int]:
        return {
            'number_of_friend': self.number_of_friends
        }
