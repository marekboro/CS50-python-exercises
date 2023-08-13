# #1
# first, _ = input("What is your name ").split(" ")
# print(f"hello {first}")

#2
# def total(galleons,sickles,knuts):
#     return (galleons * 17 + sickles) * 29+knuts

# print(total(100,50,25), "Knuts")

#3
# def total(galleons,sickles,knuts):
#     return (galleons * 17 + sickles) * 29+knuts

# coins = [100,50,25]

# print(total(coins[0],coins[1],coins[2]), "Knuts")

#4
def total(galleons,sickles,knuts):
    return (galleons * 17 + sickles) * 29+knuts

coins = [100,50,25]

print(total(*coins), "Knuts")