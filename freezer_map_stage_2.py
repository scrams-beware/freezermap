# === Stage 2: Проверка полей ===
# Project: FreezerMap
def normalize_name(value):
    return value.strip().title()


def normalize_box(value):
    return value.strip().lower()


def normalize_weight(value):
    text = value.strip().replace(",", ".")
    return float(text)


def normalize_date(value):
    parts = value.strip().split()
    if len(parts) != 2:
        raise ValueError("Дата заморозки должна быть в формате ДД.ММ.ГГГГ")
    day, rest = parts
    if "." not in day:
        raise ValueError("День должен быть в формате ДД.ММ.ГГГГ")
    day_part, month_year = day.split(".")
    if len(month_year) != 5 or month_year[0] != ".":
        raise ValueError("Дата должна быть в формате ДД.ММ.ГГГГ")
    month = month_year[1:3]
    year = month_year[3:]
    if not (1 <= int(month) <= 12):
        raise ValueError("Месяц должен быть от 01 до 12")
    if not (1 <= int(day_part) <= 31):
        raise ValueError("День должен быть от 01 до 31")
    return f"{day_part}.{month}.{year}"


class PreparationError(Exception):
    pass


class Preparation:
    def __init__(self, name, box, weight, freeze_date):
        self.name = self.validate_name(name)
        self.box = self.validate_box(box)
        self.weight = self.validate_weight(weight)
        self.freeze_date = self.validate_date(freeze_date)

    @staticmethod
    def validate_name(name):
        normalized = normalize_name(name)
        if not normalized:
            raise PreparationError("Название заготовки не может быть пустым")
        if len(normalized) > 50:
            raise PreparationError("Название заготовки слишком длинное (максимум 50 символов)")
        return normalized

    @staticmethod
    def validate_box(box):
        normalized = normalize_box(box)
        if not normalized:
            raise PreparationError("Ящик не может быть пустым")
        if len(normalized) > 30:
            raise PreparationError("Название ящика слишком длинное (максимум 30 символов)")
        return normalized

    @staticmethod
    def validate_weight(weight):
        try:
            normalized = normalize_weight(weight)
        except ValueError:
            raise PreparationError("Вес должен быть числом")
        if normalized <= 0:
            raise PreparationError("Вес заготовки должен быть больше нуля")
        if normalized > 1000:
            raise PreparationError("Вес заготовки слишком большой (максимум 1000 кг)")
        return normalized

    @staticmethod
    def validate_date(freeze_date):
        try:
            normalized = normalize_date(freeze_date)
        except ValueError as exc:
            raise PreparationError(str(exc))
        return normalized
