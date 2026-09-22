income = input("what is your income ")
income_as_numerical = float(income)
rounded_income = round(income_as_numerical)

if type(rounded_income) == int:
    print(rounded_income)
    
