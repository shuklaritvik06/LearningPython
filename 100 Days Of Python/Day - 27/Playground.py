def add(*args):
    sum = 0
    for item in args:
        sum += item
    print(sum)


add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def addmul(**kwargs):
    return kwargs["a"]+kwargs.get("b")*kwargs.get("c")


print(addmul(a=34, b=35, c=53))
