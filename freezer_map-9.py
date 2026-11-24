# === Stage 9: Быстрые фильтры ===
# Project: FreezerMap
from datetime import date, timedelta

FREEZER_MAP_FILTERS = {
    "today": "today",
    "this_week": "this_week",
    "expired": "expired",
}


class FreezerMapFilter:
    def __init__(self, reference_date=None):
        self.reference_date = reference_date or date.today()
        self.start_of_week = self.reference_date - timedelta(
            days=self.reference_date.weekday()
        )
        self.start_of_next_week = self.start_of_week + timedelta(days=7)

    def filter_by_date(self, records):
        return [
            record
            for record in records
            if self._is_today(record["frozen_date"])
            or self._is_this_week(record["frozen_date"])
            or self._is_expired(record["frozen_date"])
        ]

    def filter_today(self, records):
        return [
            record
            for record in records
            if self._is_today(record["frozen_date"])
        ]

    def filter_this_week(self, records):
        return [
            record
            for record in records
            if self._is_this_week(record["frozen_date"])
        ]

    def filter_expired(self, records):
        return [
            record
            for record in records
            if self._is_expired(record["frozen_date"])
        ]

    def filter(self, name, records):
        return getattr(self, "filter_" + name)(records)

    def _is_today(self, frozen_date):
        return frozen_date == self.reference_date

    def _is_this_week(self, frozen_date):
        return (
            self.start_of_week <= frozen_date < self.start_of_next_week
        )

    def _is_expired(self, frozen_date):
        return frozen_date < self.reference_date
