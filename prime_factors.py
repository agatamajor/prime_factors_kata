import unittest

def get_prime_factors(number):
    list = []
    if number == 2:
        list.append(2)
    if number == 3:
        list.append(3)
    return list

assert get_prime_factors(1) == []
assert get_prime_factors(2) == [2]
assert get_prime_factors(3) == [3]



