#Write a program that will calculate the amount someone earns according to the number of hours worked and the hourly wage, assuming that the person worked 350 houres at a 12% tax braket.
# At the end the program should print the hourly wage, # of hours worked, wages before taxes, tax wage,and annual wage after taxes.
def get_positive_float_input():
#INPUT
# Thes user should give the hourly wage and the amount of hours worked.
 #bad_input = True
  while(True):
    try:
      hourly_wage = float(input("Enter your hourly wage in U.S Dollars:"))
      #check in user weight is > 0. If not, reprompt t:he user
      if hourly_wage <= 0:
        print("ERROR: Enter a wage greater than 0")
        continue
      else:
        break
    except:
      print("ERROR: Please enter a number greater than 0")

  return hourly_wage

def get_positive_float_input_hours():

  while(True):
    try:
      hours = float(input("Enter your hours worked:"))
      #check in user weight is > 0. If not, reprompt the user
      if hours <= 0:
        print("ERROR: Enter a number of hours greater than 0")
        continue
      if(hours > 24):
        print(" Error: Must be 24 or below")
        continue
      else:
        break
    except:
      print("ERROR: Please enter a number greater than 0")
  return hours


hours = get_positive_float_input_hours()

hourly_wage = get_positive_float_input()

#PROCCESING
#The program should take the 2 numbers given and multiply them by each other and then multiply it by 350 for the annual wage before taxes
#The program should then find out what 12% of that is .
#This number is then subtract the total annual wage to find wage after taxes
daily_wage = hours * hourly_wage
anual_conversion = 350
wages_before_taxes = daily_wage * anual_conversion
tax_conversion = .12
taxes = wages_before_taxes * tax_conversion
annual_tax_conversion = .88
annual_after_taxes= annual_tax_conversion * wages_before_taxes


#OUTPUT
# At the end the program should print the hourly wage, # of hours worked, wages before taxes, tax wage,and annual wage after taxes.
print(f"Hourly Wage:${hourly_wage}")
print(f"Hours Worked:{hours}")
print(f"Daily wage is:$ {daily_wage:.2f}")
print(f"Wages before taxes:${ wages_before_taxes:.2f}")
print(f"Tax amount:${taxes:.2f}")
print(f"Annual wage after taxes:${annual_after_taxes:.2f}")
