"""
Design a Python program that prompts users to enter their total budget (ask them for their net monthly income) and amounts for spending categories:
Housing (rent or mortgage)
Utilities
Groceries
Transportation
Health Care
Personal Care
Clothing
Debt
Calculate the percentage of the total budget spent in each category.
Tell the user how much the spent total, and how much money they have left. 
Display the results in a user-friendly format using f-strings.
Ensure your code is well-commented to explain the functionality of different sections.

"""


net_monthly_income =float(input("enter the net monthly income:"))
housing=float(input("enter housing:"))
utilities=float(input("enter untilites:"))
groceries=float(input("enter groceries:"))
transportation=float(input("enter transporation:"))
health_care=float(input("enter health care:"))
personal_care=float(input("enter personal care:"))
clothing=float(input("enter clothing:"))
debt=float(input("enter debt:"))


# calculate the percentage of the total budget spent in each category
print(f"housing: {housing/net_monthly_income:.2%}")
print(f"utilities: {utilities/net_monthly_income: .2%}")
print(f"groceries: {groceries/net_monthly_income: .2%}")
print(f"transportation: {transportation/net_monthly_income: .2%}")
print(f"health_care: {health_care/net_monthly_income}")
print(f"personal_care: {personal_care/net_monthly_income: .2%}")
print(f"clothing: {clothing/net_monthly_income: .2%}")
print(f"debt: {debt/net_monthly_income: .2%}")

# add all expenses then subract the remaining balance
total= housing+utilities+groceries+transportation+health_care+personal_care+personal_care+clothing+debt
print(f"Money left: {net_monthly_income-total:.2f}")
print(f"total: {total:.2f}")