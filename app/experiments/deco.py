def decorated_by(func):
    func.__doc__ = '\nDecorated by decorated_by.'
    return func

@decorated_by
def say():
    print('hola')


if __name__ == '__main__':
    say()
    print(say.__doc__)


