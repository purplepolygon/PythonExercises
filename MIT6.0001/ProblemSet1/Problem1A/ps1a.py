#!/usr/bin/env python3


def month_calculator():
    total_cost = float(input("Enter the cost of your dream home: "))
    annual_salary = float(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the portion you'd like to save: "))
    portion_down_payment = 0.25
    monthly_salary = annual_salary / 12
    months = 0
    current_savings = float(0)
    annual_rate_of_return = 0.04
    monthly_rate_of_return = annual_rate_of_return / 12
    while True:
        if current_savings < portion_down_payment * total_cost:
            current_savings += (monthly_salary * portion_saved) + (
                current_savings * monthly_rate_of_return
            )
            months += 1
        else:
            print("Number of months: " + str(months))
            break


if __name__ == "__main__":
    month_calculator()
