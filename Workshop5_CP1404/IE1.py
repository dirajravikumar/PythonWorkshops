number_IE1 = []
maxLengthList = 5
while len(number_IE1) < maxLengthList:
    number = input("Number: ")
    number_IE1.append(number)

average = sum([int(i) for i in number_IE1])/maxLengthList

print("The first number is {}".format(number_IE1[0]))
print("The last number is {}".format(number_IE1[-1]))
print("The smallest number is {}".format(min(number_IE1)))
print("The largest number is {}".format(max(number_IE1)))
print("The average of the numbers is {}".format(average))