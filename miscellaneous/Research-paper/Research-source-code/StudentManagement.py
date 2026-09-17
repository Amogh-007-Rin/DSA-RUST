from Student import StudentNode

class StudentBST:
    """Binary Search Tree for Student Records"""
    def __init__(self):
        self.root = None

    def insert(self, student_id, name, gpa):
        """Insert a student record into the tree """
        new_node = StudentNode(student_id, name, gpa)
        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        while True:
            if student_id < current.student_id:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def search(self, student_id):
        """Search for a student by ID"""
        current = self.root
        while current:
            if current.student_id == student_id:
                return current
            elif student_id < current.student_id:
                current = current.left
            else:
                current = current.right
        return None  # Student not found

  
    
    def locate_student(self, student_id):
        """Searches for a student by performing traversal."""
        return self._search_student(self.root, student_id)

    def _search_student(self, node, student_id):
        """Performs traversal to find the student."""
        if node is None:
            return None  # Not found
    
        if node.student_id == student_id:
            return node  # Found the student
    
        left_result = self._search_student(node.left, student_id)
        if left_result:
            return left_result
    
        return self._search_student(node.right, student_id)  # Continue in right subtree
    
    def _collect_students(self, node, students):
        """Helper function to collect students into a list."""
        if node:
            students.append(node)  # Store node in list
            self._collect_students(node.left, students)
            self._collect_students(node.right, students)
    
    def display_sorted(self):
        """Sorts student records using a simple Bubble Sort approach and displays them."""
        students = []
        self._collect_students(self.root, students)  # Collect student records into a list
        
        # Bubble Sort - inefficient sorting
        n = len(students)
        for i in range(n):
            for j in range(0, n-i-1):
                if students[j].student_id > students[j+1].student_id:
                    students[j], students[j+1] = students[j+1], students[j]  # Swap
        
        # Display sorted students
        for student in students:
            print(f"ID: {student.student_id}, Name: {student.name}, GPA: {student.gpa}")
            
            
     # Student needs to complete these ( Refer to the Assessment Section A1.1 - A1.3)
     # TODO - A.1.1: define search_by_name method and/or any related helper methods
    def search_by_name(self, name):
        """
        Function To search for students by name in the tree.

        Parameters:
        name (str): The name of the student to search for.

        returns:
        list: A list of student names that match the search criteria.
        """
        all_names = []
        def _search(node):
            if node is None:
                return
            # Check if the name matches the current node's name
            if node.name.lower() == name.lower():
                all_names.append(node)

            _search(node.left)
            _search(node.right)

        _search(self.root)
        return all_names
     # TODO - A.1.2: define total_student_count  method and/or any related helper methods
    def total_student_count(self):
        """Function to count the total number of students in the tree.
        
        parameters: None
        
        returns:
        int: The total number of students in the tree.
        """
        def _count(node):
            if node is None:
                return 0
            return 1 + _count(node.left) + _count(node.right)

        return _count(self.root)
    
    # TODO - A.1.3: define display_ordered  method and/or any related helper methods
    
    def display_ordered(self):  
        """Function to Sort student records using Merge Sort and displays them."""
        students = []
        self._collect_students(self.root, students)

        sorted_students = self._merge_sort(students)

        for student in sorted_students:
            print(f"ID: {student.student_id}, Name: {student.name}, GPA: {student.gpa}")
    
    def _merge_sort(self, students):
        """ Function to Perform merge sort on a list of students.
        Parameters:
        students (list): The list of students to sort.
        Returns:
        list: The sorted list of students.
        
        """
        if len(students) <= 1:
            return students

        mid = len(students) // 2
        left_half = self._merge_sort(students[:mid])
        right_half = self._merge_sort(students[mid:])

        return self._merge(left_half, right_half)
    
    def _merge(self, left, right):
        """ Function to Merge two sorted lists of students.
        Parameters:
        left (list): The left half of the list to merge.
        right (list): The right half of the list to merge.

        Returns:
        list: The merged sorted list of students.
        """
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i].student_id <= right[j].student_id:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

    # Append remaining elements
        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged



