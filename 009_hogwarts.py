students = ["Hermione","Harry","Ron","Draco"]

# print(students[0])
# print(students[1])
# print(students[2])

# for student in students:
#     print(student)

# for i in range(len(students)):
#     print(i+1, students[i])


# houses = ["Gryphies","Gryphies", "Gryphies","Sneak-sies"]

studentHouses = {"Hermione":"Gryphies",
                 "Harry":"Gryphies",
                 "Ron":"Gryphies",
                 "Draco":"Sneak-sies"
                 }

# print(studentHouses["Hermione"])
# for student in studentHouses:
#     print(student.)

# for k in (studentHouses.keys()):
#     print(k +" => ", studentHouses[k])

# for s in studentHouses:
#     print(s+" ===> ",studentHouses[s])

studentos = [
    {"name":"Hermione", "house":"Gryphies", "pastramious":"Otter"},
    {"name":"Harry", "house":"Gryphies", "pastramious":"Stag"},
    {"name":"Ron", "house":"Gryphies", "pastramious":"Jack Russel terrier"},
    {"name":"Draco", "house":"Sneak-sies", "pastramious":None},
]

for student in studentos:
    print(student["name"],student["house"], sep=", ")