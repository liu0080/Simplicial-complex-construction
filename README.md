# Simplicial-complex-construction
This project is to construct certain types of simplicial complex, including Cech simplex and α-simplex, which are important in topological data analysis

To use these functions,

All points should have type np.array()

P is a set of points under the form of a list of array

-MEB(P)  returns the minimal enclosing ball of P (center and radius) , the radius is the filtration value mentioned in Task 1

-cechNaive(P,k) takes a list of array, an integer and returns a list of all simplex (dimension less than k) of P

-cechEfficient(P, k, l) takes a list of array, an integer and float number, and returns a list of all simplex (dimension less than k, filtration value less than l) of P with their filtration values.

-verification(P,A) takes a list of array P, a sub list of P, and returns the alpha-simplex of A in P
 radias is the filtration value mentioned in Task4; or a big number A is not in the alpha-complex.

-alpha(P, k, l) takes a list of array P, a integer k, a floating number l, and returns all alpha-simplex (dimention  at most k, filtration less than l) in P and their filtration value(less than l)

