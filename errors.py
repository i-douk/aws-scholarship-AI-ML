try: 
    x = int(input('Enter a number: '))
except ValueError:
    print('That is not a valid number')
finally:
    print('\n Attempted Input\n')