def calcuate():
    current_savings = 0
    r = 0.04
    months = 1

    total_cost = float(input('What is the total cost of the home you want? '))
    annual_salary = float(input('What is your annual salary? '))
    portion_saved = float(input('What percentage of your pay would you like to save (i.e, 0.1 for 10%)? '))
    semi_annual_raise = float(input('What is your semi annual raise (in percentage)? '))

    monthly_salary = float(annual_salary / 12)
    portion_down_payment = total_cost * 0.25
    monthly_saved = monthly_salary * portion_saved
    monthly_r = r/12

    while current_savings < portion_down_payment:
        if months%6 == 0:
            annual_salary = annual_salary + (annual_salary*semi_annual_raise)
            monthly_salary = annual_salary / 12
            monthly_saved = monthly_salary * portion_saved
        current_savings = ((current_savings + monthly_saved)*(monthly_r)) + (current_savings + monthly_saved)
        months +=1
          
    print(f"It took {months} months to save for your home's down payment.")



def main():
    if __name__ == "__main__":
        calcuate()

main()