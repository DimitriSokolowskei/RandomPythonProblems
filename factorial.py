num = int(input('Insert a number:'))
fat = 1
for num in range(1, num + 1):
    fat *= num
print('The factorial of {} is {}.'.format(num, fat))
