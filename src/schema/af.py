from enum import Enum
from pydantic import BaseModel


class SkinColor(Enum):
    Black = "Black"
    Caramel = "Caramel"
    White = "White"


class Freckles(Enum):
    Few = "Few"
    Many = "Many"


class HairColor(Enum):
    Black = "Black"
    Blonde = "Blonde"
    Blue = "Blue"
    Brown = "Brown"
    Purple = "Purple"
    Red = "Red"
    White = "White"


class HairStyle(Enum):
    Curly = "Curly"
    Straight = "Straight"
    Wavy = "Wavy"


class EyeColor(Enum):
    Blue = "Blue"
    Hazel = "Hazel"


class EyeLashes(Enum):
    Curly = "Curly"
    Straight = "Straight"


class AF(BaseModel):
    name: str
    skin_color: SkinColor
    freckles: Freckles
    hair_color: HairColor
    hair_style: HairStyle
    eye_color: EyeColor
    eye_lashes: EyeLashes
