from datetime import timedelta
from pathlib import Path

import pandas as pd
from icalendar import Calendar, Event, vText
from recipe import recipes, Recipes


def create_calendar(timetable: pd.DataFrame) -> bytes:
    cal = Calendar()
    for index, row in timetable.iterrows():
        for rec in recipes.keys():
            if str(rec) == str(row.recipe_id):
                recipe = recipes[rec]
        if "WARTEN" not in row.step_kind.value:
            event = Event()
            event.add('summary', f"{row.recipe}: {row.instruction}")
            event.add('dtstart', row.time)
            event.add('duration', row.duration)
            event.add('comment', row.ingredients)
            cal.add_component(event)
    return cal.to_ical()
