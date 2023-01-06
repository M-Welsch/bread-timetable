from collections import OrderedDict
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, Optional, List

import pandas as pd


class Recipes(Enum):
    Holzofen = "Holzofen Vorbereitung"
    DinkelQuarkBrot_2kg = "Dinkel-Quark-Brot"
    DinkelKastenBrot = "Dinkel Kastenbrot"
    Haferbrot_1kg = "Haferbrot pro 1kg"
    Haferbrot_2kg = "Haferbrot 2kg"
    Haferbrot_3kg = "Haferbrot 3kg"
    Auffrischbrot = "Auffrischbrot"
    SauerteigBroetchen = "Sauerteigbrötchen"
    RoggenvollkornbrotMitRoestbrot_per_1kg = "Roggenvollkornbrot mit Röstbrot"
    RoggenvollkornbrotMitRoestbrot_per_2kg = "Roggenvollkornbrot mit Röstbrot"


class StepKind(Enum):
    VERARBEITUNG: str = "VERARBEITUNG"
    WARTEN: str = "WARTEN"


@dataclass
class Ingredient:
    amount: float
    unit: str
    name: str


@dataclass
class Step:
    kind: StepKind
    duration: timedelta
    instructions: Optional[str] = None
    ingredients: Optional[List[Ingredient]] = None


recipes = {
    Recipes.DinkelQuarkBrot_2kg: [
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=5), instructions="Sauerteig machen", ingredients=[
            Ingredient(100, "g", "Roggenmehl Type 1150"),
            Ingredient(100, "g", "Wasser"),
            Ingredient(10, "g", "Anstellgut")
        ]),
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=10), instructions="Kochstück machen", ingredients=[
            Ingredient(190, "g", "Dinkelschrot"),
            Ingredient(460, "ml", "Wasser")
        ]),
        Step(kind=StepKind.WARTEN, duration=timedelta(hours=16)),
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=30), instructions="Hauptteig machen", ingredients=[
            Ingredient(80, "g", "Sesam"),
            Ingredient(100, "g", "Joghurt"),
            Ingredient(560, "g", "Dinkelmehl Type 630"),
            Ingredient(100, "g", "Roggenmehl Type 1150"),
            Ingredient(24, "g", "Salz"),
            Ingredient(16, "g", "Hefe"),
            Ingredient(100, "ml", "Wasser")
        ]),
        Step(kind=StepKind.WARTEN, duration=timedelta(minutes=60)),
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=5), instructions="Rundwirken"),
        Step(kind=StepKind.WARTEN, duration=timedelta(minutes=45), instructions="Garen lassen")
    ],
    Recipes.Haferbrot_1kg: [
        Step(StepKind.VERARBEITUNG, timedelta(minutes=5), "Sauerteig machen", [
            Ingredient(133, "g", "Haferflocken fein"),
            Ingredient(166, "g", "Wasser (50°C)"),
            Ingredient(26.7, "g", "Anstellgut"),
            Ingredient(3.3, "g", "Salz"),
        ]),
        Step(StepKind.WARTEN, timedelta(hours=8), "Sauerteig reifen lassen"),
        Step(StepKind.VERARBEITUNG, timedelta(minutes=5), "Brühstück machen", [
            Ingredient(133, "g", "Haferflocken kernig"),
            Ingredient(266, "g", "Wasser"),
            Ingredient(11.3, "g", "Salz"),
        ]),
        Step(StepKind.WARTEN, timedelta(hours=4)),
        Step(StepKind.VERARBEITUNG, timedelta(minutes=20), "Hauptteig machen", [
            Ingredient(400, "g", "Haferflocken kernig"),
            Ingredient(266, "g", "Wasser, dann 133g Wasser jew. 40°"),
            Ingredient(6.7, "g", "Hefe"),
        ]),
        Step(StepKind.WARTEN, timedelta(minutes=60))
    ],
    Recipes.RoggenvollkornbrotMitRoestbrot_per_1kg: [
        Step(StepKind.VERARBEITUNG, timedelta(minutes=5), "Sauerteig machen", [
            Ingredient(200, "g", "Roggenvollkornmehl"),
            Ingredient(200, "g", "Wasser (50°)"),
            Ingredient(40, "g", "Anstellgut"),
            Ingredient(4, "g", "Salz"),
        ]),
        Step(StepKind.VERARBEITUNG, timedelta(minutes=5), "Brühstück machen", [
            Ingredient(75, "g", "Röstbrot"),
            Ingredient(7, "g", "Salz"),
            Ingredient(225, "g", "Wasser (100°C)"),
        ]),
        Step(StepKind.WARTEN, timedelta(hours=12)),
        Step(StepKind.VERARBEITUNG, timedelta(minutes=20), "Hauptteig machen", [
            Ingredient(444, "g", "Sauerteig"),
            Ingredient(307, "g", "Brühstück"),
            Ingredient(560, "g", "Roggenvollkornmehl"),
            Ingredient(220, "g", "Wasser (100°C)"),
        ]),
        Step(StepKind.WARTEN, timedelta(minutes=30)),
        Step(StepKind.VERARBEITUNG, timedelta(minutes=10), "Rundwirken und in Gärkorb rein"),
        Step(StepKind.WARTEN, timedelta(minutes=90))
    ],
    Recipes.Holzofen: [
        Step(StepKind.VERARBEITUNG, timedelta(minutes=5), "In vorderer Hälfte anbrennen, Ofentür in erste Rastung", [
            Ingredient(4, "kg", "Holz, maximal 6cm stark")
        ]),
        Step(StepKind.WARTEN, timedelta(minutes=30)),
        Step(StepKind.VERARBEITUNG, timedelta(minutes=2), "Holz auf die Glut", [
            Ingredient(4, "kg", "Holz, maximal 6cm stark")
        ]),
        Step(StepKind.WARTEN, timedelta(minutes=30)),
        Step(StepKind.VERARBEITUNG, timedelta(minutes=2), "Glut überall verteilen, letztes Drittel Holz drauf, 1h warten und Glut mehrmals aufhacken", [
            Ingredient(4, "kg", "Holz, maximal 6cm stark")
        ]),
        Step(StepKind.WARTEN, timedelta(minutes=60)),
        Step(StepKind.VERARBEITUNG, timedelta(minutes=2), "Sauber kehren, Tür zu"),
        Step(StepKind.WARTEN, timedelta(minutes=60))
    ]
}

recipes_old = {
    Recipes.Holzofen: OrderedDict({
        "Abbrandphase: 1/3 Holz in vorderer Hälfte abbrennen. Ofentür in erste Rastung, 30min warten": timedelta(minutes=30),
        "Abbrandphase: weiteres 1/3 Holz auf die Glut, 30min warten": timedelta(minutes=30),
        "Glut überall verteilen, letztes 1/3 Holz drauf, 60min warten, Glut mehrmals aufhacken": timedelta(hours=1),
        "Sauber kehren, Tür zu. Pizza backen. Nach 1h Brot möglich": timedelta(hours=1)
    }),
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
    Recipes.Auffrischbrot: OrderedDict(
        {
            "Erste Autolyse: 350g AG, 595g Wasser (25°C)": timedelta(minutes=30),
            "Zweite Autolyse: erste Autolyse, 840g Mehl": timedelta(minutes=30),
            "Hauptteig: Zw. Autolyse, 3,5g Hefe, 21g Salz": timedelta(minutes=40),
            "In Kühlschrnak": timedelta(hours=10),
            "Garen lassen": timedelta(minutes=60)
        }
    ),
    Recipes.SauerteigBroetchen: OrderedDict({
        "Sauerteig machen (20g AG, 25g Weizen T550, 20g Wasser), 4h stehen lassen": timedelta(hours=4),
        "Vorteig verrühren (585g Weizen T550, 395g Wasser), 30min stehen lassen": timedelta(minutes=30),
        "Hauptteig (Sauerteig, Vorteig) verkneten, dann 15g Salz dazu, nochmal kneten. 6h ruhen lassen)": timedelta(hours=6),
        "9 Teiglinge formen, 60-90min ruhen lassen. Dann 25min bei 250°C OU Hitze backen": timedelta(minutes=60),

    })
}


def calculate_start_time(steps: List[Step], in_oven_time: datetime) -> datetime:
    total_timedelta = timedelta()
    for td in [step.duration for step in steps]:
        total_timedelta += td
    return in_oven_time - total_timedelta  # - time_for_last_step


def compose_ingredients(step: Step, multiplier: float) -> str:
    if step.ingredients is not None:
        return ", ".join([f"{ing.amount * multiplier}{ing.unit} {ing.name}" for ing in step.ingredients])
    else:
        return ""


def timetable_for_recipe(recipe_name: Recipes, in_oven_time: datetime, multiplier: float = 1) -> pd.DataFrame:
    start_time = calculate_start_time(recipes[recipe_name], in_oven_time)
    time_elapsed = timedelta()
    step_times = []
    df = pd.DataFrame(
        {"time": [], "instruction": [], "ingredients": [], "recipe": []}
    )
    for step in recipes[recipe_name]:
        time_needed = step.duration
        time_elapsed += time_needed
        step_time = start_time + time_elapsed
        step_times.append(step_time-time_needed)
        ingredients = compose_ingredients(step, multiplier)
        df = pd.concat([df, pd.DataFrame(
            {"time": [step_time], "instruction": [step.instructions], "ingredients": [ingredients], "recipe": [recipe_name.value], "recipe_id": recipe_name, "step_kind": step.kind, "duration": step.duration}
        )])
    return df


def total_ingredients_for_recipe(recipe_name: Recipes) -> Dict[str, float]:
    total_ingredients = {}
    for step in recipes[recipe_name]:
        if step.ingredients is None:
            continue
        for ingredient in step.ingredients:
            try:
                total_ingredients[ingredient.name] += ingredient.amount
            except KeyError:
                total_ingredients[ingredient.name] = ingredient.amount
    return total_ingredients
