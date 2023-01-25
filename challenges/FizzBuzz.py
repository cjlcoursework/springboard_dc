#!/bin/python3

import math
import os
import random
import re
import sys


def fizzBuzz(n):
    # Write your code here
    for i in range(1, n+1):
        # print("\t",i)
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)


if __name__ == '__main__':
    # n = int(input().strip())

    fizzBuzz(15)