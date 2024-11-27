names =  ['Matt O' , 'Hoyam' , 'Sayed']
assignments =  [ 0,2,3]
grades =  [12,14,19]

## message string to be used for each student
## HINT: use .format() with this string in your for loop
for x in range(3):
    print('Hi {},\n\nThis is a reminder that you have {} assignments left to \
    submit before you can graduate. Your current grade is {} and can increase \
    to {} if you submit all assignments before the due date.\n\n'.format(names[x],assignments[x],grades[x], 20))

## write a for loop that iterates through each set of names, assignments, and grades to print each student's message