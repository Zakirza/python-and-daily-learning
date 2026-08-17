class father:
    father_name = "John"

    def show_father_name(self):
        print(self.father_name)

class mother:
    mother_name = "Jane"

    def show_mother_name(self):
        print(self.mother_name)

class child(father, mother):
    child_name = ""

    def show_child_name(self):
        print(self.child_name)

c1=child()
c1.father_name="Mike"
c1.mother_name="Mary"
c1.child_name="Tom"

c1.show_father_name()
c1.show_mother_name()
c1.show_child_name()
