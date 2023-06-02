from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List, Dict

import pandas as pd

from timetable.bread_calendar import create_calendar
from timetable.pdf_creator import create_pdf
from timetable.recipe import Recipes, total_ingredients_for_recipe
from timetable.calculation import create_timetable

in_oven_times = {
    Recipes.Auffrischbrot_per_1gASG: datetime(2023, 6, 3, 13, 30),
    Recipes.LeserwunschRustikalesBauernbrot: datetime(2023, 6, 3, 14, 40),
}


@dataclass
class BakingPlanUnit:
    recipe_name: Recipes
    in_oven_time: datetime
    multiplier: float = 1


def total_ingredients(baking_plan: List[BakingPlanUnit]) -> Dict[str, float]:
    total_ingredients = {}
    for bread in baking_plan:
        current_ingredients = total_ingredients_for_recipe(bread.recipe_name)
        for ingredient, amount in current_ingredients.items():
            current_ingredients[ingredient] *= bread.multiplier
            if ingredient in total_ingredients.keys():
                total_ingredients[ingredient] += current_ingredients[ingredient]
            else:
                total_ingredients[ingredient] = current_ingredients[ingredient]
    return total_ingredients


def main():
    baking_plan = [
        #BakingPlanUnit(Recipes.DinkelQuarkBrot_800g, in_oven_times[Recipes.DinkelQuarkBrot_800g], multiplier=6),
        #BakingPlanUnit(Recipes.Haferbrot_1kg, in_oven_times[Recipes.Haferbrot_2kg], multiplier=3),
        #BakingPlanUnit(Recipes.SkaneKavring, in_oven_times[Recipes.SkaneKavring], multiplier=2),
        #BakingPlanUnit(Recipes.Treberbrot, in_oven_times[Recipes.Treberbrot], multiplier=2),
        #BakingPlanUnit(Recipes.RoggenvollkornbrotMitRoestbrot_per_1kg, in_oven_times[Recipes.Haferbrot_2kg], multiplier=2),
        BakingPlanUnit(Recipes.Auffrischbrot_per_1gASG, in_oven_times[Recipes.Auffrischbrot_per_1gASG], multiplier=500),
        # BakingPlanUnit(Recipes.RustikalesMischbrot, in_oven_times[Recipes.DinkelQuarkBrot_800g], multiplier=2),
        #BakingPlanUnit(Recipes.Holzofen, in_oven_times[Recipes.DinkelQuarkBrot_800g])
        BakingPlanUnit(Recipes.LeserwunschRustikalesBauernbrot, in_oven_times[Recipes.LeserwunschRustikalesBauernbrot], multiplier=2)
    ]
    timetable = pd.concat(
        [create_timetable(bread.recipe_name, bread.in_oven_time, bread.multiplier) for bread in baking_plan]
    )
    timetable.to_pickle("timetable.pkl")

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

    print("\nTotal Ingredients:")
    for ingredient, amount in total_ingredients(baking_plan).items():
        print(f"{amount} {ingredient}")
    create_pdf(baking_plan, timetable, total_ingredients(baking_plan))


if __name__ == "__main__":
    main()
