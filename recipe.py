from datetime import timedelta, datetime
from typing import Dict, List
import pandas as pd


class Recipe:
    def __init__(self, recipe: Dict[str, timedelta]) -> None:
        self._recipe = recipe

    def timetable(self, in_oven_time: datetime) -> pd.DataFrame:
        start_time = self.start_time(in_oven_time)
        time_elapsed = timedelta()
        step_times = []
        instructions = []
        for step, time_needed in self._recipe.items():
            time_elapsed += time_needed
            step_time = start_time + time_elapsed
            step_times.append(step_time)
            instructions.append(step)
        return pd.DataFrame({
            "time": step_times,
            "instruction": instructions
        })

    def start_time(self, in_oven_time: datetime) -> datetime:
        total_timedelta = timedelta()
        for td in list(self._recipe.values()):
            total_timedelta += td
        time_for_last_step = list(self._recipe.values())[-1]
        return in_oven_time - total_timedelta - time_for_last_step
