"""
A program that takes your monthly income, apply a monthly tax to it and also take account of your
monthly expenses, then tell you exactly all the information you need to know as regards your finance.
This helps to give you a better understanding of how you spend your money.

"""

# Creating a function where we specify all the calculation as regards the monthly finance
def calculate_finances(monthly_income: float, tax_rate: float, rent: float, food: float, gym_membership: float, currency: str) -> None:
    # calculation for each field 
    monthly_expenses: float = rent + food + gym_membership
    monthly_tax: float = monthly_income * (tax_rate / 100)
    monthly_net_income: float = monthly_income - monthly_expenses - monthly_tax
    yearly_salary: float = monthly_income * 12
    yearly_tax: float = monthly_tax * 12
    yearly_expenses: float = monthly_expenses * 12
    yearly_net_salary: float = monthly_net_income * 12

    # formating users information
    print('______________________________________________') 
    print(f'Monthly Income: {currency}{monthly_income:,.2f}')
    print(f'Tax rate: {tax_rate:,.0f}%')
    print(f'Food: {food:,.2f}')
    print(f'Rent: {rent:,.2f}')
    print(f'Gym membership: {gym_membership:,.2f}')
    print(f'Monthly tax paid: {monthly_tax:,.2f}')
    print(f'Monthly Expense: {monthly_expenses:,.2f}')
    print(f'Month net income: {monthly_net_income:,.2f}')
    print(f'Yearly salary: {yearly_salary:,.2f}')
    print(f'Yearly tax paid: {yearly_tax:,.2f}')
    print(f'Yearly Expenses: {yearly_expenses:,.2f}')
    print(f'Yearly net income: {yearly_net_salary:,.2f}')
    print('______________________________________________') 


# creating a function that deals with type error
def get_numeric_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('Invalid Input! Please enter a numeric value')


# creating a main entry point for the program
def main() -> None:
    # Get users input
    monthly_income: float = float(get_numeric_input('Enter your monthly income: '))
    tax_rate: float = float(get_numeric_input('Enter your tax rate(%): '))
    food: float = float(get_numeric_input('Enter your monthly food expenses: '))
    rent: float = float(get_numeric_input('Enter your monthly rent expense: '))
    gym_membership: float = float(get_numeric_input('Enter your gym membership fee: '))

    calculate_finances(monthly_income, tax_rate, rent, food, gym_membership, currency= '$')

# run the script
if __name__ == "__main__":
    main()
    