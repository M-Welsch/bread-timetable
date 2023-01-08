from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List, Dict

import pandas as pd

from timetable.bread_calendar import create_calendar
from timetable.pdf_creator import create_pdf
from timetable.recipe import Recipes, timetable_for_recipe, total_ingredients_for_recipe

in_oven_times = {
    Recipes.Haferbrot_2kg: datetime(2023, 1, 14, 13)
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
        BakingPlanUnit(Recipes.DinkelQuarkBrot_2kg, in_oven_times[Recipes.Haferbrot_2kg]),
        BakingPlanUnit(Recipes.Haferbrot_1kg, in_oven_times[Recipes.Haferbrot_2kg], multiplier=2),
        #BakingPlanUnit(Recipes.RoggenvollkornbrotMitRoestbrot_per_1kg, in_oven_times[Recipes.Haferbrot_2kg], multiplier=2),
        BakingPlanUnit(Recipes.RustikalesMischbrot, in_oven_times[Recipes.Haferbrot_2kg], multiplier=2),
        BakingPlanUnit(Recipes.Holzofen, in_oven_times[Recipes.Haferbrot_2kg])
    ]
    timetable = pd.concat(
        [timetable_for_recipe(bread.recipe_name, bread.in_oven_time, bread.multiplier) for bread in baking_plan]
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

    print("\nTotal Ingredients:")
    for ingredient, amount in total_ingredients(baking_plan).items():
        print(f"{amount} {ingredient}")
    create_pdf(baking_plan, timetable, total_ingredients(baking_plan))


if __name__ == "__main__":
    main()
