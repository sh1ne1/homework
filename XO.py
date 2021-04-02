import random

field = {
         1: '_', 2: '_', 3: '_',
         4: '_', 5: '_', 6: '_',
         7: '_', 8: '_', 9: '_',
        }


def print_field(field):
    beuty_field = ' _ ' + '_ ' + '_ ' + '\n'
    for keys, values in field.items():
        if keys == 2 or keys == 5 or keys == 8:
            beuty_field += '|' + values + '|'
        elif keys == 3 or keys == 6 or keys == 9:
            beuty_field += values + '|' + '\n'
        elif keys == 1 or keys == 4 or keys == 7:
            beuty_field += '|' + values
    return beuty_field


def make_move(field, field_type, cords):
    if int(cords) > 9:
        return field, False
    field_flag = [field, 'True']
    if field[int(cords)] != '_':
        return field, False
    field[int(cords)] = field_type
    return field_flag


def bot(field):

    while True:
        random_cords = random.randint(1, 9)
        if field[random_cords] == '_':
            field[random_cords] = '0'
            return field, True


def winning(field):
    flag = False
    if field[1] == 'X' and field[2] == 'X' and field[3] == 'X':
        return flag
    elif field[4] == 'X' and field[5] == 'X' and field[6] == 'X':
        return flag
    elif field[7] == 'X' and field[8] == 'X' and field[9] == 'X':
        return flag
    elif field[1] == 'X' and field[4] == 'X' and field[7] == 'X':
        return flag
    elif field[2] == 'X' and field[5] == 'X' and field[8] == 'X':
        return flag
    elif field[3] == 'X' and field[6] == 'X' and field[9] == 'X':
        return flag
    elif field[1] == 'X' and field[5] == 'X' and field[9] == 'X':
        return flag
    elif field[3] == 'X' and field[5] == 'X' and field[7] == 'X':
        return flag
    elif field[1] == '0' and field[2] == '0' and field[3] == '0':
        return flag
    elif field[4] == '0' and field[5] == '0' and field[6] == '0':
        return flag
    elif field[7] == '0' and field[8] == '0' and field[9] == '0':
        return flag
    elif field[1] == '0' and field[4] == '0' and field[7] == '0':
        return flag
    elif field[2] == '0' and field[5] == '0' and field[8] == '0':
        return flag
    elif field[3] == '0' and field[6] == '0' and field[9] == '0':
        return flag
    elif field[1] == '0' and field[5] == '0' and field[9] == '0':
        return flag
    elif field[3] == '0' and field[5] == '0' and field[7] == '0':
        return flag
    return True

def game_for_two(field):
    field_type = 'X'
    print(print_field(field))
    while winning(field):
        print('time to move:' f'{field_type}')
        cords = input('cords')
        flag = make_move(field, field_type, cords)
        if flag[1]:
            field[cords] = field_type
            print(print_field(field))
            if field_type == 'X':
                field_type = '0'
            elif field_type == '0':
                field_type = 'X'
        else:
            print('this place is taken! Try again')
    v = input('do u want play again? (yes/no)')
    if v == 'yes':
        field = {
            1: '_', 2: '_', 3: '_',
            4: '_', 5: '_', 6: '_',
            7: '_', 8: '_', 9: '_',
        }
        print(game_with_bot(field))


def game_with_bot(field):
    field_type = 'X'
    print(print_field(field))
    while winning(field):
        print('time to move:' f'{field_type}')
        if field_type == 'X':
            cords = input('cords')
            flag = make_move(field, field_type, cords)
        elif field_type == '0':
            flag = bot(field)
        if flag[1]:
            field[cords] = field_type
            print(print_field(field))
            if field_type == 'X':
                field_type = '0'
            elif field_type == '0':
                field_type = 'X'
        else:
            print('this place is taken! Try again')
    v = input('do u want play again? (yes/no)')
    if v == 'yes':
        field = {
                1: '_', 2: '_', 3: '_',
                4: '_', 5: '_', 6: '_',
                7: '_', 8: '_', 9: '_',
                }
        print(game_with_bot(field))

starter = input('with who do you want to play?(bot or 1v1):')
if starter == 'bot':
    print(game_with_bot(field))
elif starter == '1v1':
    print(game_for_two(field))
