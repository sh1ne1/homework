try:
    firstch = int(input())
    secondch = int(input())
    act = input()
    if secondch == 0 and act == '/':
        raise ZeroDivisionError()
except ValueError:
    print('must be integer!')
except ZeroDivisionError:
    print('you can`t divide on zero')
else:
    if act == '/':
        print(firstch / secondch)
    elif act == '+':
        print(firstch + secondch)
    elif act == '-':
        print(firstch - secondch)
    elif act == '*':
        print(firstch * secondch)
