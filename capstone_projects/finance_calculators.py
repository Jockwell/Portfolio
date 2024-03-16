import math

# This program will calculate the interest of the user's investment or calculate how much they owe on a home loan.
# The user must choose between the 'investment' calculator or the 'bond' calculator.
print("\n")
print("Investment \t - To calculate the amount of interest you'll earn on your investment.")
print("Bond \t\t - To calculate the amount you'll have to pay on a home loan. \n\n")

calculator_type = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

calculator_type = str.lower(calculator_type)

# This code below is an if-elif-else statements dependant on what the calculator the user chose to use above.

if calculator_type == "investment":
    user_amount = float(input("Please enter the amount of money you are depositing (£):"))
    interest_rate = float(input("Please enter the interest rate for your investment (%):"))
    investment_term = float(input("Please enter the number of years you plan to invest:"))
    interest = input("Please choose between 'simple' & 'compound' interest:")
    interest = str.lower(interest)

# Another if-elif-else statements is used dependant on whether 'simple' or 'compound' interest is used.
# Below is the code to calculate the 'simple interest investment' and prints the output.
    
    if interest == "simple":
        simple_interest_total = user_amount * (1 + (interest_rate / 100) * investment_term)
        simple_investment_output = f'''Depositing £{user_amount} with the interest rate of {interest_rate}% means the total amount once interest is applied will be £{round(simple_interest_total , 2)} after the {investment_term} year period.'''
        print(u'\u2500' * 50 + "\n\n" + simple_investment_output + "\n")
        print("This means the overall profit from your investment will be £" + str(round(simple_interest_total- user_amount, 2)) + ".\n")
        print(u'\u2500' * 50)

# Below is the code to calculate the 'compound interest investment' and prints the output.
    
    elif interest == "compound":
        compound_interest_total = user_amount * math.pow(1 + (interest_rate /100), investment_term)
        compound_investment_output = f'''Depositing £{user_amount} with the interest rate of {interest_rate}% means the total amount once interest is applied will be £{round(compound_interest_total , 2)} after the {investment_term} year period.'''
        print(u'\u2500' * 50 + "\n\n" + compound_investment_output + "\n")
        print("This means the overall profit from your investment will be £" + str(round(compound_interest_total - user_amount , 2)) + ".\n")
        print(u'\u2500' * 50)

    
    else:
        print(u'\u2500' * 50)
        print("\n" + '''You have incorrectly chosen the type of the interest you want applied. Please re-run the program enter either 'simple' or 'compound' when requested in the 'Investment' calculator. \n''')
        print(u'\u2500' * 50)

# Below is the code for when the user decides to use the 'bond' calculator to calculate how much they repay each month on their house.
        
elif calculator_type == "bond":
    house_value = float(input("Please enter the present value of your house (£):"))
    bond_interest = float(input("Please enter the interest rate (%):"))
    monthly_interest = bond_interest / 100 / 12
    repayment_months = int(input("Please enter the months you plan to repay back this bond:"))
    repayment_total = (monthly_interest * house_value) / (1 - (1 + monthly_interest) ** (-repayment_months))
    repayment_total = round(repayment_total, 2)
    bond_repayment_output = f'''If your house is valued at £{house_value}, your interest rate is {bond_interest}% and you plan to repay your house off in {repayment_months} months. You will have to pay back £{repayment_total} each month.'''

    print(u'\u2500' * 50 + "\n\n" + bond_repayment_output + "\n\n" + u'\u2500' * 50)

# Below is the code for when the user doesn't correctly choose from the 'bond' or 'investment' calculator.
# The code will ask the users to re-run the program and choose correctly between 'bond' or 'investment'.
    
else:
    print("\n" + u'\u2500' * 50)
    print('''\n You have not correctly choosen between the 'Bond' calculator or the 'Investment' calculator. 
          \n Please re-run the program and enter 'bond' or 'investment' dependent on what calculator you would like to use.
          ''')
    print(u'\u2500' * 50)