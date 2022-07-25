from datetime import datetime, timedelta
from collections import OrderedDict
import pandas as pd

from recipe import Recipe

recipes = {
    "Dinkelbrot": OrderedDict({
        "Sauerteig zusammenruehren": timedelta(minutes=5),
        "Sauerteig reifen lassen": timedelta(hours=16),
        "Hauptteig machen": timedelta(minutes=30),
        "Hauptteig gehen lassen 1": timedelta(minutes=30),
        "Dehnen und Falten 1": timedelta(minutes=2),
        "Hauptteig gehen lassen 2": timedelta(minutes=30),
        "Dehnen und Falten 2": timedelta(minutes=2),
        "Hauptteig gehen lassen 3": timedelta(minutes=30),
        "Im Gärkorb reifen lassen": timedelta(minutes=45)
    })
}

in_oven_times = {
    "Dinkelbrot": datetime(2022, 8, 5, 15)
}


if __name__ == "__main__":
    recipe = Recipe(recipes["Dinkelbrot"])
    timetable = recipe.timetable(in_oven_times["Dinkelbrot"])
    for index, row in timetable.sort_values('time').iterrows():
        steptime: datetime = row.time
        print(f"{steptime.strftime('%d.%m.%Y %H:%M:%S')}: {row.instruction}")
