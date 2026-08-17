class student:
    def __init__(self,name,rollno,gender):
        self.name=name
        self.rollno=rollno
        self.gender=gender  

    def display(self):
        print(f"student name = {self.name}")
        print(f"student rollno = {self.rollno}")
        print(f"student gender = {self.gender}")

    @classmethod
    def create_student_using_parm(cls,name,rollno,gender):
        obj=cls(name,rollno,gender)
        return obj

    @classmethod
    def create_student_using_file(cls,filename):
        f=open(filename,'r')
        student_data=f.read()
        name,rollno,gender=student_data.split()
        f.close()
        obj=cls(name,rollno,gender)
        return obj

s1=student.create_student_using_parm("zakir",786,"male")
s1.display()
print("------------------")
s2=student.create_student_using_file("filename.txt")
s2.display()
