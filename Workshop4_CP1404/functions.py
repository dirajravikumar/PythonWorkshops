def rectangle_area():
    """
    This function calcuates the area of a rectangle.
    :param height: Height of thy rectangle
    :param width: Width of thy rectangle
    :return: Area of thy rectangle
    """
    height = int(input("Enter the height of rectangle:"))
    width = int(input("Enter the width of rectangle:"))
    area = print("The area of rectangle is",height * width)
    return area

def C2F():
    """
    This function converts Celsius value to Fahrenheit.
    :param celsius_Value: Enter thy Celsius Value
    :return:
    """
    celsius_Value = (float(input("Enter your Celsius value:")))
    fahrenheitValue = celsius_Value * 9 / 5 + 32
    F = print('Fahrenheit Value:', fahrenheitValue,'º')

    return F

def BMI():
    """
    This function gives out BMI index of the user.
    :param weight: Weight of thy user
    :param height: Height of thy user
    :return:
    """
    weight = int(input('Please enter your weight in kgs:'))
    height = float(input('Please enter your height in m:'))
    bmi = print("Your BMI value is:", weight / height ** 2)

    return  bmi

rectangle_area()
BMI()
C2F()