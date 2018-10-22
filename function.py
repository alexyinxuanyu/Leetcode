def one(b):
    def f2(a):
        print("two")

    print("one")
def f2():
    print("two")
one(3)
#one()()
w=one(3)(2)
