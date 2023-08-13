#1
# balance = 0

# def main():
#     print("Balance: ",balance)
#     deposit(100)
#     withdraw(50)
#     print("Balance: ",balance)
    
# def deposit(n):
#     balance += n    

# def withdraw(n):
#     balance -= n  
    
# if __name__ == "__main__":
#     main()
    
#2
# def main():
#     balance = 0
#     print("Balance: ",balance)
#     deposit(100)
#     withdraw(50)
#     print("Balance: ",balance)
    
# def deposit(n):
#     balance += n    

# def withdraw(n):
#     balance -= n  
    
# if __name__ == "__main__":
#     main()
    
# #3
# balance = 0
# def main():
#     print("Balance: ",balance)
#     deposit(100)
#     withdraw(50)
#     print("Balance: ",balance)
    
# def deposit(n):
#     global balance
#     balance += n    

# def withdraw(n):
#     global balance
#     balance -= n  
    
# if __name__ == "__main__":
#     main()
    
#4

class Account:
    def __init__(self):
        self._balance = 0
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self,n):
        self._balance += n   
    
    def withdraw(self,n):
        self._balance -= n
        
    def __str__(self):
        return f"Acc balance: {self._balance}"
    
def main():
    account = Account()
    print(account)
    account.deposit(100)
    account.withdraw(50)
    print(account)
    
if __name__ == "__main__":
    main()
    
