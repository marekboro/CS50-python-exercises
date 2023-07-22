import sys

def main(input:list[str]):
    intro()
    takeAll(input)
    takeAllButFirst(input)
    take1(input)
   
   

def take1(input:list[str]):
    print("\ntake only 1")
    input.remove(input[0])
    if len(input)>1:
        sys.exit("Too many arguments")
    if len(input)==0:
        sys.exit("Too few arguments")
    print(f"You ran this with: {input[0]}")

def takeAll(input:list[str]):
    print("\ntake all")
    for index, params in enumerate(input):
        print(f"Param {index+1}: {params}")

def takeAllButFirst(input:list[str]):
    
    print("\ntake all but not the first:")
    for index, params in enumerate(input[1:]):
        print(f"Param {index+1}: {params}")

def intro():
    print("App that allows you to capture the additional parameters that you run the app with using sys.argv - accessing the list of arguments provided")
    print("eg runninng this program: 'python 014_name.py bingo' will result in this message and 'You ran this with: bingo' ")

main(sys.argv)