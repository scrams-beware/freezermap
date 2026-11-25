# === Stage 10: Поиск дубликатов ===
# Project: FreezerMap
freezermap_dedup.py

from datetime import date

NORMALIZE_FIELDS = ("название", "ящик")


def normalize_value(value):
    if value is None:
        return ""
    text = str(value).strip().lower()
    return text


def normalize_record(record):
    return tuple(normalize_value(record.get(field)) for field in NORMALIZE_FIELDS)


def find_duplicate_indices(records):
    normalized = [normalize_record(record) for record in records]
    seen = {}
    duplicates = []
    for index, signature in enumerate(normalized):
        if signature in seen:
            duplicates.append(index)
        else:
            seen[signature] = index
    return duplicates


def group_duplicate_indices(records):
    duplicates = find_duplicate_indices(records)
    groups = {}
    for index in duplicates:
        signature = normalize_record(records[index])
        groups.setdefault(signature, []).append(index)
    return groups


def remove_duplicates(records):
    duplicates = find_duplicate_indices(records)
    duplicates_set = set(duplicates)
    unique = [record for index, record in enumerate(records) if index not in duplicates_set]
    return unique
