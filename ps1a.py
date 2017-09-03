# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""




annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ")) 
total_cost = float(input("Enter cost of dream home: "))


current_savings = 0
portion_down_payment = total_cost*0.25
r = 0.04
monthly_salary = annual_salary/12
months = 0


while current_savings <= portion_down_payment:
    current_savings += (portion_saved*monthly_salary)+(current_savings*r/12)
    months += 1
print(months)