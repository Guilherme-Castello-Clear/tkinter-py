# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
# print(add(3, 5, 7, 8))

def calculate(n, **kwargs):
    # for key, value in kwargs.item()
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")

my_car = Car(make="Nissan")
print(my_car.model)
