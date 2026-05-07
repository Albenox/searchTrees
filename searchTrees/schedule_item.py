# schedule_item.py
# Contains the ScheduleItem class.

from dataclasses import dataclass


@dataclass
class ScheduleItem:
    subject: str
    catalog: str
    section: str
    component: str
    instructor: str

    def get_key(self):
        # Creates a unique key for the course.
        return f"{self.subject}-{self.catalog}-{self.section}"

    def __str__(self):
        # Controls how the object prints.
        return (
            f"{self.subject} {self.catalog} {self.section} | "
            f"{self.component} | "
            f"{self.instructor}"
        )