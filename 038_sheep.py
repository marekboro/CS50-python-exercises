
#1
# def main():
#     n = int(input("How many sheep you need? "))
#     for i in range(n):
#         print("🐑"*i)
        
# if __name__ == "__main__":
#     main()
    
#2
# def main():
#     n = int(input("How many sheep you need? "))
#     for i in range(n):
#         print(sheep(i+1))

# def sheep(n):
#     return "🐑"*n
        
# if __name__ == "__main__":
#     main()
    
#3
# def main():
#     n = int(input("How many sheep you need? "))
#     for s in sheep(n):
#         print(s)

# def sheep(n):
#     flock = []
#     for i in range(n+1):
#         flock.append("🐑"*i)
#     return flock
        
# if __name__ == "__main__":
#     main()
    
#4
def main():
    n = int(input("How many sheep you need? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "🐑"*i

        
if __name__ == "__main__":
    main()