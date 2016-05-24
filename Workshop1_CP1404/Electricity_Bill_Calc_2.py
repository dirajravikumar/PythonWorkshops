print('Electricity Bill Estimator 2.0')

tariff_calc = int(input('Which tariff? 11 or 31:'))
daily_use = float(input('Enter daily use in kWh:'))
bill_days = int(input('Enter number of billing days:'))


TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

#estimated_bill = float(cents * daily_use * bill_days)/100

if tariff_calc == 11:
   print('Estimated bill: $', float(daily_use * bill_days * TARIFF_11))
elif tariff_calc ==31:
    print('Estimated bill: $', float(daily_use * bill_days * TARIFF_31))
else:
    print('No other tarrif exists')