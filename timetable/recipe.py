from collections import OrderedDict
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, Optional, List

import pandas as pd


@dataclass
class RecipeData:
    name: str
    url: str


class Recipes(Enum):
    Holzofen = RecipeData("Holzofen Vorbereitung", "https://www.backdorf.de/blog/Holzbackofen-richtig-aufheizen-backdorf/")
    DinkelQuarkBrot_2kg = RecipeData("Dinkel-Quark-Brot", "")
    DinkelQuarkBrot_800g = RecipeData("Dinkel-Quark-Brot", "")
    DinkelKastenBrot = RecipeData("Dinkel Kastenbrot", "http://")
    Haferbrot_1kg = RecipeData("Haferbrot pro 1kg", "https://www.ploetzblog.de/2015/09/19/reines-haferflockenbrot/")
    Haferbrot_2kg = RecipeData("Haferbrot 2kg", "https://www.ploetzblog.de/2015/09/19/reines-haferflockenbrot/")
    Haferbrot_3kg = RecipeData("Haferbrot 3kg", "https://www.ploetzblog.de/2015/09/19/reines-haferflockenbrot/")
    Auffrischbrot = RecipeData("Auffrischbrot", "http://")
    Auffrischbrot_per_1gASG = RecipeData("Auffrischbrot", "https://brotpoet.de/2017/11/30/auffrischbrot-nach-dietmar-kappl/")
    SauerteigBroetchen = RecipeData("Sauerteigbrötchen", "http://")
    RoggenvollkornbrotMitRoestbrot_per_1kg = RecipeData("Roggenvollkornbrot mit Röstbrot", "http://")
    RoggenvollkornbrotMitRoestbrot_per_2kg = RecipeData("Roggenvollkornbrot mit Röstbrot", "http://")
    RustikalesMischbrot = RecipeData("Rustikales Mischbrot", "https://www.ploetzblog.de/2021/02/20/rustikales-mischbrot/")
    SkaneKavring = RecipeData("Skane Kavring", "")


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
    Recipes.SkaneKavring: [
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=10), instructions="Kochstück machen", ingredients=[
            Ingredient(95, "g", "Roggenmehl Type 1150"),
            Ingredient(1, "TL", "gemahlener Kreuzkümmel"),
            Ingredient(250, "g", "Wasser"),
            Ingredient(1, "EL", "Salz")
        ]),
        Step(kind=StepKind.WARTEN, duration=timedelta(hours=8)),
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=10), instructions="Sauerteig machen", ingredients=[
            Ingredient(42, "g", "Roggenmehl Type 1150"),
            Ingredient(34, "g", "Wasser (ca. 40°C)"),
            Ingredient(2, "g", "Anstellgut")
        ]),
        Step(kind=StepKind.WARTEN, duration=timedelta(hours=12)),
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=10), instructions="Vorteig machen. 4 Min kneten", ingredients=[
            Ingredient(10, "g", "Hefe"),
            Ingredient(75, "g", "Roggensauerteig"),
            Ingredient(300, "g", "Roggenmehl Type 1150"),
            Ingredient(250, "g", "Wasser"),
        ]),
        Step(kind=StepKind.WARTEN, duration=timedelta(hours=4)),
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=10), instructions="Hauptteig machen. 5 Min langsam kneten", ingredients=[
            Ingredient(10, "g", "Hefe"),
            Ingredient(200, "g", "Zuckerrübensirup"),
            Ingredient(500, "g", "Roggenmehl Type 1150"),
            Ingredient(10, "g", "Flüssiger Butter zum Bestreichen (Mengenangabe willkürlich)"),
        ])
    ],
    Recipes.DinkelQuarkBrot_2kg: [
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=5), instructions="Sauerteig machen", ingredients=[
            Ingredient(100, "g", "Roggenmehl Type 1150"),
            Ingredient(100, "ml", "Wasser"),
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
Recipes.DinkelQuarkBrot_800g: [
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=5), instructions="Sauerteig machen", ingredients=[
            Ingredient(50, "g", "Roggenmehl Type 1150"),
            Ingredient(50, "ml", "Wasser"),
            Ingredient(5, "g", "Anstellgut")
        ]),
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=10), instructions="Kochstück machen", ingredients=[
            Ingredient(95, "g", "Dinkelschrot"),
            Ingredient(230, "ml", "Wasser")
        ]),
        Step(kind=StepKind.WARTEN, duration=timedelta(hours=16)),
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=30), instructions="Hauptteig machen", ingredients=[
            Ingredient(40, "g", "Sesam"),
            Ingredient(50, "g", "Joghurt"),
            Ingredient(280, "g", "Dinkelmehl Type 630"),
            Ingredient(50, "g", "Roggenmehl Type 1150"),
            Ingredient(12, "g", "Salz"),
            Ingredient(8, "g", "Hefe"),
            Ingredient(50, "ml", "Wasser")
        ]),
        Step(kind=StepKind.WARTEN, duration=timedelta(minutes=60)),
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=5), instructions="Rundwirken"),
        Step(kind=StepKind.WARTEN, duration=timedelta(minutes=45), instructions="Garen lassen")
    ],
    Recipes.Haferbrot_1kg: [
        Step(StepKind.VERARBEITUNG, timedelta(minutes=5), "Sauerteig machen", [
            Ingredient(133, "g", "Haferflocken fein"),
            Ingredient(166, "ml", "Wasser (50°C)"),
            Ingredient(26.7, "g", "Anstellgut (Hafer)"),
            Ingredient(3.3, "g", "Salz"),
        ]),
        Step(StepKind.WARTEN, timedelta(hours=8), "Sauerteig reifen lassen"),
        Step(StepKind.VERARBEITUNG, timedelta(minutes=5), "Brühstück machen", [
            Ingredient(133, "g", "Haferflocken kernig"),
            Ingredient(266, "ml", "Wasser"),
            Ingredient(11.3, "g", "Salz"),
        ]),
        Step(StepKind.WARTEN, timedelta(hours=4)),
        Step(StepKind.VERARBEITUNG, timedelta(minutes=20), "Hauptteig machen", [
            Ingredient(400, "g", "Haferflocken kernig"),
            Ingredient(266, "ml", "Wasser, dann 133g Wasser jew. 40°"),
            Ingredient(6.7, "g", "Hefe"),
        ]),
        Step(StepKind.WARTEN, timedelta(minutes=60))
    ],
    Recipes.RoggenvollkornbrotMitRoestbrot_per_1kg: [
        Step(StepKind.VERARBEITUNG, timedelta(minutes=5), "Sauerteig machen", [
            Ingredient(200, "g", "Roggenvollkornmehl"),
            Ingredient(200, "ml", "Wasser (50°)"),
            Ingredient(40, "g", "Anstellgut"),
            Ingredient(4, "g", "Salz"),
        ]),
        Step(StepKind.VERARBEITUNG, timedelta(minutes=5), "Brühstück machen", [
            Ingredient(75, "g", "Röstbrot"),
            Ingredient(7, "g", "Salz"),
            Ingredient(225, "ml", "Wasser (100°C)"),
        ]),
        Step(StepKind.WARTEN, timedelta(hours=12)),
        Step(StepKind.VERARBEITUNG, timedelta(minutes=20), "Hauptteig machen", [
            Ingredient(444, "g", "Sauerteig"),
            Ingredient(307, "g", "Brühstück"),
            Ingredient(560, "g", "Roggenvollkornmehl"),
            Ingredient(220, "ml", "Wasser (100°C)"),
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
    ],
    Recipes.RustikalesMischbrot: [
        Step(StepKind.VERARBEITUNG, timedelta(minutes=10), "Sauerteig machen", [
            Ingredient(400, "g", "Roggenmehl Type 1150"),
            Ingredient(400, "ml", "Wasser (50°C)"),
            Ingredient(80, "g", "Anstellgut"),
            Ingredient(8, "g", "Salz")
        ]),
        Step(StepKind.VERARBEITUNG, timedelta(minutes=10), "Vorteig machen", [
            Ingredient(100, "g", "Dinkelvollkornmehl"),
            Ingredient(50, "ml", "Wasser (kalt)"),
            Ingredient(1, "g", "Hefe")
        ]),
        Step(StepKind.WARTEN, timedelta(hours=16)),
        Step(StepKind.VERARBEITUNG, timedelta(minutes=15), "kneten", [
            Ingredient(460, "g", "Weizenmehl Type 1050"),
            Ingredient(200, "ml", "Wasser (35°C)"),
            Ingredient(13, "g", "Salz")
        ]),
        Step(StepKind.WARTEN, timedelta(minutes=30)),
        Step(StepKind.VERARBEITUNG, timedelta(minutes=2), "Dehnen und Falten"),
        Step(StepKind.WARTEN, timedelta(minutes=30)),
        Step(StepKind.VERARBEITUNG, timedelta(minutes=5), "In Gärkorb"),
        Step(StepKind.WARTEN, timedelta(minutes=75)),
    ],
    Recipes.Auffrischbrot_per_1gASG: [
        Step(StepKind.VERARBEITUNG, timedelta(minutes=5), "Erste Autolyse", [
            Ingredient(1, "g", "Anstellgut (alt)"),
            Ingredient(1.7, "ml", "Wasser")
        ]),
        Step(StepKind.WARTEN, timedelta(minutes=30)),
        Step(StepKind.VERARBEITUNG, timedelta(minutes=2), "Zweite Autolyse", [
            Ingredient(2.7, "g", "Erste Autolyse"),
            Ingredient(2.3, "g", "Mehl (mindestens 30% Weizen/Dinkel)")  # originalls 2.4
        ]),
        Step(StepKind.WARTEN, timedelta(minutes=30)),
        Step(StepKind.VERARBEITUNG, timedelta(minutes=15), "Hauptteig machen", [
            Ingredient(6, "g", "Zweite Autolyse"),
            Ingredient(1/100, "g", "Hefe"),
            Ingredient(6/100, "g", "Salz")
        ]),
        Step(StepKind.WARTEN, timedelta(minutes=40)),
        Step(StepKind.VERARBEITUNG, timedelta(minutes=1), "In Kühlschrank"),
        Step(StepKind.WARTEN, timedelta(hours=13)),
        Step(StepKind.VERARBEITUNG, timedelta(minutes=5), "Rund/Langwirken"),
        Step(StepKind.WARTEN, timedelta(hours=1))
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
            {"time": [step_time], "instruction": [step.instructions], "ingredients": [ingredients], "recipe": [recipe_name.value.name], "recipe_id": recipe_name, "step_kind": step.kind, "duration": step.duration}
        )])
    return df


def total_ingredients_for_recipe(recipe_name: Recipes) -> Dict[str, float]:
    total_ingredients = {}
    for step in recipes[recipe_name]:
        if step.ingredients is None:
            continue
        for ingredient in step.ingredients:
            label = f"{ingredient.unit} {ingredient.name}"
            try:
                total_ingredients[label] += ingredient.amount
            except KeyError:
                total_ingredients[label] = ingredient.amount
    return total_ingredients
