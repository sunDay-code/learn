"""
Singleton
    A "singleton" object: the lone object returned by
    its class every time the class is called

Reference: https://python-patterns.guide/gang-of-four/singleton/
"""


class Logger(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(Logger, cls).__new__(cls)
            # Put any initialization here.
        return cls._instance


def _main():
    log1 = Logger()
    print(log1)

    log2 = Logger()
    print(log2)

    print("Are they the same object? ", log1 is log2)


if __name__ == "__main__":
    _main()