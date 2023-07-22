# x = input("enter x\n")
# y = input("enter y\n")
# z = int(x)+int(y)
# print(z)

# OR

# x = int(input("give me X: \n"))
# y = int(input("give me X: \n"))
# print(f"{x} + {y} = {x+y}")

# # OR

# x = float(input("give me X: \n"))
# y = float(input("give me X: \n"))
# z = round(x+y)
# print(f'{z:,}')

#madness: 
#print(
#    int(input("give me X: \n"))
#   +int(input("give me Y: \n"))
#    )

# take 3
# x = float(input("give me X: \n"))
# y = float(input("give me X: \n"))
# z = round(x/y,2)
# print(z)
# print(f'{z:.4f}')

def main():
    x = int(input("give x!: \n"))
    
    print(f"{x}^2 =", square(x))
    y = int(input("give y!, faster!: \n"))
    print(f"{x}^{y} =", pow(x,y))

def square(n):
    return n*n

if __name__== "__main__":
    main()
