class Borg:
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state

b1 = Borg()
b2 = Borg()
print id(b1) == id(b2)
