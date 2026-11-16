# === Stage 6: Теги ===
# Project: FreezerMap
from datetime import date
from typing import Dict, List, Optional


class Tag:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"Tag({self.name!r})"


class PreparedItem:
    def __init__(
        self,
        name: str,
        box: str,
        weight: float,
        freeze_date: date,
        tags: Optional[List[Tag]] = None,
    ):
        self.name = name
        self.box = box
        self.weight = weight
        self.freeze_date = freeze_date
        self.tags = tags if tags is not None else []

    def add_tag(self, name: str) -> "PreparedItem":
        if name not in self.tags:
            self.tags.append(Tag(name))
        return self

    def remove_tag(self, name: str) -> "PreparedItem":
        self.tags = [tag for tag in self.tags if tag.name != name]
        return self

    def get_tags(self) -> List[Tag]:
        return list(self.tags)

    def find_tag(self, name: str) -> Optional[Tag]:
        for tag in self.tags:
            if tag.name == name:
                return tag
        return None

    def __repr__(self):
        return (
            f"PreparedItem(name={self.name!r}, box={self.box!r}, "
            f"weight={self.weight}, freeze_date={self.freeze_date}, "
            f"tags={[t.name for t in self.tags]})"
        )


def create_tag(name: str) -> Tag:
    return Tag(name)


def find_by_tag(items: List[PreparedItem], tag_name: str) -> List[PreparedItem]:
    return [item for item in items if item.find_tag(tag_name) is not None]


def remove_tag_from_items(items: List[PreparedItem], tag_name: str) -> int:
    removed = 0
    for item in items:
        if item.remove_tag(tag_name) is not None:
            removed += 1
    return removed


if __name__ == "__main__":
    apple = PreparedItem("Яблоко", "box_A", 1.5, date(2024, 1, 15))
    apple.add_tag("фрукты")
    apple.add_tag("на пирог")

    carrot = PreparedItem("Морковь", "box_B", 0.8, date(2024, 1, 16))
    carrot.add_tag("овощи")

    items = [apple, carrot]

    print(find_by_tag(items, "фрукты"))
    print(find_by_tag(items, "овощи"))
    print(remove_tag_from_items(items, "фрукты"))
    print(items[0].get_tags())
