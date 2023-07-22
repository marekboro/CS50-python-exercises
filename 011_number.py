# print("hello, dude")


# x = int(input("gimme a number:"))
# print(f"x is {x}")

# try:
#     x = int(input("gimme a number:"))
#     print(f"x is {x}")
# except ValueError:
#     print("x is not an integer")

# try:
#     x = int(input("gimme a number:"))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")

# while(True):
#     try:
#         x = int(input("gimme a number:"))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break
# print(f"x is {x}")

# y = True
# while(y):
#     try:
#         x = int(input("gimme a number:"))
#         y = False
#     except ValueError:
#         y = True
#     else:
#         print(f"x is {x}")

# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while(True):
#         try:
#             return int(input("What number will you give me ?:"))
#         except ValueError:
#             pass
#             # print("x is not an integer")

# def main():
#     print(f"x is {get_int()}")

# def get_int():
#     while(True):
#         try:
#             return int(input("What number will you give me ?:"))
#         except ValueError:
#             pass
            

def main():
    sum_numbers_in_range()

def get_int(prompt):
    while(True):
        try:
            return int(input(prompt))
        except ValueError:
            pass

def sum_two():
    x = get_int("Rysiu, what is your first number?: ")
    y = get_int("and the other number? ")
    print(f"Their sum is : {x+y}")

def sum_numbers_in_range():
    x = get_int("Rysiu, what is the first number?: ")
    y = get_int("and the last number? ")
    print(f"{sum(range(x,y+1))}")
    


main()