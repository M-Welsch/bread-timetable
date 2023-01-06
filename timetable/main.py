from datetime import datetime
from pathlib import Path

import pandas as pd

from timetable.bread_calendar import create_calendar
from timetable.recipe import Recipes, timetable_for_recipe

in_oven_times = {
    Recipes.Haferbrot_2kg: datetime(2023, 1, 7, 13)
}


def main():
    timetable = pd.concat(
        [
            timetable_for_recipe(Recipes.DinkelQuarkBrot_2kg, in_oven_times[Recipes.Haferbrot_2kg]),
            timetable_for_recipe(Recipes.Haferbrot_1kg, in_oven_times[Recipes.Haferbrot_2kg], multiplier=2),
            timetable_for_recipe(Recipes.RoggenvollkornbrotMitRoestbrot_per_1kg, in_oven_times[Recipes.Haferbrot_2kg], multiplier=2),
            timetable_for_recipe(Recipes.Holzofen, in_oven_times[Recipes.Haferbrot_2kg])
        ]
    )
    for index, row in timetable.sort_values("time").iterrows():
        steptime: datetime = row.time
        if not row.instruction:
            continue
        print(f"{steptime.strftime('%d.%m.%Y %H:%M:%S')}: {row.recipe} - {row.instruction}", end="")
        if row.ingredients:
            print(f": {row.ingredients}")
        else:
            print("")
    with open("cal.ics", "wb") as f:
        f.write(create_calendar(timetable))


if __name__ == "__main__":
    main()
