print('Body-Mass-Index Calculator')

weight = int(input('Please enter your weight in kgs:'))
height = float(input('Please enter your height in m:'))
bmi = weight / height ** 2

print("Your BMI value is:", bmi)