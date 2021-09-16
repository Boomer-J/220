"""
name: Jenks, Boomer
hello.py

Problem: Calculates the total monthly interest charge and the total monthly interest for any starting balance and payment

Certification of authenticity:
I certify that this assignment is entirely my own work.
"""
def  main():
    interest_rate = eval(input("input the annual interest rate: "))
    billing_days = eval(input("input the number of days in the billing cycle: "))
    bal = eval(input("input your inital balance: "))
    payment = eval(input("input the value of your payment: "))
    days = eval(input("input day of the billing cycle you submitted your payment: "))
    step1 = bal * billing_days
    step2 = payment * (billing_days - days)
    step3 = step1 - step2
    dailyb = step3 / billing_days
    monthly_interest = interest_rate / 12
    #print("the monthly interest charge is",round(Monthly_interest,2))
    monthly_charge = dailyb * monthly_interest
    print(round(monthly_charge*.01, 2))
if __name__ == '__main__':
    main()
