# === Stage 3: Хранилище в памяти ===
# Project: FreezerMap
in_memory_freezer_store.py

from datetime import date


class Preparation:
    """Сущность «заготовка»: название, ящик, вес, дата заморозки."""

    __slots__ = ("id", "name", "box", "weight", "freeze_date")

    def __init__(self, id, name, box, weight, freeze_date):
        self.id = id
        self.name = name
        self.box = box
        self.weight = weight
        self.freeze_date = freeze_date

    def __repr__(self):
        return f"Preparation(id={self.id!r}, name={self.name!r}, box={self.box!r}, weight={self.weight}, freeze_date={self.freeze_date!r})"


class InMemoryPreparationStore:
    """Хранилище в памяти для сущностей «заготовка»."""

    def __init__(self):
        self._items = {}

    def add(self, preparation):
        if preparation.id in self._items:
            raise ValueError(f"Заготовка с id={preparation.id!r} уже существует")
        self._items[preparation.id] = preparation
        return preparation

    def get(self, id):
        if id not in self._items:
            raise KeyError(f"Заготовка с id={id!r} не найдена")
        return self._items[id]

    def exists(self, id):
        return id in self._items

    def list_all(self):
        return list(self._items.values())

    def count(self):
        return len(self._items)

    def clear(self):
        self._items.clear()


if __name__ == "__main__":
    store = InMemoryPreparationStore()

    box_id = "box_001"
    prep1 = Preparation(id="p1", name="Грибы", box=box_id, weight=350.0, freeze_date=date(2024, 1, 15))
    prep2 = Preparation(id="p2", name="Лук", box=box_id, weight=200.0, freeze_date=date(2024, 1, 20))

    store.add(prep1)
    store.add(prep2)

    print(f"Добавлено заготовок: {store.count()}")
    print("Список:")
    for p in store.list_all():
        print(f"  {p.name} ({p.weight} г) из ящика {p.box}, заморожена: {p.freeze_date}")

    print("Получение по id 'p2':", store.get("p2"))
    print("Проверка существования 'p1':", store.exists("p1"))
    print("Попытка получить 'p3':", end=" ")
    try:
        store.get("p3")
    except KeyError as e:
        print("ошибка:", e)
