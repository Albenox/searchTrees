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

    print()
    print("Search Test")
    print("-----------")

    # Search for a specific course.
    result = schedule.search_course("AIR", "154", "01HL")

    if result is not None:
        print("Course found:")
        print(result)
    else:
        print("Course not found")

    print()
    print("Subject Search Test")
    print("-------------------")

    # Search for every course with a matching subject.
    subject_results = schedule.search_by_subject("AIR")

    print("Courses found:", len(subject_results))

    for item in subject_results[:10]:
        print(item)


if __name__ == "__main__":
    main()