from collections import OrderedDict
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List

import pandas as pd


class Recipes(Enum):
    DinkelQuarkBrot = "Dinkel-Quark-Brot"
    DinkelKastenBrot = "Dinkel Kastenbrot"
    Haferbrot = "Haferbrot"


recipes = {
    Recipes.DinkelQuarkBrot: OrderedDict(
        {
            "Sauerteig, Kochstück machen": timedelta(minutes=10),
            "Sauerteig, Kochstück reifen lassen": timedelta(hours=16),
            "Hauptteig machen": timedelta(minutes=30),
            "Hauptteig gehen lassen 1": timedelta(minutes=60),
            "Rundwirken": timedelta(minutes=5),
            "Garen": timedelta(minutes=45),
        }
    ),
    Recipes.Haferbrot: OrderedDict(
        {
            "Sauerteig zusammenrühren": timedelta(minutes=5),
            "Sauerteig reifen lassen": timedelta(hours=4),
            "Brühstück machen": timedelta(minutes=5),
            "Brühstück reifen lassen": timedelta(hours=12),
            "Hauptteig machen": timedelta(minutes=20),
            "Garen lassen": timedelta(minutes=60),
        }
    ),
    Recipes.DinkelKastenBrot: OrderedDict(
        {
            "Vorteig, Quellstück machen": timedelta(hours=12),
            "Teig mischen": timedelta(minutes=15),
            "Teig ruhen lassen 1": timedelta(minutes=28),
            "Dehnen und Falten 1": timedelta(minutes=2),
            "Teig ruhen lassen 2": timedelta(minutes=28),
            "Dehnen und Falten 2": timedelta(minutes=2),
            "Teig ruhen lassen 3": timedelta(minutes=30),
            "Langwirken, in Kastenform": timedelta(minutes=5),
            "Reifen lassen": timedelta(minutes=90),
        }
    ),
}


class Recipe:
    def __init__(self, recipe: Recipes) -> None:
        self._recipe_name = recipe.value
        self._recipe: Dict[str, timedelta] = recipes[recipe]

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
        return pd.DataFrame({"time": step_times, "instruction": instructions, "recipe": self._recipe_name})

    def start_time(self, in_oven_time: datetime) -> datetime:
        total_timedelta = timedelta()
        for td in list(self._recipe.values()):
            total_timedelta += td
        time_for_last_step = list(self._recipe.values())[-1]
        return in_oven_time - total_timedelta - time_for_last_step
