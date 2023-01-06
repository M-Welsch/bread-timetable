from datetime import datetime
from pathlib import Path

import pandas as pd

from timetable.bread_calendar import save_calendar
from timetable.recipe import Recipe, Recipes

in_oven_times = {
    Recipes.Haferbrot_2kg: datetime(2023, 1, 7, 13)
}


if __name__ == "__main__":
    dinkelquarkbrot = Recipe(Recipes.DinkelQuarkBrot_2kg)
    haferbrot = Recipe(Recipes.Haferbrot_2kg)
    roggenvk = Recipe(Recipes.RoggenvollkornbrotMitRoestbrot_per_2kg)
    holzofen_vorbereitung = Recipe(Recipes.Holzofen)
    timetable = pd.concat(
        [
            holzofen_vorbereitung.timetable(in_oven_times[Recipes.Haferbrot_2kg]),
            dinkelquarkbrot.timetable(in_oven_times[Recipes.Haferbrot_2kg]),
            haferbrot.timetable(in_oven_times[Recipes.Haferbrot_2kg]),
            roggenvk.timetable(in_oven_times[Recipes.Haferbrot_2kg])
        ]
    )
    for index, row in timetable.sort_values("time").iterrows():
        steptime: datetime = row.time
        print(f"{steptime.strftime('%d.%m.%Y %H:%M:%S')}: {row.recipe} - {row.instruction}")
    save_calendar(Path("cal.ics"), timetable)

