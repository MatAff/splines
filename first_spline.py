#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# Start line segment
x1 = 0
y1 = 0
x2 = -0.25
y2 = 1

# End line segment
x3 = 10
y3 = 10
x4 = 11
y4 = 10

A = np.matrix([x1,y1])
B = np.matrix([x2,y2])
C = np.matrix([x3,y3])
D = np.matrix([x4,y4])

def intersect(A, B, C, D):
    CA = A - C
    AB = B - A
    CD = D - C
    s = np.cross(CA,AB) / np.cross(CD, AB)
    return(C + s * CD)

def rel_line(S, E, ratio):
    return(S + (E - S) * ratio)

# Compute intersect
I = intersect(A, B, C, D)
print(I)    

# Loop and calculate spline points
n = 100
spline_points = np.zeros((n,2))
for i in range(n):
    ratio = i / (n-1)
    S = rel_line(B, I, ratio)
    E = rel_line(I, C, ratio)
    P = rel_line(S, E, ratio)
    spline_points[i,0] = P[0,0]
    spline_points[i,1] = P[0,1]

print(spline_points)    

def plot_matrix(M):
    for i in range((M.shape[0] - 1)):
        plt.plot([M[i, 0], M[i + 1, 0]],
                 [M[i, 1], M[i + 1, 1]],
                 'k-')
    plt.show()

plot_matrix(spline_points)