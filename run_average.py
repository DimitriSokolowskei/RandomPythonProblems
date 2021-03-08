def run_timing():
    time = int(input('How many times did you run this week?'))
    total_km = 0

    for i in range(1, time + 1):
        run = float(input('How many km did you run in the {}° day?'.format(i)))
        total_km += run
    average = total_km / time
    print('I ran an average of {} km in {} days.'.format(average, time))

print(run_timing())
