from enum import Enum
from typing import Optional
from pydantic import BaseModel


class SkinColor(Enum):
    Green = "Green"
    Blue = "Blue"
    Purple = "Purple"
    Pink = "Pink"


class Freckles(Enum):
    NoFreckles = "No Freckles"
    Freckles = "Freckles"


class HairColor(Enum):
    Green = "Green"
    Blue = "Blue"
    Purple = "Purple"
    Pink = "Pink"
    White = "White"
    Black = "Black"


class HairStyle(Enum):
    Hairstyle1 = "Hairstyle 1"
    Hairstyle2 = "Hairstyle 2"
    Hairstyle3 = "Hairstyle 3"
    Hairstyle4 = "Hairstyle 4"


class EyeColor(Enum):
    Green = "Green"
    Blue = "Blue"
    Purple = "Purple"
    Pink = "Pink"
    Yellow = "Yellow"
    Brown = "Brown"


class EyeLashes(Enum):
    ShortEyelashes = "Short Eyelashes"
    LongEyelashes = "Long Eyelashes"


class AF(BaseModel):
    af_id: Optional[int]
    name: str
    skin_color: SkinColor
    freckles: Freckles
    hair_color: HairColor
    hair_style: HairStyle
    eye_color: EyeColor
    eye_lashes: EyeLashes
