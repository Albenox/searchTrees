# main.py
# Tests of the Course Schedule Trees Project.

from schedule import Schedule


def display_menu():
    print()
    print("Course Schedule Menu")
    print("--------------------")
    print("1. Display first courses")
    print("2. Search by course section")
    print("3. Search by subject")
    print("4. Search by subject and catalog")
    print("5. Search by instructor")
    print("6. Display tree heights")
    print("7. Exit")


def main():
    print("Course Schedule Tree System")
    print("---------------------------")

    # Create both schedules.
    bst_schedule = Schedule("bst")
    avl_schedule = Schedule("avl")

    # Load the same CSV file into both schedules.
    bst_schedule.load_from_csv("courses_2023.csv")
    avl_schedule.load_from_csv("courses_2023.csv")

    print("BST records loaded:", bst_schedule.get_count())
    print("AVL records loaded:", avl_schedule.get_count())

    choice = ""

    while choice != "7":
        display_menu()
        choice = input("Enter your choice: ")

        print()

        if choice == "1":
            print("First 10 Courses")
            print("----------------")
            avl_schedule.print_first_items(10)

        elif choice == "2":
            subject = input("Enter subject: ")
            catalog = input("Enter catalog number: ")
            section = input("Enter section: ")

            result = avl_schedule.search_course(subject, catalog, section)

            if result is not None:
                print()
                print("Course found:")
                print(result)
            else:
                print()
                print("Course not found.")

        elif choice == "3":
            subject = input("Enter subject: ")

            results = avl_schedule.search_by_subject(subject)

            print()
            print("Courses found:", len(results))

            for item in results:
                print(item)

        elif choice == "4":
            subject = input("Enter subject: ")
            catalog = input("Enter catalog number: ")

            results = avl_schedule.search_by_subject_catalog(subject, catalog)

            print()
            print("Courses found:", len(results))

            for item in results:
                print(item)

        elif choice == "5":
            instructor = input("Enter instructor name: ")

            results = avl_schedule.search_by_instructor(instructor)

            print()
            print("Courses found:", len(results))

            for item in results:
                print(item)

        elif choice == "6":
            print("BST Height:", bst_schedule.get_height())
            print("AVL Height:", avl_schedule.get_height())

        elif choice == "7":
            print("Goodbye.")

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()