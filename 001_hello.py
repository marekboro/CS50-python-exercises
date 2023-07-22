# take 1:
# print("hello world")
# print("1." #error : missing parethasis error type: syntax
# print("2.")
# print("3.")
# print("4.")


#take 2:
# def hello(to):
#  print("Hello",to)

# name = input("Give name now!: \n")
# hello(name)

#take 3:
def main():
    name = input("Give name please!: \n")
    hello(name)

def hello(to="world"):
    # print("hello... ", to)
    return f"hello... , {to}"

if __name__ == "__main__":
    main()