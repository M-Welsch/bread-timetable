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


recipes_new = {
    Recipes.DinkelQuarkBrot_2kg: [
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=5), instructions="Sauerteig machen", ingredients=[
            Ingredient(100, "g", "Roggen"),
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
    ]
}

recipes = {
    Recipes.Holzofen: OrderedDict({
        "Abbrandphase: 1/3 Holz in vorderer Hälfte abbrennen. Ofentür in erste Rastung, 30min warten": timedelta(minutes=30),
        "Abbrandphase: weiteres 1/3 Holz auf die Glut, 30min warten": timedelta(minutes=30),
        "Glut überall verteilen, letztes 1/3 Holz drauf, 60min warten, Glut mehrmals aufhacken": timedelta(hours=1),
        "Sauber kehren, Tür zu. Pizza backen. Nach 1h Brot möglich": timedelta(hours=1)
    }),
    Recipes.DinkelQuarkBrot_2kg: OrderedDict(
        {
            "Sauerteig (100g Roggen, 100g Wasser, 10g AG), Kochstück machen (190 Dinkelschrot, 460ml Wasser)": timedelta(minutes=10),
            "Sauerteig, Kochstück reifen lassen": timedelta(hours=16),
            "Hauptteig machen (80g Sesam, 100g Joghurt, 560g Dinkel T630, 100g Roggen, 24g Salz, 16g Hefe, 100g Wasser)": timedelta(minutes=30),
            "Hauptteig gehen lassen 1": timedelta(minutes=60),
            "Rundwirken": timedelta(minutes=5),
            "Garen": timedelta(minutes=45),
        }
    ),
    Recipes.Haferbrot_1kg: OrderedDict(
        {
            "Sauerteig zusammenrühren (133g Haferf. fein, 166g Wasser (50°C), 26,7g AG, 3,3g Salz)": timedelta(minutes=5),
            "Sauerteig reifen lassen": timedelta(hours=8),
            "Brühstück machen (133g Haferfl. kernig, 266g Wasser, 11,3g Salz)": timedelta(minutes=5),
            "Brühstück reifen lassen": timedelta(hours=4),
            "Hauptteig machen (400g Haferfl. kernig, 266g Wasser, dann 133g Wasser jew. 40°, 6,7g Hefe)": timedelta(minutes=20),
            "Garen lassen": timedelta(minutes=60),
        }
    ),
    Recipes.Haferbrot_2kg: OrderedDict(
        {
            f"Sauerteig zusammenrühren ({133*2}g Haferf. fein, {166*2}g Wasser (50°C), {2*26.7}g AG, {2*3.3}g Salz)": timedelta(minutes=5),
            "Sauerteig reifen lassen": timedelta(hours=8),
            f"Brühstück machen ({2*133}g Haferfl. kernig, {2*266}g Wasser, {2*11.3}g Salz)": timedelta(minutes=5),
            "Brühstück reifen lassen": timedelta(hours=4),
            f"Hauptteig machen ({2*400}g Haferfl. kernig, {2*266}g Wasser, dann {2*133}g Wasser jew. 40°, {2*6.7}g Hefe)": timedelta(minutes=20),
            "Garen lassen": timedelta(minutes=60),
        }
    ),
    Recipes.Haferbrot_3kg: OrderedDict(
        {
            f"Sauerteig zusammenrühren ({133*3}g Haferf. fein, {166*3}g Wasser (50°C), {3*26.7}g AG, {3*3.3}g Salz)": timedelta(minutes=5),
            "Sauerteig reifen lassen": timedelta(hours=8),
            f"Brühstück machen ({3*133}g Haferfl. kernig, {3*266}g Wasser, {3*11.3}g Salz)": timedelta(minutes=5),
            "Brühstück reifen lassen": timedelta(hours=4),
            f"Hauptteig machen ({3*400}g Haferfl. kernig, {3*266}g Wasser, dann {3*133}g Wasser jew. 40°, {3*6.7}g Hefe)": timedelta(minutes=20),
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

    }),
    Recipes.RoggenvollkornbrotMitRoestbrot_per_2kg: OrderedDict({
        "Sauerteig und Brühstück machen (ST: 400g RoggenVKMehl, 400g Wasser (50°), 80g ASG, 8g Salz) (BS: 150g Röstbrot, 14g Salz, 450g Wasser (100°)), 12h stehen lassen": timedelta(minutes=10),
        "ST und BS 12h ruhen lassen": timedelta(hours=12),
        "Hauptteig machen (ST, BS, 560g RoggenVKMehl, 220g Wasser (100°)": timedelta(minutes=20),
        "Hauptteig 30min ruhen lassen": timedelta(minutes=30),
        "Im Gärkorb 1,5h reifen lassen": timedelta(minutes=90)
    })
}


def calculate_start_time(steps: List[Step], in_oven_time: datetime) -> datetime:
    total_timedelta = timedelta()
    for td in [step.duration for step in steps]:
        total_timedelta += td
    return in_oven_time - total_timedelta  # - time_for_last_step


def timetable_for_recipe(recipe_name: Recipes, in_oven_time: datetime) -> pd.DataFrame:
    start_time = calculate_start_time(recipes_new[recipe_name], in_oven_time)
    time_elapsed = timedelta()
    step_times = []
    df = pd.DataFrame(
        {"time": [], "instruction": [], "ingredients": [], "recipe": []}
    )
    for step in recipes_new[recipe_name]:
        time_needed = step.duration
        time_elapsed += time_needed
        step_time = start_time + time_elapsed
        step_times.append(step_time-time_needed)
        ingredients = ", ".join([f"{ing.amount}{ing.unit} {ing.name}" for ing in step.ingredients])
        df = pd.concat([df, pd.DataFrame(
            {"time": [step_time], "instruction": [step.instructions], "ingredients": [ingredients], "recipe": [recipe_name]}
        )])


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
