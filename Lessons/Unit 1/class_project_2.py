class Person:
    def __init__(self, name, earnings) -> None:
        self.name, self.earnings = name, earnings

# Alex was a doctor so he earned $200,000 dollars for the year
# Ben who is a lawyer earned $100,000 dollars
# Caleb earned $95,000 through stock investments
# Daniel earned $20,000 from working at dominos. 

database = [
    Person("Alex", 200000),
    Person("Ben", 100000),
    Person("Caleb", 95000),
    Person("Daniel", 20000)
]

# $0            – $18,200       no tax
# $18,201       – $45,000       19 cents for each $1 over $18,200
# $45,001       – $120,000      $5,092 plus 32.5 cents for each $1 over $45,000
# $120,001      – $180,000      $29,467 plus 37 cents for each $1 over $120,000

def calculate_tax(income):
    if income < 18201:
        return 0
    elif income < 45000:
        return 0.19 * (income - 18200)
    elif income < 120000:
        return 5092 + .325 * (income - 45000)
    else:
        return 29467 + .37 * (income - 120000)

for person in database:
    print(person.name + " owes $" + str(calculate_tax(person.earnings)) + " of tax. ")