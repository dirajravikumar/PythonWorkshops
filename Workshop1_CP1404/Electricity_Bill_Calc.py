print('Electricity Bill Estimator')

cents = int(input('Enter cents per kWh:'))
daily_use = float(input('Enter daily use in kWh:'))
bill_days = int(input('Enter number of billing days:'))

estimated_bill = float(cents * daily_use * bill_days)/100


print("Estimated bill: ${:.2f}".format(estimated_bill))