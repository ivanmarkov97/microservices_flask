import typing as t
from dataclasses import dataclass


@dataclass
class User:
    login: str
    password: str
    name: str

    def to_dict(self) -> t.Dict[str, str]:
        return {
            'name': self.name,
            'login': self.login
        }
