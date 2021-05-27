#!/usr/bin/env python3


def month_calculator_with_raise():
    annual_salary = float(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the portion you\'d like to save: "))
    total_cost = float(input("Enter the cost of your dream home: "))
    semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal:"))
    portion_down_payment = .25
    monthly_salary = annual_salary / 12
    months = 0
    current_savings = float(0)
    annual_rate_of_return = .04
    monthly_rate_of_return = annual_rate_of_return / 12
    while True:
        if current_savings < portion_down_payment * total_cost:
            current_savings += (monthly_salary * portion_saved) + (current_savings * monthly_rate_of_return)
            months += 1
            if months % 6 == 0:
                monthly_salary += semi_annual_raise * monthly_salary
                continue
        else:
            print("Number of months: " + str(months))
            break


if __name__ == '__main__':
    month_calculator_with_raise()
