###
# Test pass check
#
total_tasks = int(input('Enter the total number of tasks: '))
correct_tasks = int(input('Enter the number of correctly completed tasks: '))

if correct_tasks >= total_tasks / 2:
    print('Test passed')
else:
    print('Test failed')
