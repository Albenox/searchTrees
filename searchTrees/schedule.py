# schedule.py
# Contains the Schedule class.

import csv
from schedule_item import ScheduleItem
from search_trees import BSTMap
from search_trees import AVLTreeMap


class Schedule:
    def __init__(self, tree_type="bst"):
        # Creates either a BST or AVL tree.

        if tree_type.lower() == "avl":
            self.items = AVLTreeMap()
        else:
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
        # Creates a key and searches the tree.

        key = f"{subject}-{catalog}-{section}"

        return self.items.search(key)

    def search_by_subject(self, subject):
        # Searches through the tree and returns all courses with the matching subject.

        results = []

        for key, item in self.items.inorder_items():
            if item.subject.upper() == subject.upper():
                results.append(item)

        return results

    def search_by_subject_catalog(self, subject, catalog):
        # Searches through the tree and returns all courses with the matching subject and catalog number.

        results = []

        for key, item in self.items.inorder_items():
            if item.subject.upper() == subject.upper() and item.catalog == catalog:
                results.append(item)

        return results

    def search_by_instructor(self, instructor):
        # Searches through the tree and returns all courses with the matching instructor.

        results = []

        for key, item in self.items.inorder_items():
            if instructor.upper() in item.instructor.upper():
                results.append(item)

        return results