# === Stage 7: Группировка ===
# Project: FreezerMap
from collections import Counter


def group_by_box(ingredients):
    grouped = {}
    for ingredient in ingredients:
        box = ingredient["box"]
        grouped.setdefault(box, []).append(ingredient)
    counts = {box: len(items) for box, items in grouped.items()}
    return grouped, counts


def main():
    data = [
        {"name": "Говядина", "box": "A1", "weight": 1.2, "frozen": "2024-01-05"},
        {"name": "Курица", "box": "A1", "weight": 0.8, "frozen": "2024-01-06"},
        {"name": "Рыба", "box": "B2", "weight": 0.5, "frozen": "2024-01-07"},
        {"name": "Говядина", "box": "B2", "weight": 2.0, "frozen": "2024-01-08"},
        {"name": "Курица", "box": "C3", "weight": 1.5, "frozen": "2024-01-09"},
    ]
    grouped, counts = group_by_box(data)
    print("Группы:", grouped)
    print("Количество:", counts)


if __name__ == "__main__":
    main()
