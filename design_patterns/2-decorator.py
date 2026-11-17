#!/usr/bin/env python3

"""
Decorator Design Pattern - Coffee Shop
"""


class Coffee:
    def cost(self):
        return 50

    def description(self):
        return "Coffee"


class MilkDecorator:
    def __init__(self, beverage):
        self._inner = beverage

    def cost(self):
        return self._inner.cost() + 10

    def description(self):
        return self._inner.description() + " + milk"


class SugarDecorator:
    def __init__(self, beverage):
        self._inner = beverage

    def cost(self):
        return self._inner.cost() + 5

    def description(self):
        return self._inner.description() + " + sugar"


class CaramelDecorator:
    def __init__(self, beverage):
        self._inner = beverage

    def cost(self):
        return self._inner.cost() + 15

    def description(self):
        return self._inner.description() + " + caramel"


def main():
    beverage1 = MilkDecorator(Coffee())
    print(beverage1.description(), beverage1.cost())

    beverage2 = MilkDecorator(SugarDecorator(Coffee()))
    print(beverage2.description(), beverage2.cost())

    beverage3 = CaramelDecorator(
        MilkDecorator(
            SugarDecorator(
                Coffee()
            )
        )
    )
    print(beverage3.description(), beverage3.cost())


if __name__ == "__main__":
    main()
