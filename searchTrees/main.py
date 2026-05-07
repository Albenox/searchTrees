# main.py
# Tests of the Course Schedule Trees Project.

from schedule import Schedule


def main():
    print("BST Test")
    print("--------")

    # Create a BST schedule.
    bst_schedule = Schedule("bst")

    bst_schedule.load_from_csv("courses_2023.csv")

    print("BST records loaded:", bst_schedule.get_count())

    print()
    print("BST Height:", bst_schedule.get_height())

    print()
    print("First 5 BST Courses")
    print("-------------------")

    bst_schedule.print_first_items(5)

    print()
    print("AVL Test")
    print("--------")

    # Create an AVL schedule.
    avl_schedule = Schedule("avl")

    avl_schedule.load_from_csv("courses_2023.csv")

    print("AVL records loaded:", avl_schedule.get_count())

    print()
    print("AVL Height:", avl_schedule.get_height())

    print()
    print("First 5 AVL Courses")
    print("-------------------")

    avl_schedule.print_first_items(5)

    print()
    print("Instructor Search Test")
    print("----------------------")

    instructor_results = avl_schedule.search_by_instructor("Scott")

    print("Courses found:", len(instructor_results))

    for item in instructor_results:
        print(item)


if __name__ == "__main__":
    main()