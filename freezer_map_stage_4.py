# === Stage 4: Генерация идентификаторов ===
# Project: FreezerMap
import re
import uuid

PROJECT_PREFIX = "FM"


class IdentifierError(Exception):
    pass


def generate_id(name: str, prefix: str = PROJECT_PREFIX) -> str:
    if not name or not isinstance(name, str):
        raise IdentifierError("Имя не может быть пустым")

    slug = re.sub(r"[^a-zA-Z0-9]+", "-", name.strip())
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    unique = uuid.uuid4().hex[:8]
    return f"{prefix}-{slug}-{unique}"


def validate_unique(existing: set, new_id: str) -> bool:
    return new_id not in existing


def ensure_unique(existing: set, name: str, prefix: str = PROJECT_PREFIX) -> str:
    new_id = generate_id(name, prefix)
    while not validate_unique(existing, new_id):
        new_id = generate_id(name, prefix)
        existing.add(new_id)
    existing.add(new_id)
    return new_id


def parse_id(identifier: str) -> tuple[str, str, str]:
    parts = identifier.split("-")
    prefix = parts[0]
    name = "-".join(parts[1:-1])
    unique = parts[-1]
    return prefix, name, unique


def build_index(names: list[str], prefix: str = PROJECT_PREFIX) -> dict[str, str]:
    index: dict[str, str] = {}
    for name in names:
        index[ensure_unique(index, name, prefix)] = name
    return index
