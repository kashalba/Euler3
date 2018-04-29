#!/bin/python3

import sys
import math
import unittest


def divide_till_possible(n, divisor) :
    prime_factor = 1
    while(n % divisor == 0):
        prime_factor = divisor
        n//=divisor
    return n, prime_factor

def find_largest_prime_factor(n) :
    if n < 2 :
        return 1
    n,largest_prime_factor = divide_till_possible(n,2)
    if n > 2 :
        divisor = 3
        while(divisor <= math.sqrt(n)):
            n,largest_prime_factor = divide_till_possible(n,divisor)
            divisor+=2
    return(max(largest_prime_factor,n))

class TestLargestPrimeFactorMethods(unittest.TestCase):

    def test_zero_should_return_one(self):
        self.assertEqual(1, find_largest_prime_factor(0))

    def test_one_should_return_one(self):
        self.assertEqual(1, find_largest_prime_factor(1))

    def test_two_should_return_two(self):
        self.assertEqual(2, find_largest_prime_factor(2))

    def test_three_should_return_three(self):
        self.assertEqual(3, find_largest_prime_factor(3))

    def test_four_should_return_two(self):
        self.assertEqual(2, find_largest_prime_factor(4))

    def test_five_should_return_five(self):
        self.assertEqual(5, find_largest_prime_factor(5))

    def test_six_should_return_three(self):
        self.assertEqual(3, find_largest_prime_factor(6))

    def test_eight_should_return_two(self):
        self.assertEqual(2, find_largest_prime_factor(8))

    def test_nine_should_return_three(self):
        self.assertEqual(3, find_largest_prime_factor(9))

    def test_ten_should_return_five(self):
        self.assertEqual(5, find_largest_prime_factor(10))

    def test_fifteen_should_return_five(self):
        self.assertEqual(5, find_largest_prime_factor(15))

    def test_eighteen_should_return_three(self):
        self.assertEqual(3, find_largest_prime_factor(18))

    def test_13195_should_return_29(self):
        self.assertEqual(29, find_largest_prime_factor(13195))

if __name__ == '__main__':
    unittest.main()