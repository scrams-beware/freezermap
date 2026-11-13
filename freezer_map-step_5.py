# === Stage 5: Сортировка записей ===
# Project: FreezerMap
sort_freezer_records.py

from datetime import datetime


def sort_by_name(records, ascending=True):
    """Сортировка заготовок по названию, возрастание или убывание."""
    key = lambda r: r["name"].lower()
    return sorted(records, key=key, reverse=not ascending)


def sort_by_freeze_date(records, ascending=True):
    """Сортировка заготовок по дате заморозки, возрастание или убывание."""
    key = lambda r: r["freeze_date"]
    return sorted(records, key=key, reverse=not ascending)


def sort_by_created_date(records, ascending=True):
    """Сортировка заготовок по дате создания записи, возрастание или убывание."""
    key = lambda r: r["created_at"]
    return sorted(records, key=key, reverse=not ascending)


def sort_records(records, field, ascending=True):
    """Универсальная сортировка заготовок по произвольному полю."""
    return sorted(records, key=lambda r: r.get(field), reverse=not ascending)


if __name__ == "__main__":
    sample = [
        {"name": "Морковь", "freeze_date": datetime(2024, 1, 5), "created_at": datetime(2024, 1, 1)},
        {"name": "Айва", "freeze_date": datetime(2024, 2, 10), "created_at": datetime(2024, 1, 2)},
        {"name": "Брокколи", "freeze_date": datetime(2024, 1, 20), "created_at": datetime(2024, 1, 3)},
    ]
    print(sort_by_name(sample))
    print(sort_by_freeze_date(sample))
    print(sort_by_created_date(sample))
    print(sort_records(sample, "name"))
    print(sort_records(sample, "created_at", ascending=False))
