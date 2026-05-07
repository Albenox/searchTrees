# schedule.py
# Contains the Schedule class.

import csv


class Schedule:
    def __init__(self):
        # Keeps track of how many records exist in the CSV file.
        self.record_count = 0

    def load_from_csv(self, filename):
        # Opens the CSV file and counts the number of rows.

        with open(filename, "r", encoding="utf-8-sig", newline="") as csv_file:
            reader = csv.DictReader(csv_file)

            # Loop through every row in the CSV file.
            for row in reader:
                self.record_count += 1

    def get_count(self):
        # Returns the total number of records loaded.
        return self.record_count