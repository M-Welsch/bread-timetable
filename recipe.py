from datetime import timedelta, datetime
from typing import Dict, List


class Recipe:
    def __init__(self, recipe: Dict[str, timedelta]) -> None:
        self._recipe = recipe

    def timetable(self, in_oven_time: datetime) -> List[str]:
        table = []
        total_timedelta = timedelta()
        for td in list(self._recipe.values()):
            total_timedelta += td
        start_time = in_oven_time - total_timedelta - list(self._recipe.values())[-1]

        time_elapsed = timedelta()
        for step, time_needed in self._recipe.items():
            time_elapsed += time_needed
            step_time = start_time + time_elapsed
            table.append(f"{step_time.strftime('%d.%m.%Y %H:%M:%S')}: {step}")
        return table

