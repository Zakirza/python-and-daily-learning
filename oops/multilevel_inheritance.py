class grandfather:
    def __init__(self,grandfather_name):
        self.grandfather_name = grandfather_name

    def show_grandfather(self):
        print(f"Grandfather's name is {self.grandfather_name}") 

class father(grandfather):
    def __init__(self, father_name, grandfather_name):
        super().__init__(grandfather_name)
        self.father_name = father_name

    def show_father(self):
        print(f"Father's name is {self.father_name}")

class child(father):
    def __init__(self, child_name, father_name, grandfather_name):
        super().__init__(father_name, grandfather_name)
        self.child_name = child_name

    def show_child(self):
        print(f"Child's name is {self.child_name}")
        self.show_father()
        self.show_grandfather()


c1 = child("Tom", "Mike", "John")
c1.show_child()