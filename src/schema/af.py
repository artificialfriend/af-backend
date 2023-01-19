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


class BubbleColor(Enum):
    Blue = "Blue"


class AF(BaseModel):
    name: str
    skin_color: SkinColor
    freckles: Freckles
    hair_color: HairColor
    hair_style: HairStyle
    eye_color: EyeColor
    eye_lashes: EyeLashes
    bubble_color: BubbleColor

    def to_dict(self):
        d = {}
        for k, v in self.dict().items():
            if hasattr(v, "value"):
                d[k] = v.value
            else:
                d[k] = v
        return d


if __name__ == "__main__":
    af_dict = {
        "name": "Klara",
        "skin_color": "Caramel",
        "freckles": "Few",
        "hair_color": "White",
        "hair_style": "Wavy",
        "eye_color": "Hazel",
        "eye_lashes": "Straight",
        "bubble_color": "Blue",
    }

    af = AF(**af_dict)

    print(af.to_dict())
