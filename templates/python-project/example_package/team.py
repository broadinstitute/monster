from dataclasses import dataclass


@dataclass
class Team:
    name: str

    def is_cool(self) -> bool:
        return self.name == "monster"
