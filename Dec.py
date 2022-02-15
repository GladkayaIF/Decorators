import datetime

def logger(path):
    def decorator(old_function):
        def new_function(*args, **kwargs ):
            old_return = old_function(*args, **kwargs)
            out_line = 'datetime call function = ' + str(datetime.datetime.today()) + '\n'
            out_line += 'name function = ' + str(old_function) + '\n'
            out_line += '*args function = '+str(*args)+'\n'
            out_line += '**kwargs function = ' + str(**kwargs) + '\n'
            out_line += 'return function = '+str(old_return)
            with open(path, mode='w', encoding="utf8") as f:
                f.write(out_line)
                f.close()
            return old_return
        return new_function
    return decorator

@logger("C:/Users/axata/PycharmProjects/pythonProject/Decorators/logger_Dec.txt")
def foo(x):
    multy = 10
    print('foo')
    return x*multy

foo(5)