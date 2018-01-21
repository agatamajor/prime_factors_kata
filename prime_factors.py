import unittest

def get_prime_factors(number):
    list = []
    if number != 1:
        list.append(number)
    return list

assert get_prime_factors(1) == []
assert get_prime_factors(2) == [2]
assert get_prime_factors(3) == [3]



