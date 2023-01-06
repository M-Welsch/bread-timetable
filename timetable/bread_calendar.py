from datetime import timedelta
from pathlib import Path

import pandas as pd
from icalendar import Calendar, Event, vText
from recipe import recipes_new, Recipes


def save_calendar(output_file: Path, timetable: pd.DataFrame):
    cal = Calendar()
    for index, row in timetable.iterrows():
        event = Event()
        event.add('summary', f"{row.recipe}: {row.instruction}")
        event.add('dtstart', row.time)
        event.add('dtend', row.time + timedelta(minutes=30))
        cal.add_component(event)
    with open(output_file, 'wb') as f:
        f.write(cal.to_ical())


def create_calendar_new(timetable: pd.DataFrame) -> bytes:
    cal = Calendar()
    for index, row in timetable.iterrows():
        for rec in recipes_new.keys():
            if str(rec) == str(row.recipe_id):
                recipe = recipes_new[rec]
        if "WARTEN" not in row.step_kind.value:
            event = Event()
            event.add('summary', f"{row.recipe}: {row.instruction}")
            event.add('dtstart', row.time)
            event.add('dtend', row.time + row.duration)
            cal.add_component(event)
    return cal.to_ical()
