
# ? Special Methods:
                    # ! Special Methods are those method which are run when class is made

                    # ? some of the special methods are:
                    # ^ 1.__init__
                    # ^ 2.__new__
                    # ^ etc......

                    # nfttrt








class Students :
    def __new__(cls):
        print('welcome to init method new method')
        obj = super().__new__(cls)
        return obj

    def __init__(self):
        print('welcome to init method')
s1 =Students()