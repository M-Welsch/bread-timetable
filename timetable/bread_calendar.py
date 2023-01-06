from datetime import timedelta
from pathlib import Path

import pandas as pd
from icalendar import Calendar, Event, vText


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
