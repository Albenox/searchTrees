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
    print()

    # Display some of the loaded courses.
    print("First 10 Courses")
    print("----------------")
    schedule.print_first_items(10)


if __name__ == "__main__":
    main()