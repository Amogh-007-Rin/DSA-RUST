from StudentManagement import StudentBST
from Main import insert_sample_students

# Initialize BST and insert sample students

# Define test function
def test_search_by_name():
    # Test case 1: Search for a name with a single match
    name1 = "Ethan Hunt"
    result = bst.search_by_name(name1)
    result_formatted = [(student.student_id, student.name, student.gpa) for student in result]
    print(f"Matching students for '{name1}': {result_formatted}")  # Expected Output: [(101, "Ethan Hunt", 3.2)]

    # Test case 2: Search for a name with multiple matches
    name2 = "Alice Johnson"
    result = bst.search_by_name(name2)
    result_formatted = [(student.student_id, student.name, student.gpa) for student in result]
    # Expected: e.g., [(103, "Alice Johnson", 3.3), (105, "Alice Johnson", 3.5)]
    print(f"Matching students for '{name2}': {result_formatted}") 

    # Test case 3: Search for a name with no match
    name3 = "Zoe Smith"
    result = bst.search_by_name(name3)
    result_formatted = [(student.student_id, student.name, student.gpa) for student in result]
    print(f"Matching students for '{name3}': {result_formatted}")  # Expected: []

bst = StudentBST()
insert_sample_students(bst)  # This should insert students into the BST

def test_total_student_count():
    # Test case 1: Count students in the full tree
    result = bst.total_student_count()
    print(f"Total student count: {result}")  # Expected Output: 12

    # Test case 2: Inserting a new student and counting again
    bst.insert(116, "Mary Jane", 3.8)
    result = bst.total_student_count()
    print(f"Total student count after adding a new student: {result}")  # Expected Output: 13

    # Test case 3: Count students in an empty tree
    empty_bst = StudentBST()  # Create a new empty BST
    result = empty_bst.total_student_count()
    print(f"Total student count in an empty tree: {result}")  # Expected Output: 0


def test_display_ordered():
    # Test case 1: Display sorted students in the full tree
    print("Test case 1: Display sorted students in the full tree")
    bst.display_ordered()  # Expected Output: 
    # ID: 101, Name: Ethan Hunt, GPA: 3.2
    # ID: 102, Name: Bob Smith, GPA: 3.8
    # ID: 103, Name: Kyle Johnson, GPA: 3.3
    # ID: 104, Name: Hannah Lee, GPA: 3.6
    # ID: 105, Name: Alice Johnson, GPA: 3.5
    # ID: 106, Name: Liam Scott, GPA: 3.75
    # ID: 107, Name: Diana Prince, GPA: 3.7
    # ID: 108, Name: George Miller, GPA: 3.1
    # ID: 109, Name: Jessica Davis, GPA: 3.0
    # ID: 110, Name: Charlie Brown, GPA: 2.9
    # ID: 112, Name: Ian Wright, GPA: 3.4
    # ID: 115, Name: Fiona Clark, GPA: 3.9
    # ID: 116, Name: Mary Jane, GPA: 3.8
    # ID: 117, Name: Amogh Dath, GPA: 5.0

    # Test case 2: Insert a new student and display sorted students
    print("\nTest case 2: Insert a new student and display sorted students")
    bst.insert(100, "Mary Jane", 3.8)
    bst.display_ordered()  # Expected Output: 
    # ID: 100, Name: Mary Jane, GPA: 3.8
    # ID: 101, Name: Ethan Hunt, GPA: 3.2
    # ID: 102, Name: Bob Smith, GPA: 3.8
    # ID: 103, Name: Kyle Johnson, GPA: 3.3
    # ID: 104, Name: Hannah Lee, GPA: 3.6
    # ID: 105, Name: Alice Johnson, GPA: 3.5
    # ID: 106, Name: Liam Scott, GPA: 3.75
    # ID: 107, Name: Diana Prince, GPA: 3.7
    # ID: 108, Name: George Miller, GPA: 3.1
    # ID: 109, Name: Jessica Davis, GPA: 3.0
    # ID: 110, Name: Charlie Brown, GPA: 2.9
    # ID: 112, Name: Ian Wright, GPA: 3.4
    # ID: 115, Name: Fiona Clark, GPA: 3.9
    # ID: 116, Name: Mary Jane, GPA: 3.8
    # ID: 117, Name: Amogh Dath, GPA: 5.0

if __name__ == "__main__":
    test_display_ordered()












