def test():
    def square():
        x = 10
    def rect():
        nonlocal x
        x = 20
    def glo():
        global x
        x = 30
    x = 0
    print(x)
    square()
    print(x)
    rect()
    print(x)
    glo()
    print(x)

test()
print(x)
