class Investment:
    def __init__(self, principal, interest):
        self.principal = principal
        self.interest = interest

    def value_after(self, n):
        return self.principal * (1 + self.interest) ** n

    def __str__(self):
        print("principal - %.2f , interest rate - %.2f" %(self.principal, self.interest))


a = Investment(1000.00, 5.12)
print(a.value_after(20))
a.__str__()
