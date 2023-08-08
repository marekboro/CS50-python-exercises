# 1:
# name = input("Name: ")
# house = input("House: ")
# print(f"{name} from {house}")

#2:
# def main():
#     name = get_name()
#     house = get_house()
#     print(f"{name} from {house}")

# def get_name():
#     return input("Name: ")

# def get_house():
#     return input("House: ")

# if __name__ == "__main__":
#     main()

# 3:
# def main():
#     name, house = get_student()
#     print(f"{name} from {house}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return name, house

# if __name__ == "__main__":
#     main()

#4:
# def main():
#     student = get_student()
#     print(f"{student[0]} from {student[1]}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return (name, house)

# if __name__ == "__main__":
#     main()

#5:
# def main():
#     student = get_student()
#     if student[0] == "Padma":
#         student[1] ="Ravenclaw"
    
#     print(f"{student[0]} from {student[1]}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return [name, house]

# if __name__ == "__main__":
#     main()

#6:
# def main():
#     student = get_student()
#     if student["name"] == "Padma":
#         student['house'] ="Ravenclaw"
    
#     print(f"{student['name']} from {student['house']}")


# def get_student():
# #    student = {}
# #    student["name"] = input("Name: ")
# #    student["house"] = input("House: ")
#     name = input("Name: ")
#     house = input("House: ")
#     return {"name": name, "house": house}

# if __name__ == "__main__":
#     main()

#7:
# class Student:
#     ...

# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")


# def get_student():
#     student = Student()
#     student.name = input("Name: ")
#     student.house = input("House: ")
#     return student

# if __name__ == "__main__":
#     main()

#8:
# class Student:
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house
#         self.experimental = f"{name} comes from the place know as {house}"

# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")
#     print(f"{student.experimental}")


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name,house)
     

# if __name__ == "__main__":
#     main()

#9:
# class Student:
#     def __init__(self, name, house):
#         if not name: # same as if 'name == ""'
#             raise ValueError("missing name")
#         self.name = name
#         if house not in ["Griffindor","Hufflepuff","Ravenclaw","Slytherin"]:
#             raise ValueError("invalid house")
#         self.house = house

# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")
    


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name,house)

#10:
# class Student:
#     def __init__(self, name, house):
#         if not name: # same as if 'name == ""'
#             raise ValueError("missing name")
#         self.name = name
#         if house not in ["Griffindor","Hufflepuff","Ravenclaw","Slytherin"]:
#             raise ValueError("invalid house")
#         self.house = house
#     def __str__(self):
#         return f"{self.name} from {self.house}"

# def main():
#     student = get_student()
#     print(student)

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name,house) 

# if __name__ == "__main__":
#     main()

#11:
# class Student:
#     def __init__(self, name, house, patronus):
#         if not name:
#             raise ValueError("missing name")
#         self.name = name
#         if house not in ["Griffindor","Hufflepuff","Ravenclaw","Slytherin"]:
#             raise ValueError("invalid house")
#         self.house = house
#         self.patronus = patronus

#     def __str__(self):
#         return f"{self.name}from {self.house}"
    
#     def charm(self):
#         match self.patronus:
#             case "Stag":
#                 return  "go go stagget"
#             case "Otter":
#                 return  "serious motter"
#             case "Jack Russel terrier":
#                 return  "Woof Woof"
#             case _:
#                 return "abra kadabra"

#     def cast_charm(self):
#         print("Expecto Petroleum!")
#         print(self.charm())


# def main():
#     student = get_student()
#     # print(student)
#     student.cast_charm()

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     patronus = input("Patronus: ")
#     return Student(name,house,patronus) 

# if __name__ == "__main__":
#     main()

#12:
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("missing name")
        self.name = name
        if house not in ["Griffindor","Hufflepuff","Ravenclaw","Slytherin"]:
            raise ValueError("invalid house")
        self.house = house
    

    def __str__(self):
        return f"{self.name}from {self.house}"


def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name,house) 

if __name__ == "__main__":
    main()