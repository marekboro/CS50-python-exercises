def main():
    x = int(input("Please enter x: \n"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    #3
    return n%2==0
    #2 return True if n%2==0 else False
    #1 if n%2==0:
    #1     return True
    

main()

# if x%2==0:
#     print("x is even")
# else:
#     print("x is odd")