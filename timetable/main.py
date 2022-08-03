from datetime import datetime

import pandas as pd

from recipe import Recipe, Recipes

in_oven_times = {Recipes.DinkelQuarkBrot: datetime(2022, 8, 4, 15), Recipes.Haferbrot: datetime(2022, 8, 4, 16)}


if __name__ == "__main__":
    dinkelquarkbrot = Recipe(Recipes.DinkelQuarkBrot)
    haferbrot = Recipe(Recipes.Haferbrot)
    timetable = pd.concat(
        [
            dinkelquarkbrot.timetable(in_oven_times[Recipes.DinkelQuarkBrot]),
            haferbrot.timetable(in_oven_times[Recipes.Haferbrot]),
        ]
    )
    for index, row in timetable.sort_values("time").iterrows():
        steptime: datetime = row.time
        print(f"{steptime.strftime('%d.%m.%Y %H:%M:%S')}: {row.recipe} - {row.instruction}")
