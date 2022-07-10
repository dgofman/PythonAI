'''
2. Stadium Seating
There are three seating categories at a stadium. Class A seats cost $20, Class B seats cost $15, and Class C seats cost $10. 
Write a program that asks how many tickets for each class of seats were sold, then displays the amount of income generated from ticket sales.

>> python hw1_exercise8.py

<< How many seats sold for class A: hello_world
<<   Error: could not convert string to float: 'hello_world'
<< How many seats sold for class A: 5
<< How many seats sold for class B: 3
<< How many seats sold for class C: 7

<< Total sold tickets: 15

<< Your income: $215.00
'''

from hw1_common_total import CommonTotal

class Stadium(CommonTotal):
    rows =  {'A': 20, 'B': 15, 'C': 10}
    questions = list(map(lambda row : 'How many seats sold for class {}: '.format(row), rows.keys()))

    def __init__(self):
        CommonTotal.__init__(self, self.questions)

    def income(self):
        total = 0.0
        for index, cost in enumerate(self.rows.values()):
            total += self._values[index] * cost
        return total

def main():
    a = Stadium()
    print("\nTotal sold tickets: {:.0f}".format(a.getSum()))
    print("\nYour income: ${:.2f}".format(a.income()))

if __name__ == "__main__":
    main()
