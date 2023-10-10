"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contracts=1, commission=0):
        self.name = name
        self.commission = commission
        self.contracts = contracts

    def get_pay(self):
        pass

    def __str__(self):
        pass

class SalariedEmployee(Employee):
    def __init__(self, name, salary, contracts=1, commission=0,):
        super().__init__(name, contracts, commission)
        self.salary = salary
        self.contracts = contracts

    def get_pay(self):
        if self.commission == 0:
            return self.salary
        else:
            return (self.commission * self.contracts) + self.salary
        
    def __str__(self):
        if self.commission == 0:
            return(f"{self.name} works on a monthly salary of {self.salary}.  Their total pay is {self.get_pay()}.")
        elif self.contracts == 1:
            return(f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.commission}.  Their total pay is {self.get_pay()}.")
        else:
            return(f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.contracts} contract(s) at {self.commission}/contract.  Their total pay is {self.get_pay()}.")

class WagedEmployee(Employee):
    def __init__(self, name, hours, wages, contracts=1, commission=0):
        super().__init__(name, contracts, commission)
        self.hours = hours
        self.wages = wages

    def get_pay(self):
        if self.commission == 0:
            return self.hours * self.wages
        else:
            return (self.commission * self.contracts) + (self.hours * self.wages)
        
    def __str__(self):
        if self.commission == 0:
            return(f"{self.name} works on a contract of {self.hours} hours at {self.wages}/hour.  Their total pay is {self.get_pay()}.")
        elif self.contracts == 1:
            return(f"{self.name} works on a contract of {self.hours} hours at {self.wages}/hour and receives a bonus commission of {self.commission}.  Their total pay is {self.get_pay()}.")
        else:
            return(f"{self.name} works on a contract of {self.hours} hours at {self.wages}/hour and receives a commission for {self.contracts} contract(s) at {self.commission}/contract.  Their total pay is {self.get_pay()}.")

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalariedEmployee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = WagedEmployee('Charlie', 100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalariedEmployee('Renee', 3000, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = WagedEmployee('Jan', 150, 25, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalariedEmployee('Robbie', 2000, commission=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = WagedEmployee('Ariel', 120, 30, commission=600)

