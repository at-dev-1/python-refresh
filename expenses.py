total = 0
expenses = []
num_expenses = int(input("Enter number of expenses: "))


for i in range(num_expenses):
    expenses.append(float(input("Enter expense: ")))

    total = sum(expenses)


print("You spent $", total, sep="")