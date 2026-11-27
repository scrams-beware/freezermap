# === Stage 11: Массовое обновление ===
# Project: FreezerMap
from datetime import datetime


class FreezerMap:
    def __init__(self, name, box_id):
        self.name = name
        self.box_id = box_id
        self.weight = 0.0
        self.frozen_date = None


class FreezerMapApp:
    def __init__(self):
        self.items = []
        self.boxes = {}

    def add_item(self, item):
        self.items.append(item)
        self.boxes.setdefault(item.box_id, []).append(item)

    def preview_update(self, predicate, changes):
        results = []
        for item in self.items:
            if predicate(item):
                results.append({
                    'name': item.name,
                    'box_id': item.box_id,
                    'old_weight': item.weight,
                    'new_weight': changes.get('weight', item.weight),
                    'old_date': item.frozen_date,
                    'new_date': changes.get('frozen_date', item.frozen_date),
                })
        return results

    def apply_update(self, predicate, changes):
        for item in self.items:
            if predicate(item):
                if 'weight' in changes:
                    item.weight = changes['weight']
                if 'frozen_date' in changes:
                    item.frozen_date = changes['frozen_date']
