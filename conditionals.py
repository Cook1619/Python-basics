
temp = 19

if temp > 30:
    print('ITS TRUE')
elif temp > 20:
    print('Its a little cooler')
else:
    print('Its cold')
print('Done')


# age = 12

# message = "Eligible" if age >= 18 else "Not Eligible"
# print(message)

high_income = False
good_credit = True
student = True
if (high_income and good_credit) and not student:
    print('You\'re approved')
else:
    print('Not approved')
