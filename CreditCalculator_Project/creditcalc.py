import math
import sys

args = sys.argv

#All possible variables the user could input
parameter_dict = {}
for user_input in args[1:]: #Iterate over argv[1:]
    varname = user_input.split("=")[0] #Get what's left of the '='
    varvalue = user_input.split("=")[1] #Get what's right of the '='
    parameter_dict[varname] = varvalue

for varvalues in parameter_dict.values():
    if varvalues != 'annuity' and varvalues != 'diff':
        if float(varvalues) < 0:
            print('Incorrect parameters')
        else:
            continue
    else:
        continue

if parameter_dict['--type'] == 'annuity' and len(parameter_dict) == 4:
    if '--periods' not in parameter_dict:

        credit_principal = int(parameter_dict['--principal'])
        monthly_payment = float(parameter_dict['--payment'])
        credit_interest = float(parameter_dict['--interest'])
        i = (credit_interest / 100) / 12

        n_of_periods = math.log((monthly_payment / (monthly_payment - i * credit_principal)), (1 + i))

        years = math.ceil(n_of_periods) // 12
        months = math.ceil(n_of_periods) % 12
        overpayment = (math.ceil(n_of_periods) * math.ceil(monthly_payment)) - credit_principal

        if years > 1 and months > 1:
            print('It will take {0} years and {1} months to repay this credit!'.format(years, months))
            print('Overpayment = {}'.format(overpayment))
        elif years == 0 and months > 1:
            print('It will take {0} months to repay this credit!'.format(months))
            print('Overpayment = {}'.format(overpayment))
        elif years > 0 and months == 0:
            print('It will take {0} years to repay this credit!'.format(years))
            print('Overpayment = {}'.format(overpayment))
        elif years == 1 and months == 0:
            print('It will take {0} year to repay this credit!'.format(years))
            print('Overpayment = {}'.format(overpayment))
        elif years == 1 and months > 1:
            print('It will take {0} year and {1} months to repay this credit!'.format(years, months))
            print('Overpayment = {}'.format(overpayment))
        elif years == 1 and months == 1:
            print('It will take {0} year and {1} month to repay this credit!'.format(years, months))
            print('Overpayment = {}'.format(overpayment))

    elif '--payment' not in parameter_dict:

        credit_principal = int(parameter_dict['--principal'])
        n_of_periods = int(parameter_dict['--periods'])
        credit_interest = float(parameter_dict['--interest'])
        i = (credit_interest / 100) / 12

        monthly_payment = credit_principal * ((i * (1 + i) ** n_of_periods) / ((1 + i) ** n_of_periods - 1))
        overpayment = (n_of_periods * math.ceil(monthly_payment)) - credit_principal

        print('Your monthly payment = {0} !'.format(math.ceil(monthly_payment)))

        if overpayment > 0:
            print('Overpayment = {}'.format(overpayment))
        else:
            pass

    elif '--principal' not in parameter_dict:

        monthly_payment = float(parameter_dict['--payment'])
        n_of_periods = int(parameter_dict['--periods'])
        credit_interest = float(parameter_dict['--interest'])
        i = (credit_interest / 100) / 12

        credit_principal = monthly_payment / ((i * (1 + i) ** n_of_periods) / ((1 + i) ** n_of_periods - 1))

        print('Your credit principal = {0} !'.format(credit_principal))

elif parameter_dict['--type'] == 'diff' and len(parameter_dict) == 4 and '--payment' not in parameter_dict:
    credit_principal = int(parameter_dict['--principal'])
    n_of_periods = int(parameter_dict['--periods'])
    credit_interest = float(parameter_dict['--interest'])
    i = (credit_interest / 100) / 12
    sum_of_payments = 0

    for month in range(1, n_of_periods+1):
        D = (credit_principal / n_of_periods) + i * (credit_principal - ((credit_principal * (month - 1)) / n_of_periods))
        print('Month {0}: payment is {1}'.format(month, math.ceil(D)))
        sum_of_payments += math.ceil(D)

    if sum_of_payments > credit_principal:
        print('Overpayment = {}'.format(sum_of_payments - credit_principal))
    else:
        pass

else:
    print('Incorrect parameters')