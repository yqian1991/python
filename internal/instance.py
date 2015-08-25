class A:
    #a
    b = 1
    c = "b"
    def __init__(self, d):
        self.d = d
    pass

a = A(1)
print a.__dict__
print A.b
print a.d
print a.__class__
print a.__repr__
