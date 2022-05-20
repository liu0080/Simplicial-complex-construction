# -*- coding: utf-8 -*-

import numpy as np
import random as rd
import itertools
from scipy import spatial   # to construct kD-tree

import cechComplex

MAX = 1000000       # a number large enough

def MEB_alpha(P, R, n):
    """
    input: P a list of arrays (points), R a sublist of P which forms a simplex, n a integer not larger than len(P)
    output: the minimal ball with R on its boundary and contain no points of P[:n] if it exists; if not, output MAX with array([0,0,0])
    """

    if len(R)>4 :
      return np.array([0,0,0]), MAX
    if n==0:
      return cechComplex.circumball(R)

    p=P[n-1]
    
    D = MEB_alpha(P, R.copy(), n - 1)

    # if p in R
    if (R == p).all(1).any():
      return D
  
    if D[1] == MAX:
      return D
    if not cechComplex.inball(p,D):
      return D
    
    R.append(p)
    return MEB_alpha(P, R.copy(), n - 1)


def verification(P,A):      # verify if the simplex constructed by A is in the alpha-complex
    P_copy = P.copy()
    rd.shuffle(P_copy)
    A_copy=A.copy()
    return MEB_alpha(P_copy, A_copy, len(P_copy))[1]

 
# def test4(P,A):
#     a= verification(P,A)
#     if a==MAX:
#         print('not in the alpha complex')
#     else:
#         print('filtration value: ' + str(a))


# a=np.array([5,0,1])
# b=np.array([-1,-3,4])
# c=np.array([-1,-4,-3])
# d=np.array([-1,4,-3])
# e=np.array([0,0,0])
# f=np.array([5,0,3])
# P=[a,b,c,d,e]
# A=[a,b,c]
# test4(P,A)



def alpha(P, k, l):
    """
    input: P a list of arrays (points), k a integer who marks the upperbound of dimension, l the limite of filtration value
    output: all the simplexes of at most k dimension, filtration value less than l, together with their filtration values.
    """
    alpha = {}
    n = len(P)
    k = min(k,3)
    for d in range(k+1, 0, -1):
        for i in itertools.combinations(range(n), d):
            R = [P[i[j]] for j in range(len(i))]
            filtration_value = verification(P, R)
            if filtration_value < MAX:
                alpha[i] = filtration_value
    alpha = dict(sorted(alpha.items(),key = lambda x:x[1]))
    return alpha

# x1 = np.array([0,5,0])
# x2 = np.array([3,4,0])
# x3 = np.array([-3,4,0])
# x4 = np.array([0,0,4])
# x5 = np.array([0,0,-4])
# P = [x1,x2,x3,x4]
# Q = [x1,x2,x3,x4,x5]  

# print(alpha(P,2,10))