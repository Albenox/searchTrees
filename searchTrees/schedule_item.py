# schedule_item.py
# Contains the ScheduleItem class.

from dataclasses import dataclass


@dataclass
class ScheduleItem:
    subject: str
    catalog: str
    section: str