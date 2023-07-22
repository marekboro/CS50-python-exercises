# print("#")
# print("#")
# print("#")

# for _ in range(3):
#     print("#")



def main():
    print_column(3)
    print_separator()
    print_column1(3)
    print_separator()
    print_row(4,"?")
    print_separator()
    print_square(7)

def print_column(height):
    for _ in range(height):
        print("#")

def print_column1(height):
        print("# \n" * height, end="")

def print_row(width,character):
     print(character * width, sep="",end="\n")

def print_separator():
    print("<-.._..->")

def print_square(length):
    for _ in range(length):
        # print("dds")
        print_row(length,"#")

main()