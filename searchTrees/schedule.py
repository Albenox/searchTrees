# schedule.py
# Contains the Schedule class.

import csv
from schedule_item import ScheduleItem


class Schedule:
    def __init__(self):
        # Stores all ScheduleItem objects.
        self.items = []

    def load_from_csv(self, filename):
        # Opens the CSV file and loads course data.

        with open(filename, "r", encoding="utf-8-sig", newline="") as csv_file:
            reader = csv.DictReader(csv_file)

            # Loop through every row in the CSV file.
            for row in reader:

                # Create a ScheduleItem object from the row data.
                item = ScheduleItem(
                    subject=row["Subject"].strip(),
                    catalog=row["Catalog"].strip(),
                    section=row["Section"].strip(),
                    component=row["Component"].strip(),
                    instructor=row["Instructor"].strip()
                )

                # Store the object in the list.
                self.items.append(item)

    def get_count(self):
        # Returns the total number of records loaded.
        return len(self.items)

    def print_first_items(self, amount=10):
        # Prints a small number of schedule items.

        for item in self.items[:amount]:
            print(item)