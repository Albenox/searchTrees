# schedule.py
# Contains the Schedule class.

import csv
from schedule_item import ScheduleItem
from search_trees import BSTMap


class Schedule:
    def __init__(self):
        # Stores all ScheduleItem objects inside a binary search tree.
        self.items = BSTMap()
        self.record_count = 0

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

                # Use the course key to insert the item into the tree.
                self.items.insert(item.get_key(), item)
                self.record_count += 1

    def get_count(self):
        # Returns the total number of records loaded.
        return self.record_count

    def print_first_items(self, amount=10):
        # Prints a small number of schedule items in sorted order.

        count = 0

        for key, item in self.items.inorder_items():
            if count >= amount:
                break

            print(item)
            count += 1

    def search_course(self, subject, catalog, section):
        # Creates a key and searches the BST.

        key = f"{subject}-{catalog}-{section}"

        return self.items.search(key)