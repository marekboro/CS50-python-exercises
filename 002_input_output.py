"""
Multi
Line
Comment
syntax
"""

# single line commenting syntax

# # ask for name
# name = input("Enter your full name \n")
# first, last = name.split(" ")

# # Say hi to user. 
# print("Hello, ", name,  sep='')
# print(f"Hello, {name.strip().title()}",  )
# print('hello, "friend"')
# print("hello, \"friend\"", end='')
# print( "... the end")


# hacker solution: 
name = input("Enter your full name \n").strip().title()
first, last = name.split(" ")
print(f"Hello, {first.strip().title()}", f"I know your last name too: {last}" , sep=" - ",  )
example = 'This is a longer text to split'
a,b,c,d,e,f,g = example.split(' ')
print(f" the example string: '{example}', and the individual constituents: {a},{b},{c},{d},{e},{f},{g}")