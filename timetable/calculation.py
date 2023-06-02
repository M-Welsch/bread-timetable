from datetime import datetime, timedelta

import pandas as pd

from timetable.recipe import Recipes, recipes, StepKind, Step


class RecipeError(Exception):
    pass


def compose_ingredients(step: Step, multiplier: float) -> str:
    if step.ingredients is not None:
        return ", ".join([f"{ing.amount * multiplier}{ing.unit} {ing.name}" for ing in step.ingredients])
    else:
        return ""


def create_timetable(recipe_name: Recipes, in_oven_time: datetime, multiplier: float = 1) -> pd.DataFrame:
    steps = recipes[recipe_name]
    baking_step = steps.pop()
    if not baking_step.kind == StepKind.BACKEN:
        raise RecipeError(f"the last step for any recipe shall be BACKEN. Adjust {recipe_name}")
    table = pd.DataFrame({
        "time": [in_oven_time+baking_step.duration, in_oven_time],
        "instruction": ["Fertig", baking_step.instructions],
        "ingredients": ["",""],
        "recipe": [recipe_name.value.name, recipe_name.value.name],
        "recipe_id": [recipe_name, recipe_name],
        "step_kind": [StepKind.WARTEN, baking_step.kind],
        "duration": [timedelta(minutes=1), baking_step.duration]
    })
    for step in reversed(steps):
        step_beginning_time = table.iloc[-1]["time"] - step.duration
        ingredients = compose_ingredients(step, multiplier)
        table = pd.concat([table, pd.DataFrame({
            "time": [step_beginning_time],
            "instruction": [step.instructions],
            "ingredients": [ingredients],
            "recipe": [recipe_name.value.name],
            "recipe_id": recipe_name,
            "step_kind": step.kind,
            "duration": step.duration
        })])
    return table
