
class StudentNode:
    """A node in the Binary Search Tree (BST)"""
    def __init__(self, student_id, name, gpa):
        self.student_id = student_id
        self.name = name
        self.gpa = gpa
        self.left = None
        self.right = None