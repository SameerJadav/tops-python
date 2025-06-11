# Write Python programs to demonstrate different types of inheritance (single, multiple, multilevel, etc.)


class Grandparent:
    def dispaly_grandparent(self):
        print("Grandparent")


class ParentA(Grandparent):  # Single inheritance from Grandparent
    def display_parent_a(self):
        print("Parent A")


class ParentB:
    def display_parent_b(self):
        print("Parent B")


class Child(ParentA, ParentB):  # Multiple inheritance from ParentA and ParentB
    def display_child(self):
        print("Child")


class Grandchild(Child):  # Multilevel inheritance from Child
    def display_grandchild(self):
        print("Grandchild")


class SiblingA(ParentA):  # Hierarchical inheritance from ParentA
    def display_sibling_a(self):
        print("Sibling A")


class SiblingB(ParentA):  # Another branch of hierarchical inheritance from ParentA
    def display_sibling_b(self):
        print("Sibling B")
