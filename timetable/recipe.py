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
            "Sauerteig (100g Roggen, 100g Wasser, 10g AG), Kochstück machen (190 Dinkelschrot, 460ml Wasser)": timedelta(minutes=10),
            "Sauerteig, Kochstück reifen lassen": timedelta(hours=16),
            "Hauptteig machen (80g Sesam, 100g Joghurt, 560g Dinkel T630, 100g Roggen, 24g Salz, 16g Hefe, 100g Wasser)": timedelta(minutes=30),
            "Hauptteig gehen lassen 1": timedelta(minutes=60),
            "Rundwirken": timedelta(minutes=5),
            "Garen": timedelta(minutes=45),
        }
    ),
    Recipes.Haferbrot: OrderedDict(
        {
            "Sauerteig zusammenrühren (133g Haferf. fein, 166g Wasser (50°C), 26,7g AG, 3,3g Salz)": timedelta(minutes=5),
            "Sauerteig reifen lassen": timedelta(hours=4),
            "Brühstück machen (133g Haferfl. kernig, 266g Wasser, 11,3g Salz)": timedelta(minutes=5),
            "Brühstück reifen lassen": timedelta(hours=12),
            "Hauptteig machen (400g Haferfl. kernig, 266g Wasser, dann 133g Wasser jew. 40°, 6,7g Hefe)": timedelta(minutes=20),
            "Garen lassen": timedelta(minutes=60),
        }
    ),
    Recipes.DinkelKastenBrot: OrderedDict(
        {
            "Vorteig (260g Dinkel T630, 130g Wasser, 0,52g Hefe), Quellstück machen (66g Leinmehl, 260g Wasser, 26g Salz)": timedelta(hours=12),
            "Teig mischen (1040g Dinkelmehl T630, 456g Wasser (40°), 10g Hefe, 26g Öl": timedelta(minutes=15),
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
            step_times.append(step_time-time_needed)
            instructions.append(step)
        return pd.DataFrame({"time": step_times, "instruction": instructions, "recipe": self._recipe_name})

    def start_time(self, in_oven_time: datetime) -> datetime:
        total_timedelta = timedelta()
        for td in list(self._recipe.values()):
            total_timedelta += td
        time_for_last_step = list(self._recipe.values())[-1]
        return in_oven_time - total_timedelta #- time_for_last_step
