"""
A program that split the total amount of expense between a given number of persons present and 
also take note of individual percentage in the split.

"""
# creating a function to take care of typevalue errors in out program
def get_numeric_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError as e:
            print(f'Error : {e}')

# creating a function to work out the individual percentage sharing 
def percentage_sharing(number_of_people: int) ->None:
    percentages = []
    total_percentage = 0
    for i in range(1, number_of_people + 1):
        while True:
            remaining_percentage: float  = 100 - total_percentage
            print(f'Remaining percentge: {remaining_percentage:.2f}%')

            percentage: float = get_numeric_input(f'Enter the sharing percentage of {i}:')

            if 0<= percentage <= remaining_percentage:
                percentages.append(percentage)
                total_percentage += percentage
                break
            else:
                print(f'Please enter a percentage between 0 and {remaining_percentage}')
    return percentages

# Creating a function where we specify all the calculation as regards sharing of the total amount
def calculate_split(total_amount: float, number_of_people: int, currency: str) -> None:
    # checking that the total number of people exceeds one
    if number_of_people <= 1:
        raise ValueError('Number of people must be greater than one')
    
    # Invoking the percentage sharing function
    percentages = percentage_sharing(number_of_people)

    # fomating users information and also calculating individual amount base on individual percentage
    print('______________________________________________')
    print(f'Total amount: {currency}{total_amount:,.2f}')
    print(f'Total number of people: {number_of_people}')
    for idex, pct in enumerate(percentages, start= 1):
        sharing_per_person: float = (pct / 100) * total_amount
        print(f'Sharing for person {idex} with {pct}%  is {currency}{sharing_per_person:,.2f}')
    print('______________________________________________')


# creating a main entry point for the program
def main()->None:
    total_amount: float = get_numeric_input('Enter the total amount to be shared: ')
    number_of_people: int = int(get_numeric_input('Enter the total number of people present: '))

    calculate_split(total_amount, number_of_people, currency= '$')

# run the script
if __name__ == '__main__':
    main()