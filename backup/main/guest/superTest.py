class A(object):
    def who_am_i(self):
        print("I am a A")
    # pass

class B(A):
    # def who_am_i(self):
    #     print("I am a B")
    pass

class C(A):
    def who_am_i(self):
        print("I am a C")

class D(B,C):
    # def who_am_i(self):
    #     print("I am a D")
    pass

d1 = D()
d1.who_am_i()