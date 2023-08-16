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
# def total(galleons,sickles,knuts):
#     return (galleons * 17 + sickles) * 29+knuts

# coins = [100,50,25]

# print(total(*coins), "Knuts")

#5
# def total(galleons,sickles,knuts):
#     return (galleons * 17 + sickles) * 29+knuts

# coins = {"galleons":100,"sickles":50,"knuts":25}

# # print(total(galleons=100,sickles=50,knuts=25), "Knuts")
# print(total(coins["galleons"],coins["sickles"],coins["knuts"]), "Knuts")

#6
# def total(galleons,sickles,knuts):
#     return (galleons * 17 + sickles) * 29+knuts

# coins = {"galleons":100,"sickles":50,"knuts":25}

# print(total(**coins), "Knuts")

#7


def f(*args, **kwargs):
    print("Positional: ",args)
    print("named: ",kwargs)
    x = kwargs.keys()
    buildsting = ""
    for key in x:
        print(key)
        buildsting += f"{key}, "
    print("buildsting: ", buildsting)
    
    
coins = {"galleons":100,"sickles":50,"knuts":25}
coins2 = {"galleonz":100,"sicklez":50,"knutz":25}
f(100,50,25, **coins,  **coins2)

