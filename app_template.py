def add():
    add_answer = x + y
    return add_answer

def sub():
    sub_answer = x - y
    return sub_answer

def div():
    div_answer = x/y
    return div_answer

def mul():
    mul_answer = x * y
    return mul_answer

def calculation():
    calc = input("Please select one of the following options you would like to perform \n For addition type \'A\' \n For subtraction type \'S\' \n For multiplication type \'M\' \n For division type \'D\'")
    if len(calc) == 1:
        if calc.isalpha() == True:
            return print ('Next lets enter the values you wish to use in the calculation')
        else:
            return print('You have not entered a letter lets try that again')
    else:
        return print('You have entered too many characters lets try that again')
