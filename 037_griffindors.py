students = [{"name": "Hermione", "house":"Gryffindor"},
            {"name": "Harry", "house":"Gryffindor"},
            {"name": "Ron", "house":"Gryffindor"},
            {"name": "Padma", "house":"Ravenclaw"},
            {"name": "Draco", "house":"Slytherin"}]


#1
# gryffindors = [
#     student["name"] for student in students if student["house"] == "Gryffindor"
# ]

# for griffindor in sorted(gryffindors):
#     print(griffindor)

#2
# def is_griffindor(student):
#     return student["house"] == "Gryffindor"
         
# gryffindors = filter(is_griffindor, students)

# for griffindor in sorted(gryffindors, key=lambda s: s["name"]):
#     print(griffindor["name"])
    
#3     
# gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

# for griffindor in sorted(gryffindors, key=lambda s: s["name"]):
#     print(griffindor["name"])
    
strudentNames = ["Harry","Hermione","Ron"]
#4    
# gryffindors  = []
# for name in strudentNames:
#     gryffindors.append({"name":name,"house":"Gryffindor"})
# print(gryffindors)
    
#5 
# gryffindors  = [{"name":student,"house":"Gryffindor"} for student in strudentNames]
# print(gryffindors)

#5 
# gryffindors  = {student:"Gryffindor" for student in strudentNames}
# print(gryffindors)

#6 
# for i in range(len(strudentNames)):
#     print(i+1, strudentNames[i])
    
#7

for i, student in enumerate(strudentNames):
    print(i+1, student)