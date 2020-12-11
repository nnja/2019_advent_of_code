from util import *

data = get_data(1)


def fuel(mass):
    """
    to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.
    """
    return int(int(mass) / 3) - 2


def p1(data):
    return sum(fuel(mass) for mass in data)


def infinite_fuel(mass):
    """
    So, for each module mass, calculate its fuel and add it to the total. Then, treat the fuel amount you just calculated as the input mass and repeat the process, continuing until a fuel requirement is zero or negative. For example:
    """
    total_fuel = 0

    while fuel(mass) > 0:
        fuel_amount = fuel(mass)
        total_fuel += fuel_amount
        mass = fuel_amount

    return total_fuel

def p2(data):
    return sum(infinite_fuel(mass) for mass in data)


def test():

    data = """
    """

    run_tests(fuel, [(12, 2)])
    run_tests(fuel, [(14, 2)])
    run_tests(fuel, [(1969, 654)])
    run_tests(fuel, [(100756, 33583)])
    run_tests(infinite_fuel, [(14, 2)])
    run_tests(infinite_fuel, [(1969, 966)])
    run_tests(infinite_fuel, [(100756, 50346)])


test()
print("Result1:", p1(data))
print("Result2:", p2(data))
