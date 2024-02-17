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
    Auffrischbrot = RecipeData("Auffrischbrot", "http://")
    Auffrischbrot_per_1gASG = RecipeData("Auffrischbrot", "https://brotpoet.de/2017/11/30/auffrischbrot-nach-dietmar-kappl/")
    SauerteigBroetchen = RecipeData("Sauerteigbrötchen", "http://")
    RoggenvollkornbrotMitRoestbrot_per_1kg = RecipeData("Roggenvollkornbrot mit Röstbrot", "http://")
    RoggenvollkornbrotMitRoestbrot_per_2kg = RecipeData("Roggenvollkornbrot mit Röstbrot", "http://")
    RustikalesMischbrot = RecipeData("Rustikales Mischbrot", "https://www.ploetzblog.de/2021/02/20/rustikales-mischbrot/")
    SkaneKavring = RecipeData("Skane Kavring", "siehe Rolands Rezept Buch")
    Treberbrot = RecipeData("Treberbrot", "https://www.ploetzblog.de/2018/09/29/aarauer-treberbrot/"),
    LeserwunschRustikalesBauernbrot = RecipeData("Leserwunsch: Rustikales Bauernbrot", "https://www.ploetzblog.de/2013/04/27/leserwunsch-rustikales-bauernbrot/")
    VeganesLaugengebaeck = RecipeData("Veganes Laugengebäck pro Stück (ca. 100g)", "https://www.ploetzblog.de/rezepte/veganes-laugengebaeck/id=61d41a8154477a2938bc6e70")
    Pizzateig = RecipeData("Pizzateig", "http://www.perfekte-pizza.de/perfekter-pizzateig/")
    RoggenvollkornKastenbrot = RecipeData("Roggenvollkorn Kastenbrot", "Brotbackbuch, Seite 54")
    Stockbrot = RecipeData("Stockbrot", "https://www.ploetzblog.de/rezepte/stockbrot/id=6253fc47194ceb174cdd0e84")
    Krapfen = RecipeData("Krapfen", "Buch von Jo Semola")
    Checker = RecipeData("Checker", "This is only for unit testing. Don't bake this.")
    Checker2 = RecipeData("Checker2", "This is only for unit testing. Also don't bake this.")


class StepKind(Enum):
    VERARBEITUNG: str = "VERARBEITUNG"
    WARTEN: str = "WARTEN"
    BACKEN: str = "BACKEN"


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
    Recipes.Krapfen: [
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=20), instructions="Alle Zutaten 10-12 Minuten zu einem glatten Teig verkneten", ingredients=[
            Ingredient(16.25, "g", "Vollmilch"),
            Ingredient(33.125, "g", "Weizenmehl Type 550"),
            Ingredient(1.25, "g", "Zucker"),
            Ingredient(1.125, "g", "Hefe"),
            Ingredient(3.75, "g", "Butter"),
            Ingredient(0.5626, "g", "Salz"),
            Ingredient(1, "g", "Mark einer Vanilleschote"),
            Ingredient(0.25, "g", "Eigelb"),
            Ingredient(3.125, "g", "Anstellgut (Optional)"),
            Ingredient(5/16, "g", "Backmalz (aktiv) (optional)")
        ]),
        Step(kind=StepKind.WARTEN, duration=timedelta(minutes=30), instructions="30 Minuten bei Raumtemperatur ruhen lassen"),
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=15), instructions="In Portionen à 60g teilen. Die Teiglinge rund formen"),
        Step(kind=StepKind.WARTEN, duration=timedelta(hours=4), instructions="mit Schluss nach unten in einem leicht bemehlten Tuch 4 Stunden bei Raumtemperatur ruhen lassen"),
        Step(kind=StepKind.BACKEN, duration=timedelta(minutes=10), instructions="In eine Pfanne mit hohem Rand oder einer Fritteuse reichlich Öl auf 170-180°C erhitzen. Die aufgegangenen Teiglinge mit dem Schluss nach oben in das heiße Öl gleiten lassen und von beiden Seiten je 2-3 Minuten goldgelb frittieren. In Portionen frittieren, damit die Teiglinge sich nicht berühren und das Öl nicht zu stark abkühlt")
    ],
    Recipes.Stockbrot: [
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=10), instructions="Vorteig miaschen", ingredients=[
            Ingredient(5.8, "g", "Weizenvollkornmehl"),
            Ingredient(5.8, "g", "Wasser"),
            Ingredient(0.006, "g", "Hefe")
        ]),
        Step(kind=StepKind.WARTEN, duration=timedelta(hours=20)),
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=15), instructions="Kneten", ingredients=[
            Ingredient(0.46, "g", "Salz"),
            Ingredient(1, "g", "Estragon Majoran Thymian (Menge nach Gefühl)"),
            Ingredient(8.7*0.96, "g", "Wasser (15°C)"),
            Ingredient(0.46, "g", "Sonnenblumenöl"),
            Ingredient(16.2, "g", "Weizenmehl Type 550"),
            Ingredient(2.3, "g", "altes Weizenanstellgut TA200 (weich)"),
            Ingredient(11.6, "g", "Vorteig"),
            Ingredient(0.23, "g", "Hefe")
        ]),
        Step(kind=StepKind.WARTEN, duration=timedelta(hours=14), instructions="bei 5°C 12-24h reifen lassen"),
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=20), instructions="Teiglinge zu je 40g abstechen, in ca. 30cm lange Stränge mit viel Mehl ausrollen. Teiglinge in Mehl wälzen, auf ein gut bemehltes Blech setzen"),
        Step(kind=StepKind.WARTEN, duration=timedelta(hours=10), instructions="2-10h bei 5°C reifen lassen"),
        Step(kind=StepKind.BACKEN, duration=timedelta(minutes=5), instructions="knapp über Flamme 5min backen")
    ],
    Recipes.Pizzateig: [
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=10), instructions="Rühren bis eine Masse entsteht, die von der Konsistenz eher an Pfannkuchenteig als an Pizzateig erinnert", ingredients=[
            Ingredient(600, "g", "Weizenmehl Type 405"),
            Ingredient(625, "g", "Wasser (kalt)"),
            Ingredient(10, "g", "Hefe"),
            Ingredient(40, "g", "Salz")
        ]),
        Step(kind=StepKind.WARTEN, duration=timedelta(minutes=20), instructions="Abdecken und 20 min warten"),
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=4), instructions="Rühren"),
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=5), instructions="restliches Mehl in ca. 100g Portionen einkneten", ingredients=[
            Ingredient(400, "g", "Weizenmehl Type 405")
        ]),
        Step(kind=StepKind.WARTEN, duration=timedelta(minutes=20), instructions="Abdecken und 20 min warten"),
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=20), instructions="Teig in ca. 270g große Stücke aufteilen, Rundwirken, dann in Kühlschrank"),
        Step(kind=StepKind.WARTEN, duration=timedelta(hours=24)),
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=5), instructions="Pizza machen"),
        Step(kind=StepKind.BACKEN, duration=timedelta(minutes=5))
    ],
    Recipes.VeganesLaugengebaeck: [
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=10), instructions="Vorteig machen. Teigtemperatur 18°C", ingredients=[
            Ingredient(15, "g", "Wasser 15°C"),
            Ingredient(6.1, "g", "Dinkelvollkornmehl"),
            Ingredient(6.1, "g", "Weizenvollkornmehl"),
            Ingredient(3.1, "g", "Roggenmehl Type 1150"),
            Ingredient(0.31, "g", "Hefe")
        ]),
        Step(kind=StepKind.WARTEN, duration=timedelta(hours=12), instructions="bei 5°C reifen lassen"),
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=15), instructions="Zu einem Teig vermischen, Teigtemperatu etwa 22°C", ingredients=[
            Ingredient(1.2, "g", "Salz"),
            Ingredient(18, "g", "Wasser (20°C)"),
            Ingredient(3.1, "g", "Sonnenblumenöl"),
            Ingredient(43, "g", "Weizenmehl Type 550"),
            Ingredient(3.1, "g", "Sauerteigpulver"),
            Ingredient(0.31, "g", "Hefe")
        ]),
        Step(StepKind.WARTEN, duration=timedelta(hours=1), instructions="bei 20°C reifen lassen"),
        Step(StepKind.VERARBEITUNG, duration=timedelta(minutes=15), instructions="Teiglinge zu je 100g abstechen, straff rundschleifen, dann 15min mit Schluss nach unten auf unbemehlter Arbeitsfläche zugedeckt entspannen lassen"),
        Step(StepKind.WARTEN, duration=timedelta(minutes=15)),
        Step(StepKind.VERARBEITUNG, duration=timedelta(minutes=15), instructions="Formen"),
        Step(StepKind.WARTEN, duration=timedelta(hours=1)),
        Step(StepKind.WARTEN, duration=timedelta(minutes=15), instructions="offen anhauten lassen"),
        Step(StepKind.VERARBEITUNG, duration=timedelta(minutes=15), instructions="laugen, mit Salz bestreuen"),
        Step(StepKind.BACKEN, duration=timedelta(minutes=12), instructions="Backen")
    ],
    Recipes.SauerteigBroetchen: [
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(hours=3, minutes=30), instructions="Sauerteig machen", ingredients=[
            Ingredient(20, "g", "Anstellgut Weizen"),
            Ingredient(25, "g", "Weizenmehl Type 550"),
            Ingredient(20, "g", "Wasser")
        ])  # to be finished
    ],
    Recipes.LeserwunschRustikalesBauernbrot: [
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=5), instructions="Sauerteig machen", ingredients=[
            Ingredient(100, "g", "Roggenvollkornmehl"),
            Ingredient(50, "g", "Roggenmehl Type 1150"),
            Ingredient(150, "g", "Wasser (40°C)"),
            Ingredient(15, "g", "Anstellgut (Roggen)")
        ]),
        Step(kind=StepKind.WARTEN, duration=timedelta(hours=20)),
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=15), instructions="Alle Zutaten 5 Minuten auf niedrigster Stufe und weitere 2 Minuten auf zweiter Stufe zu einem leicht klebenden Teig verarbeiten (Teigtemperatur ca. 28°C)", ingredients=[
            Ingredient(315, "g", "Sauerteig"),
            Ingredient(300, "g", "Roggenmehl Type 1150"),
            Ingredient(100, "g", "Weizenmehl Type 1050"),
            Ingredient(50, "g", "Weizenvollkornmehl"),
            Ingredient(175, "g", "Wasser (50°C)"),
            Ingredient(9, "g", "Salz")
        ]),
        Step(kind=StepKind.WARTEN, duration=timedelta(minutes=45)),
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=2), instructions="Ausstoßen"),
        Step(kind=StepKind.WARTEN, duration=timedelta(minutes=45)),
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=5), instructions="Rundwirken und in Gärkorb rein"),
        Step(kind=StepKind.WARTEN, duration=timedelta(minutes=45)),
        Step(kind=StepKind.BACKEN, duration=timedelta(minutes=45), instructions="Bei 250°C fallend auf 220°C mit Schluss nach oben 50 Minuten mit Dampf backen")
    ],
    Recipes.Treberbrot: [
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=5), instructions="Weizensauer machen", ingredients=[
            Ingredient(100, "g", "Weizenmehl Type 550"),
            Ingredient(100, "g", "Wasser 45°C"),
            Ingredient(10, "g", "Anstellgut (Weizen)")
        ]),
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=5), instructions="Roggensauer machen", ingredients=[
            Ingredient(100, "g", "Roggenmehl Type 997"),
            Ingredient(100, "g", "Wasser 45°C"),
            Ingredient(10, "g", "Anstellgut (Roggen)")
        ]),
        Step(kind=StepKind.WARTEN, duration=timedelta(hours=14)),
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=5), instructions="Autolyseteig machen", ingredients=[
            Ingredient(600, "g", "Weizenmehl Type 550"),
            Ingredient(400, "g", "Wasser 30°C"),
        ]),
        Step(kind=StepKind.WARTEN, duration=timedelta(minutes=30)),
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=15), instructions="Hauptteig machen Schritt 1. 5 Minuten auf erster und 5 Minuten auf zweiter Stufe verkneten", ingredients=[
            Ingredient(0, "", "Alle Vorteige"),
            Ingredient(190, "g", "Weizenvollkornmehl"),
            Ingredient(20, "g", "Salz")
        ]),
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=2), instructions="Treber 1-2 Minuten einkneten", ingredients=[
            Ingredient(250, "g", "Treber")
        ]),
        Step(kind=StepKind.WARTEN, duration=timedelta(minutes=30)),
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=1), instructions="Dehnen und falten"),
        Step(kind=StepKind.WARTEN, duration=timedelta(minutes=30)),
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=1), instructions="Dehnen und falten"),
        Step(kind=StepKind.WARTEN, duration=timedelta(minutes=30)),
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=1), instructions="Dehnen und falten"),
        Step(kind=StepKind.WARTEN, duration=timedelta(minutes=30)),
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=1), instructions="Dehnen und falten"),
        Step(kind=StepKind.WARTEN, duration=timedelta(minutes=30)),
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=1), instructions="Dehnen und falten"),
        Step(kind=StepKind.WARTEN, duration=timedelta(minutes=30)),
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=5), instructions="Langwirken, in Gärkörbe rein, abdecken und 20h bei 5°C reifen lassen, dann einschneiden und backen"),
        Step(kind=StepKind.WARTEN, duration=timedelta(hours=24)),
    ],
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
            Ingredient(2, "g", "Anstellgut (Roggen)")
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
        ]),
        Step(kind=StepKind.WARTEN, duration=timedelta(minutes=90), instructions="Teig direkt in die Kastenform und 1,5h warten"),
    ],
    Recipes.DinkelQuarkBrot_2kg: [
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=5), instructions="Sauerteig machen", ingredients=[
            Ingredient(100, "g", "Roggenmehl Type 1150"),
            Ingredient(100, "ml", "Wasser"),
            Ingredient(10, "g", "Anstellgut (Roggen)")
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
        Step(kind=StepKind.WARTEN, duration=timedelta(minutes=45), instructions="Garen lassen"),
        Step(kind=StepKind.BACKEN, duration=timedelta(minutes=60), instructions="Backen"),
    ],
    Recipes.DinkelQuarkBrot_800g: [
        Step(kind=StepKind.VERARBEITUNG, duration=timedelta(minutes=5), instructions="Sauerteig machen", ingredients=[
            Ingredient(50, "g", "Roggenmehl Type 1150"),
            Ingredient(50, "ml", "Wasser"),
            Ingredient(5, "g", "Anstellgut (Roggen)")
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
        Step(kind=StepKind.WARTEN, duration=timedelta(minutes=45), instructions="Garen lassen"),
        Step(kind=StepKind.BACKEN, duration=timedelta(minutes=60), instructions="Backen")
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
        Step(StepKind.WARTEN, timedelta(minutes=60)),
        Step(StepKind.BACKEN, timedelta(minutes=60), instructions="Backen bei viel Grad")
    ],
    Recipes.RoggenvollkornbrotMitRoestbrot_per_1kg: [
        Step(StepKind.VERARBEITUNG, timedelta(minutes=5), "Sauerteig machen", [
            Ingredient(200, "g", "Roggenvollkornmehl"),
            Ingredient(200, "ml", "Wasser (50°)"),
            Ingredient(40, "g", "Anstellgut (Roggen)"),
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
            Ingredient(280, "g", "Roggenvollkornmehl"),
            Ingredient(110, "ml", "Wasser (100°C)"),
        ]),
        Step(StepKind.WARTEN, timedelta(minutes=30)),
        Step(StepKind.VERARBEITUNG, timedelta(minutes=10), "Rundwirken und in Gärkorb rein"),
        Step(StepKind.WARTEN, timedelta(minutes=90)),
        Step(StepKind.BACKEN, timedelta(minutes=60), instructions="Backen")
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
        Step(StepKind.WARTEN, timedelta(minutes=60)),
        Step(StepKind.BACKEN, timedelta(minutes=120))
    ],
    Recipes.RustikalesMischbrot: [
        Step(StepKind.VERARBEITUNG, timedelta(minutes=10), "Sauerteig machen", [
            Ingredient(400, "g", "Roggenmehl Type 1150"),
            Ingredient(400, "ml", "Wasser (50°C)"),
            Ingredient(80, "g", "Anstellgut (Roggen)"),
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
        Step(StepKind.BACKEN, timedelta(hours=1))
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
        Step(StepKind.WARTEN, timedelta(hours=1)),
        Step(StepKind.BACKEN, timedelta(minutes=45), instructions="Backen")
    ],
    Recipes.Checker: [
        Step(StepKind.VERARBEITUNG, duration=timedelta(hours=1), instructions="Step1", ingredients=[
            Ingredient(1, "g", "Boring one")
        ]),
        Step(StepKind.WARTEN, duration=timedelta(hours=1)),
        Step(StepKind.VERARBEITUNG, timedelta(minutes=30), instructions="Step2", ingredients=[
            Ingredient(2, "g", "another boring thing")
        ]),
        Step(StepKind.WARTEN, duration=timedelta(minutes=30)),
        Step(StepKind.BACKEN, timedelta(minutes=45))
    ]
}


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
