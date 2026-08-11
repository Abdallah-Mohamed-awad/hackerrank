#!/bin/python3

import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

text = ""

for column in range(m):
    for row in range(n):
        text += matrix[row][column]

text = re.sub(r'(?<=\w)[^\w]+(?=\w)', ' ', text)
print(text)
