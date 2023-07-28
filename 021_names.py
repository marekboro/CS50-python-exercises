# names = []

# for _ in range(3):
#     names.append(input("What's your name? "))

# for name in sorted(names):
#     print(f"Hello, {name}")
# -------------------------------
# name = input("Whats is your name? ")

# # namesFile = open('021_names.txt','w')
# namesFile = open('021_names.txt','a')
# namesFile.write(f"{name}\n")
# namesFile.close()

# --------------------------- Write: 
# name = input("Whats is your name? ")
# with open('021_names.txt','a') as namesFile:
#     namesFile.write(f"{name}\n")
#     namesFile.close()

# ---------------- Read #1:
# with open('021_names.txt','r') as namesFile:
#     lines = namesFile.readlines()
    
# for index, name in enumerate(lines): 
#     # print(f"{index+1:02}: {name}",end="")
#     print(f"{index+1:02}: {name.rstrip()}")

# ---------------- Read #2:
# with open('021_names.txt','r') as namesFile:
#     for index, line in enumerate(namesFile):
#         print(f"Line {index+1:02}: {line.rstrip()}")

# ---------------- Read 3:
# with open('021_names.txt') as namesFile:
#     for line in namesFile:
#         names.append(line.rstrip())
# for index, name in enumerate(sorted(names)):
#     print(f"Line {index+1:02}: {name.rstrip()}")

# ---------------- Read 4:
# with open('021_names.txt') as namesFile:
#     for index, name in enumerate(sorted(namesFile)):
#         print(f"Line {index+1:02}: {name.rstrip()}")

# ---------------- Read 4:
# with open('021_names.csv') as namesFile:
#     for index, line in enumerate(sorted(namesFile)):
#         name, location = line.rstrip().split(",")
#         print(f"Line {index+1:02}: {name} lives in {location}")

# ---------------- Read 5: sorting by specific thing
# students = []
# with open('021_names.csv') as namesFile:
#     for line in namesFile:
#         name, location = line.rstrip().split(",")
#         student = {"name":name,"location":location}
#         students.append(student)

# def get_name(student):
#     return student['name']


# for student in sorted(students,key=get_name):
#     print(f"{student['name']} lives in {student['location']}")

# ---------------- Read 6: sorting by specific thing + lambdas
# students = []
# with open('021_names.csv') as namesFile:
#     for line in namesFile:
#         # index = line.find(".")
#         name, location = line.rstrip().split(",")
#         student = {"name":name,"location":location}
#         students.append(student)

# for student in sorted(students,key= lambda student: student['name']):
#     print(f"{student['name']} lives in {student['location']}")

# ---------------- Read 7: use CSV
# import csv
# students = []
# with open('021_names2.csv') as namesFile:
#     reader = csv.DictReader(namesFile)
#     for row in reader:
#         students.append({"name": row["name"], "location": row["location"]})
#         # students.append(row) ??

# for student in sorted(students,key= lambda student: student['name']):
#     print(f"{student['name']} lives in {student['location']}")

# ---------------- Read 8: go nuts
import csv
# print("why many words if few do job")
name = input("Name?")
location = input("Where live?")

with open('021_names3.csv',"a") as file:
    # writer = csv.writer(file)
    # writer.writerow([name,location])
    writer = csv.DictWriter(file,fieldnames=["name","location"],lineterminator="\n")
    writer.writerow({"name":name,"location":location})
#     for row in reader:
#         students.append({"name": row["name"], "location": row["location"]})
        
# for student in sorted(students,key= lambda student: student['name']):
#     print(f"{student['name']} lives in {student['location']}")