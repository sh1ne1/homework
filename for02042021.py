name = ['kek', ' lol', 'lel', 'ti kot']


def generator(names):
    for i in names:
        activate_word = yield
        if activate_word == 'nextone':
            yield i


func = generator(name)


while True:
    d = input('do u want next one?')
    if d == 'yes':
        next(func)
        print(func.send('nextone'))
