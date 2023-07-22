def meow1():
    print("Meow")
    print("Meow")
    print("Meow")



def meow2():
    i = 0
    while i <3:
        print("meow")
        i +=1

def meow3(n):
    i = n
    while i != 0:
        print("Meow !")
        i = i-1

def meow4(n):
    for _ in range(n):
        print("M30w")

def meow5(n):
    print("meWOW\n"*n, end="")


def ask():
    x = input("How many meows?: \n")
    return x

def askNumber():
    while True:
        n = int(input("You want meow how many times ?"))
        if n>0:
    #         break
    # return n
              return n

        #     continue
        # else:
        #     break

def ask_and_meow3():
    meow3(int(ask()))

def ask_and_meow4():
    meow4(int(ask()))

def ask_and_meow5():
    meow5(int(ask()))

def askNumber_then_meows():
    i = int(askNumber())
    meow3(i)
    meow4(i)
    meow5(i)

def main():
    # meow1()
    # meow2()
    # meow3(3)
    # ask_and_meow3()
    # ask_and_meow4()
    # ask_and_meow5()
    askNumber_then_meows()

main()    