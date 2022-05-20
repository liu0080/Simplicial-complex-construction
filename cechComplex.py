# -*- coding: utf-8 -*-

import numpy as np
import random as rd
import itertools


def mid(a,b):        # midpoint of two points
    return (a+b)/2

def dis(a,b):       # distance between two points
    return np.linalg.norm(a-b)

def inball(a,ball):     # verify if the point a is in a given ball represented by its center(ball[0]) and radius(ball[1])
    return dis(a,ball[0]) < ball[1]

def circumball(P): # calculate the circumball of a set of at most 4 points
    n = len(P)
    if n == 0:
        return np.array([0,0,0]), 0
    if n == 1:
        return P[0], 0
    if n == 2:
        return (P[0]+P[1])/2, np.around(dis(P[0],P[1])/2, 5)
    if n == 3:
        A = [[],[],[1,1,1]]         # Set c = xP1+yP2+zP3. As they are coplanar, we get x+y+z=1;
        for i in range(2):          # by the property of circumcenter, we have (c-mid(Pi,Pj))*(Pi-Pj)=0
            for j in range(3):      # By solving the linear system, we get the circumcenter.
                A[i].append(np.dot(P[j],P[i]-P[i+1]))
        A = np.array(A)
        b = np.array([np.dot(P[0]+P[1],P[0]-P[1])/2, np.dot(P[1]+P[2],P[1]-P[2])/2, 1])
        bary = np.linalg.solve(A, b)
        c = bary[0]*P[0] + bary[1]*P[1] + bary[2]*P[2]
        r = dis(c, P[0])
        return np.around(c,5), np.around(r,5)
    if n == 4:      # calculate the circumball of a 4-point set, with the same idea in 3-point condition
        A = [[],[],[],[1,1,1,1]]
        for i in range(3):
            for j in range(4):
                A[i].append(np.dot(P[j],P[i]-P[i+1]))
        A = np.array(A)
        b = np.array([np.dot(P[0]+P[1],P[0]-P[1])/2, np.dot(P[1]+P[2],P[1]-P[2])/2, np.dot(P[2]+P[3],P[2]-P[3])/2, 1])
        bary = np.linalg.solve(A, b)
        c = bary[0]*P[0] + bary[1]*P[1] + bary[2]*P[2] + bary[3]*P[3]
        r = dis(c, P[0])
        return np.around(c,5), np.around(r,5)
    


 


def MEBOrigin(P, R, n):   
    """
    input: 2 list of points P et R avec |R| <= 4, integer n
    output: the minimal enclosing ball of P[:n], with R on its boundary, represented by its center (a list) and radius (a floating number)
    """

    if (n == 0 or len(R) == 4) :
        return circumball(R)
    p=P[n-1]

    d = MEBOrigin(P, R.copy(), n - 1)
 
    if inball(p,d):
      return d 
    
    R.append(p)
    return MEBOrigin(P, R.copy(), n - 1)

def MEB(P):     # calculate the MEB of a set P
    P_copy=P.copy()
    rd.shuffle(P_copy)
    return MEBOrigin(P, [],len(P))

"""
    Tests for MEB
"""
# a = np.array([-10,0,0])
# b = np.array([10,0,0])
# c = np.array([0,1,0])
# print(MEB([a]))
# print(MEB([a,b]))
# print(MEB([a,b,c]))

# print()
# a = np.array([-5,0,0])
# b = np.array([3,-4,0])
# c = np.array([3,4,0])
# print(MEB([a,b,c]))

# print()
# a = np.array([5,0,1])
# b = np.array([-1,-3,4])
# c = np.array([-1,-4,-3])
# d = np.array([1,4,-3])
# print(MEB([a,b,c,d]))

def filtration(simplex):   # return the filtration value of a simplex, which we use to sort the complex
    return simplex[-1]

def cechNaive(P, k):       # we construct C^k in a naive way
    complex = []
    for i in range(k+1):      # visit all tuples of at most k+1 points
        for R in itertools.combinations(range(len(P)), i+1):  
            r=[]
            for i in R:
                r.append(P[i])
            complex.append([R,MEB(r)[1]])
    complex.sort(key=filtration)
    return complex

# a=np.array([5,0,1])
# b=np.array([-1,-3,4])
# c=np.array([-1,-4,-3])
# d=np.array([-1,4,-3])
# e=np.array([0,0,0])
# P=[a,b,c,d,e]

# for i in cechNaive(P,5):
#     print(i)
                   

def cechEfficient(P, k, l):   # we construct C^k_l in a more efficient way
    complex = []
    Graph = {}      # use a dictionary to construct a graph with vertices in P, 
    n = len(P)      # where their is a edge between u,v if dis(u,v) < l
    for i in range(n):     # but there is a trick: in the adjacency list of a point u, we just keep those u whose index in P is bigger than v's, to avoid repeated calculation
        Graph[i] = []    
        complex.append([[i],0])
        
    for (i,j) in itertools.combinations(range(n),2):
        if dis(P[i],P[j])/2 < l:
                Graph[i].append(j)
               
    for d in range(1,k):
        for i in range(n):
            candidate = Graph[i]
            for nlist in itertools.combinations(candidate, d):   # to check if a d+1-simplex is in C^k_l           
                nlist=list(nlist)
                dSimplex=[P[i]] 

                for j in nlist:
                    dSimplex.append(P[j])
                nlist.insert(0,i)
                r = MEB(dSimplex)[1]
                if r < l:
                    complex.append([nlist, r])

    complex.sort(key=filtration)
    return complex



# a=np.array([5,0,1])
# b=np.array([-1,-3,4])
# c=np.array([-1,-4,-3])
# d=np.array([-1,4,-3])
# e=np.array([0,0,0])
# P=[a,b,c,d,e]

# for i in cechEfficient(P,5,5):
#     print(i)






