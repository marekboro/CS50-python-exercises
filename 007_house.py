def main1():
    name = input("What is your name? \n")
    if name == "Harry":
        print("Griffindor")
    elif name == "Hermione":
        print("Griffindor")
    elif name == "Ron":
        print("Griffindor")
    elif name == "Draco":
        print("SnakePeople")
    else:
        print("Who?")

def main2():
    name = input("What is your name? \n")
    if name == "Harry" or name == "Hermione" or name == "Ron":
        print("Griffindor")
    elif name == "Draco":
        print("SnakePeople")
    else:
        print("Who?")

def main3():
    name = input("What is your name? \n")
    match name:
        case "Harry" | "Hermione" | "Ron":
            print("Griffindor")
        case "Draco":
            print("SneakSneak")
        case _:
            print("Who dat?")
    



main3()