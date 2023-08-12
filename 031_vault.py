class Vault:
    def __init__(self,name,galleons =0, sickles=0,knuts=0):
        self.name = name
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
    def __add__(self,other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault("total",galleons,sickles,knuts)
    
    def __mul__(self,other):
        galleons = self.galleons * other.galleons
        sickles = self.sickles * other.sickles
        knuts = self.knuts * other.knuts
        return Vault("multiplied",galleons,sickles,knuts)
    
    def __sub__(self,other):
        # print("Get out ya thief!")
        galleons = abs(self.galleons - other.galleons)
        sickles = abs(self.sickles - other.sickles)
        knuts = abs(self.knuts - other.knuts)
        return Vault("difference",galleons,sickles,knuts)
        
    def __str__(self):
        return f"{self.name}:\n{self.galleons} galleons\n{self.sickles} sickles\n{self.knuts} knuts\n"
        
potter = Vault("potter", 100,50,25)        
weesley = Vault("weesley", 25, 50, 100)
       
total = potter + weesley
difference = potter - weesley
multiplied = potter * weesley
# print(potter)
# print(weesley)
# print(total)
# print(difference)
print(multiplied)
