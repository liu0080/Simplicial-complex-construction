# -*- coding: utf-8 -*-

import numpy as np
import cechComplex
import alphaComplex
MAX = 1000000

"""
Test cases for MEB
"""
# a = np.array([-10,0,0])
# b = np.array([10,0,0])
# c = np.array([0,1,0])
# print(cechComplex.MEB([a]))
# print(cechComplex.MEB([a,b]))
# print(cechComplex.MEB([a,b,c]))

# print()
# a = np.array([-5,0,0])
# b = np.array([3,-4,0])
# c = np.array([3,4,0])
# print(cechComplex.MEB([a,b,c]))

# print()
# a = np.array([5,0,1])
# b = np.array([-1,-3,4])
# c = np.array([-1,-4,-3])
# d = np.array([1,4,-3])
# print(cechComplex.MEB([a,b,c,d]))


"""
Test cases for cechNaive
"""
# a=np.array([5,0,1])
# b=np.array([-1,-3,4])
# c=np.array([-1,-4,-3])
# d=np.array([-1,4,-3])
# e=np.array([0,0,0])
# P=[a,b,c,d,e]

# for i in cechComplex.cechNaive(P,5):
#     print(i)

"""
Test cases for cechEfficient
"""
# a=np.array([5,0,1])
# b=np.array([-1,-3,4])
# c=np.array([-1,-4,-3])
# d=np.array([-1,4,-3])
# e=np.array([0,0,0])
# P=[a,b,c,d,e]

# for i in cechComplex.cechEfficient(P,5,5):
#     print(i)

"""
Test cases for verification
"""
 
# def test4(P,A):
#     a= alphaComplex.verification(P,A)
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

"""
Test cases for alpha
"""
x1 = np.array([0,5,0])
x2 = np.array([3,4,0])
x3 = np.array([-3,4,0])
x4 = np.array([0,0,4])
x5 = np.array([0,0,-4])
P = [x1,x2,x3,x4]
Q = [x1,x2,x3,x4,x5]
alpha = alphaComplex.alpha(P,2,10)  
for i in alpha.keys():
  print(str(i)+' -> '+str(alpha[i]))