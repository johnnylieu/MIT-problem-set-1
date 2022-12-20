def calcuate():
    current_savings = 0
    r = 0.04
    months = 1

    total_cost = float(input('What is the total cost of the home you want? '))
    annual_salary = float(input('What is your annual salary? '))
    portion_saved = float(input('What percentage of your pay would you like to save (i.e, 0.1 for 10%)? '))

    monthly_salary = float(annual_salary / 12)
    portion_down_payment = total_cost * 0.25
    portion_saved = monthly_salary * portion_saved
    monthly_r = r/12

    while current_savings < portion_down_payment:
        current_savings = (current_savings + portion_saved)*(1+monthly_r)
        months +=1
    
    print(f"It took {months} months to save for your home's down payment.")



def main():
    if __name__ == "__main__":
        calcuate()

main()