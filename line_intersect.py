#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

# https://www.quora.com/How-do-I-get-the-point-of-intersection-of-two-lines-using-a-cross-product-if-I-know-two-points-of-each-line

x1 = 0
y1 = 0
x2 = 1
y2 = 1

x3 = 4
y3 = 1
x4 = 5
y4 = 0

l1 = [[x1,y1],
      [x2,y2]]

A = np.matrix([x1,y1])
B = np.matrix([x2,y2])
C = np.matrix([x3,y3])
D = np.matrix([x4,y4])

def compute_intersect(A, B, C, D):
    CA = A - C
    AB = B - A
    CD = D - C
    s = np.cross(CA,AB) / np.cross(CD, AB)
    return(C + s * CD)

print(compute_intersect(A, B, C, D))