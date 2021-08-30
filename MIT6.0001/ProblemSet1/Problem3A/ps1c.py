#!/usr/bin/env python3

# Given a time period of 3 years, an annual salary, as well as a semi annual raise, calculate what percentage
# of your income you should ideally save.
# Some notes: number of steps in this is significantly higher than given test examples on MIT and
# money_saved should be passed annual_salary, but it's fine.


def money_saved(guess_ideal_portion):
    ideal_portion = guess_ideal_portion * 0.0001
    annual_salary = 150000
    monthly_salary = annual_salary / 12
    months = 0
    semi_annual_raise = .07
    annual_rate_of_return = .04
    monthly_rate_of_return = annual_rate_of_return / 12
    current_savings = 0
    while months < 36:
        current_savings += (monthly_salary * ideal_portion) + (
            current_savings * monthly_rate_of_return
        )
        months += 1
        if months % 6 == 0:
            monthly_salary += semi_annual_raise * monthly_salary
            continue
    return current_savings


def searcher():
    savings_needed = 250000
    if money_saved(10000) < savings_needed:
        raise Exception("It is not possible to pay the down payment in three years")
    y_y = 10000
    counter = 1
    guess_ideal_portion = 5000
    current_savings = 0
    last_guess = 0
    while abs(savings_needed - current_savings) > 100:
        current_savings = money_saved(guess_ideal_portion)
        print(guess_ideal_portion)
        if current_savings < 249900:
            counter += 1
            last_guess = guess_ideal_portion
            guess_ideal_portion = (last_guess + y_y) / 2
            print(current_savings)
            print(guess_ideal_portion)
            print("looph")
            continue
        elif current_savings > 250100:
            counter += 1
            guess_ideal_portion = (guess_ideal_portion + last_guess) / 2
            continue
        return guess_ideal_portion, counter


if __name__ == "__main__":
    print(searcher())
