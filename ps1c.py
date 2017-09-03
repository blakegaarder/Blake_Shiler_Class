# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""




#########################################################



annual_salary = float(input("Enter your starting annual salary: "))

semi_annual_raise = .07
current_savings = 0
portion_down_payment = 250000
r = 0.04  #rate of return
monthly_salary = annual_salary/12
savings_rate = 0.01
monthly_saved = monthly_salary * savings_rate
months = 0
numGuesses =  0
low = 0
high = 100000
ans = (high + low)/2.0

while abs(ans - portion_down_payment) < range(int(current_savings - 100),int(current_savings + 100)):
    if ans < portion_down_payment:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0

    numGuesses += 1

    savings_rate = ans * .001

    monthly_saved = monthly_salary * savings_rate

    for months in range(36):
        months += 1
        if months % 6 == 0:

            annual_salary += (semi_annual_raise * annual_salary)

            monthly_salary = annual_salary/12

            monthly_saved = monthly_salary * savings_rate

        current_savings += (monthly_saved)+(current_savings*r/12)

    ans = current_savings

print(ans)
print(numGuesses)


#######################################################

# x = 25
# epsilon = 0.01
# numGuesses =  0
# low = 0.0
# high = max(1.0, x)
# ans = (high + low)/2.0
# while abs(ans**2 - x) >= epsilon:
#     print 'low =', low, 'high =', high, 'ans =', ans
#     numGuesses += 1
#     if ans**2 < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low)/2
# print 'numGuess =', numGuesses
# print ans, 'is close to square root of', x



