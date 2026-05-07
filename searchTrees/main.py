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
    print("7. Switch tree type")
    print("8. Exit")


def print_results(results):
    # Prints the number of results and each course found.

    print()
    print("Courses found:", len(results))

    if len(results) == 0:
        print("No matching courses were found.")
    else:
        for item in results:
            print(item)


def main():
    print("Course Schedule Tree System")
    print("---------------------------")

    # Create both schedules.
    bst_schedule = Schedule("bst")
    avl_schedule = Schedule("avl")

    # Load the same CSV file into both schedules.
    bst_schedule.load_from_csv("courses_2023.csv")
    avl_schedule.load_from_csv("courses_2023.csv")

    # Start using AVL by default.
    current_schedule = avl_schedule
    current_tree_name = "AVL"

    print("BST records loaded:", bst_schedule.get_count())
    print("AVL records loaded:", avl_schedule.get_count())

    choice = ""

    while choice != "8":
        print()
        print("Current Tree:", current_tree_name)

        display_menu()

        choice = input("Enter your choice: ")

        print()

        if choice == "1":
            print("First 10 Courses")
            print("----------------")
            current_schedule.print_first_items(10)

        elif choice == "2":
            subject = input("Enter subject: ")
            catalog = input("Enter catalog number: ")
            section = input("Enter section: ")

            result = current_schedule.search_course(subject, catalog, section)

            if result is not None:
                print()
                print("Course found:")
                print(result)
            else:
                print()
                print("Course not found.")

        elif choice == "3":
            subject = input("Enter subject: ")
            results = current_schedule.search_by_subject(subject)
            print_results(results)

        elif choice == "4":
            subject = input("Enter subject: ")
            catalog = input("Enter catalog number: ")

            results = current_schedule.search_by_subject_catalog(subject, catalog)

            print_results(results)

        elif choice == "5":
            instructor = input("Enter instructor name: ")

            results = current_schedule.search_by_instructor(instructor)

            print_results(results)

        elif choice == "6":
            print("BST Height:", bst_schedule.get_height())
            print("AVL Height:", avl_schedule.get_height())

        elif choice == "7":
            # Switch between BST and AVL trees.

            if current_schedule == avl_schedule:
                current_schedule = bst_schedule
                current_tree_name = "BST"
            else:
                current_schedule = avl_schedule
                current_tree_name = "AVL"

            print("Switched to", current_tree_name)

        elif choice == "8":
            print("Goodbye.")

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()