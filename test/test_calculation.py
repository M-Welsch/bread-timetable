from datetime import datetime

from timetable.calculation import create_timetable
from timetable.recipe import Recipes


def test_timetable() -> None:
    in_oven_time = datetime(2023, 1, 1, 12)
    table = create_timetable(Recipes.Checker, in_oven_time)
    pass