def print_line(the_func):
    def wrapper():
        print('')
        print('=' * 50)

        the_func()
    return wrapper
