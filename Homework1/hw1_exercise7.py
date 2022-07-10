'''
Exercise for more experienced students
1. Automobile Costs
Write a program that asks the user to enter the monthly costs for the following expenses
incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires, and
maintenance. The program should then display the total monthly cost of these expenses, and the total annual cost of these expenses.

>> python hw1_exercise7.py

<< Enter loan payment: hello_world
<<   Error: could not convert string to float: 'hello_world'
<< Enter loan payment: 250.50     
<< Enter car insurance: 65.30
<< Enter gas expenses: 80
<< Enter oil expenses: 20
<< Enter tire costs: 40
<< Enter maintenance costs: 55

<< Monthly car expenses: $510.80

<< Annual car expenses: $6129.60
'''

from hw1_common_total import CommonTotal

class Automobile(CommonTotal):
    questions = (
        'Enter loan payment: ',
        'Enter car insurance: ',
        'Enter gas expenses: ',
        'Enter oil expenses: ',
        'Enter tire costs: ',
        'Enter maintenance costs: ')

    def __init__(self):
        CommonTotal.__init__(self, self.questions)

    def annual(self):
        return self.getSum() * 12

def main():
    a = Automobile()
    print("\nMonthly car expenses: ${:.2f}".format(a.getSum()))
    print("\nAnnual car expenses: ${:.2f}".format(a.annual()))

if __name__ == "__main__":
    main()
