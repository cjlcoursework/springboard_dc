#!/bin/python3

import math
import os
import random
import re
import sys


def longest_segment(string):
    n = list(map(lambda x: int(x), string.split()))
    lower_bound = n[0]
    upper_bound = n[1]
    bad_numbers = n[2:]
    segment = []
    long_segment = []

    for i in range(lower_bound, upper_bound + 1):
        if i in bad_numbers:
            this_len = len(segment)
            if this_len > len(long_segment):
                long_segment = segment
            segment = []
        else:
            segment.append(i)

    if len(segment) > len(long_segment):
        long_segment = segment

    print(len(long_segment))


if __name__ == '__main__':
    # n = input().strip()

    longest_segment("1 10 5 4 2 15")
