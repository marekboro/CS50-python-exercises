# #1
# MEOWS = 3

# for _ in range(MEOWS):
#     print("M E O W")
    
#2

# class Cat:
#     MEOWS = 3
    
#     def meow(self):
#         for _ in range(Cat.MEOWS):
#             print("meow")

# cat = Cat()
# cat.meow()

#3
# def meow(n: int):
#     for _ in range(n):
#         print("meow")
        

# # number = int(input("How many meows? "))
# number: int = int(input("How many meows? "))
# meow(number)

#4
# def meow(n: int) -> None: 
#     for _ in range(n):
#         print("meow")
   
        
# number: int = int(input("How many meows? "))
# meows: str = meow(number)
# print(meows)

#5
# def meow(n: int) -> str: 
#     return  "meow\n" *n
    
# number: int = int(input("How many meows? "))
# meows: str = meow(number)
# print(meows)

#6
# import sys

# if len(sys.argv)==1:
#     print("meow")
# else:
#     print("usage: meows.py")    


#7
# import sys

# if len(sys.argv) == 1:
#     print("meow")
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     print("meow\n"*int(sys.argv[2]))
# else:
#     print("usage:\n flags:\n  -n: number of times to meow")
    
#8
# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("-n")
# args = parser.parse_args()

# for _ in range(int(args.n)):
#     print("meow")
    
#8
import argparse

parser = argparse.ArgumentParser(description="Meow like a horse")
parser.add_argument("-n",default=1, help="number of times you want to meow like a trooper", type=int)
args = parser.parse_args()
print(f" --> {parser}")
for _ in range(int(args.n)):
    print("meow")

   