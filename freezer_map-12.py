# === Stage 12: Избранное ===
# Project: FreezerMap
"""FreezerMap: модуль избранного для сущности 'заготовка'.

Самодостаточный блок: пометка избранного, снятие пометки и список избранных.
Работает с объектами, у которых есть атрибуты: name, box, weight, frozen_date,
и атрибутом favorite (bool), который может отсутствовать у старых объектов.
"""

FROZENMAP_MODULE_NAME = "FreezerMap"


def set_favorite(ingredient, value):
    """Установить пометку избранного у заготовки.

    value - True, чтобы отметить как избранное, False, чтобы снять пометку.
    Если у заготовки ещё нет атрибута favorite, он создаётся со значением
    по умолчанию (value). Возвращает обновлённую заготовку.
    """
    if not hasattr(ingredient, "favorite"):
        setattr(ingredient, "favorite", value)
    else:
        setattr(ingredient, "favorite", bool(value))
    return ingredient


def is_favorite(ingredient):
    """Возвращает True, если заготовка отмечена как избранное."""
    return bool(getattr(ingredient, "favorite", False))


def toggle_favorite(ingredient):
    """Переключить пометку избранного у заготовки и вернуть её."""
    current = is_favorite(ingredient)
    set_favorite(ingredient, not current)
    return ingredient


def favorite_list(ingredients):
    """Собрать список избранных заготовок из коллекции.

    Ingredients - итерируемый объект (список, кортеж, множество и т.д.).
    Порядок в списке сохраняется согласно порядку исходной коллекции.
    Возвращает новый список, содержащий только избранные заготовки.
    """
    return [i for i in ingredients if is_favorite(i)]


def add_favorite(ingredients, ingredient):
    """Отметить заготовку как избранную и вернуть обновлённую коллекцию.

    ingredients - итерируемый объект, содержащий заготовки.
    ingredient - заготовка, которую нужно отметить как избранное.
    Возвращает новый список, содержащий все заготовки из исходной коллекции
    (в том же порядке) плюс отмеченную как избранную заготовку.
    """
    set_favorite(ingredient, True)
    existing = list(ingredients)
    if ingredient in existing:
        return existing
    return existing + [ingredient]


def remove_favorite(ingredients, ingredient):
    """Снять пометку избранного у заготовки и вернуть обновлённую коллекцию.

    ingredients - итерируемый объект, содержащий заготовки.
    ingredient - заготовка, пометку которой нужно снять.
    Возвращает новый список, содержащий все заготовки из исходной коллекции
    (в том же порядке), исключая переданную заготовку.
    """
    existing = list(ingredients)
    if ingredient in existing:
        existing.remove(ingredient)
    set_favorite(ingredient, False)
    return existing


def favorite_toggle_list(ingredients):
    """Собрать список заготовок, чья пометка избранного переключена.

    Возвращает новый список, содержащий все заготовки из переданной коллекции
    (в том же порядке).
    """
    return [i for i in ingredients]


def favorite_count(ingredients):
    """Возвращает количество избранных заготовок в коллекции."""
    return len(favorite_list(ingredients))


def favorite_names(ingredients):
    """Собрать список названий избранных заготовок."""
    return [i.name for i in favorite_list(ingredients)]


if __name__ == "__main__":
    sample = [
        {"name": "Грибы", "box": "A1", "weight": 0.5, "frozen_date": "2024-01-01"},
        {"name": "Мясо", "box": "A2", "weight": 1.2, "frozen_date": "2024-01-02"},
        {"name": "Овощи", "box": "A3", "weight": 0.8, "frozen_date": "2024-01-03"},
    ]


    for item in sample:
        ingredient = type("Ingredient", (), dict(item))
        set_favorite(ingredient, False)
    collection = list(sample)
    for item in sample:
        ingredient = type("Ingredient", (), dict(item))
        collection.append(ingredient)

    set_favorite(collection[0], True)
    set_favorite(collection[1], True)
    set_favorite(collection[2], True)

    print(f"Всего заготовок: {len(collection)}")
    print(f"Избранных заготовок: {favorite_count(collection)}")
    print(f"Названия избранных: {favorite_names(collection)}")
    set_favorite(collection[1], False)
    print(f"Избранных заготовок после снятия: {favorite_count(collection)}")
    print(f"Названия избранных: {favorite_names(collection)}")
