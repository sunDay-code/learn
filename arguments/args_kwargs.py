"""
Reference:
    1. https://www.geeksforgeeks.org/args-kwargs-python/
    2. https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters
"""

"""
*args

The special syntax *args in function definitions in python is 
used to pass a variable number of arguments to a function. It is 
used to pass a non-key worded, variable-length argument list. 

The syntax is to use the symbol * to take in a variable number of arguments;
by convention, it is often used with the word args. What *args allows you to 
do is take in more arguments than the number of formal arguments that you 
previously defined. With *args, any number of extra arguments can be tacked on 
to your current formal parameters (including zero extra arguments).
For example : we want to make a multiply function that takes any number of 
arguments and able to multiply them all together. It can be done using *args.
Using the *, the variable that we associate with the * becomes an iterable meaning
you can do things like iterate over it, run some higher-order functions such as map 
and filter, etc.

The *args will give you all function parameters as a tuple
"""


def args_func(*argv):
    for arg in argv:
        print("*arg ", arg)


def args_func2(arg1, *argv):
    print("arg1", arg1)
    for arg in argv:
        print("*arg ", arg)


"""
**kwargs

The special syntax **kwargs in function definitions in python is used to pass a keyworded, 
variable-length argument list. We use the name kwargs with the double star. The reason is because 
the double star allows us to pass through keyword arguments (and any number of them).
"""


def kwargs_func(arg1, **kwargs):
    print('arg: %s' % arg1)

    for key, value in kwargs.items():
        print("kwargs: %s == %s" % (key, value))


def kwargs_func2(**kwargs):
    for a in kwargs:
        print(a, kwargs[a])


def foo(a, b, c):
    print(a, b, c)


def _main():
    print("Calling ", args_func.__name__)
    args_func('Hello', 'World', 'To', 'You')

    print("Calling ", args_func2.__name__)
    args_func2('Hello', 'World', 'To', 'You')

    print("Calling ", kwargs_func.__name__)
    kwargs_func(arg1='Hello', arg2='World', arg3='To', arg4='You')

    print("Calling ", kwargs_func2.__name__)
    kwargs_func2(name='one', age=27)

    # Another usage
    obj = {'b': 10, 'c': 'hello'}
    print("Calling ", foo.__name__)
    foo(100, **obj)


if __name__ == "__main__":
    _main()
