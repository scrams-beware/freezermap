# === Stage 1: Каркас модуля ===
# Project: FreezerMap
from dataclasses import dataclass
from datetime import date


@dataclass
class Prep:
    name: str
    box: str
    weight: float
    frozen_date: date


def make_demo_preps() -> list[Prep]:
    return [
        Prep("Морковь", "box-a", 2.5, date(2024, 1, 15)),
        Prep("Лук", "box-a", 1.2, date(2024, 1, 16)),
        Prep("Груша", "box-b", 3.0, date(2024, 1, 17)),
    ]


def main() -> None:
    preps = make_demo_preps()
    print("FreezerMap — карта морозилки")
    print(f"Ящиков: {len({p.box for p in preps})}")
    for p in preps:
        print(f"{p.name} — {p.box} — {p.weight} кг — {p.frozen_date}")


if __name__ == "__main__":
    main()
