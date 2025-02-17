
# Get details of loan
money_owed = float(input("How much money is owed, in dollars?\n ")) # $50,000

apr = float(input("What is the annual percentage rate of the loan?\n")) #3%
payment = float(input( "How much will you pay off each month in dollars?\n")) # $1,000
months = int(input("How many months will it take to pay off the loan?\n")) #24

monthly_rate= apr/100/12

for i in range(months):
    # Calculate interest to pay

    interest_paid = money_owed * monthly_rate

    # Add in interest

    money_owed = money_owed + interest_paid

    if money_owed -payment < 0:
        print("The last payment is", money_owed)
        print("You paid off the loan in", i+1, "months.")
        break

    # Make payment

    money_owed = money_owed - payment

    print("Paid", payment, "of which", interest_paid, "is interest.", end=" ")
    print("Now I owe", money_owed)