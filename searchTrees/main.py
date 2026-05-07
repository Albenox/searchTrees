# main.py
# Tests of the Course Schedule Trees Project.

from schedule import Schedule


def main():
    print("File Test")
    print()

    # Create the Schedule object.
    schedule = Schedule()

    # Load the CSV file.
    schedule.load_from_csv("courses_2023.csv")

    # Display the number of records found.
    print("Total records loaded:", schedule.get_count())


if __name__ == "__main__":
    main()