def add(x,y):
    add_answer = x + y
    print (f'Your answer is {add_answer}')

def sub(x,y):
    sub_answer = x - y
    print (f'Your answer is {sub_answer}')

def div(x,y):
    div_answer = x/y
    print (f'Your answer is {div_answer}')

def mul(x,y):
    mul_answer = x * y
    print (f'Your answer is {mul_answer}')

def operation_input():
    calc = input("Please select one of the following options you would like to perform \n For addition type \'A\' \n For subtraction type \'S\' \n For multiplication type \'M\' \n For division type \'D\'\n")
    if len(calc.lower()) == 1:
        if calc.isalpha() == True and  calc in ['a','s','m','d']:        
            print ('Next lets enter the values you wish to use in the calculation')
            value_input(calc)
        elif calc.isalpha == True:
            print (f'You have entered {calc} which is not valid operation letter, lets try again')
        else:
            print(f'You have entered {calc} which is not a letter lets try that again')
    elif len(calc) > 1:
        print(f'You have entered {calc} which is too many letter/value, lets try again')
    else:
        raise ValueError('You have not entered any characters lets try that again')

def value_input(calc):
    x = input("Please enter the first value for your calculation\n")
    y = input("Please enter the second value for your calculation\n")
    if x.isnumeric() == True and y.isnumeric() == True:
        x = int(x)
        y = int(y)
        if calc == 'a':
            add(x,y)
        elif calc == 's':
            sub(x,y)
        elif calc == 'm':
            mul(x,y)
        else:
            div(x,y)
    else:
        raise TypeError('You have not entered a numerical value, lets try again')

if __name__ == "__main__":
    operation_input()