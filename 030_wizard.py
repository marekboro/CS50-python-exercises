# # 1
# class Student:
#     def __init__(self,name,house):
#         if not name:
#             raise ValueError("missing name")
#         self.name = name
#         self.house = house
        
#     ...

# class Professor:
#     def __init__(self,name,subject):
#         if not name:
#             raise ValueError("missing name")
#         self.name = name
#         self.subject = subject

# 2
class Wizard:
    def __init__(self,name):
        if not name:
            raise ValueError("missing name")
        self.name = name
    def __str__(self):
        return f"{self.name} is a Wizard"

class Student(Wizard):
    def __init__(self,name,house):
        super().__init__(name)
        self.house = house
    def __str__(self):
        return f"{self.name} from {self.house}"   
    ...

class Professor(Wizard):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject
    def __str__(self):
        return f"{self.name} teaches {self.subject}"
    ...

def main():
    wizard = Wizard("Albus")
    student = Student("Harry", "Griffindor")
    professor = Professor("Severus", "Defense of the Dark arts")
    print(wizard)
    print(student)
    print(professor)
    

if __name__ == "__main__":
    main()
