# version code 761
# Please fill out this stencil and submit using the provided submission script.

from vec import Vec
from GF2 import one
from itertools import product

## Problem 1
def vec_select(veclist, k): 
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_select([v1, v2, v3, v4], 'a') == [Vec(D,{'b': 1}), Vec(D,{'b': 2})]
    True
    '''
    return [vec for vec in veclist if vec[k] == 0]

def vec_sum(veclist, D): 
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_sum([v1, v2, v3, v4], D) == Vec(D, {'b': 13, 'a': 11})
    True
    '''
    return sum(veclist, Vec(D, {}))

def vec_select_sum(veclist, k, D): 
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_select_sum([v1, v2, v3, v4], 'a', D) == Vec(D, {'b': 3})
    True
    '''
    return vec_sum(vec_select(veclist, k), D)



## Problem 2
def scale_vecs(vecdict):
    '''
    >>> v1 = Vec({1,2,3}, {2: 9})
    >>> v2 = Vec({1,2,4}, {1: 1, 2: 2, 4: 8})
    >>> scale_vecs({3: v1, 5: v2}) == [Vec({1,2,3},{2: 3.0}), Vec({1,2,4},{1: 0.2, 2: 0.4, 4: 1.6})]
    True
    '''
    return [vecdict[vec] / vec for vec in vecdict]


## Problem 3
def GF2_span(D, L):
    '''
    >>> from GF2 import one
    >>> D = {'a', 'b', 'c'}
    >>> L = [Vec(D, {'a': one, 'c': one}), Vec(D, {'b': one})]
    >>> len(GF2_span(D, L))
    4
    >>> Vec(D, {}) in GF2_span(D, L)
    True
    >>> Vec(D, {'b': one}) in GF2_span(D, L)
    True
    >>> Vec(D, {'a':one, 'c':one}) in GF2_span(D, L)
    True
    >>> Vec(D, {x:one for x in D}) in GF2_span(D, L)
    True
    '''

    """
    https://d396qusza40orc.cloudfront.net/matrix/slides%2FThe_Vector_Space_02_Span.pdf
    L is a Span
    """
    res = []

    product_of_linear_coeffs = product([0,one], repeat=len(L))

    for linear_coeffs in product_of_linear_coeffs:
        vec = Vec(D, {})
        for i in range(len(linear_coeffs)):
            vec = vec + linear_coeffs[i] * L[i]
        res.append(vec)

    print(res)

    return res


    """
    veclist = list()
    ix = 0
    for d in D:
        v = [one] * len(D)
        veclist.append(v)
        for i in range(ix):
            v[i] = 0
        ix += 1
    print(veclist)

    res = []
    for p in product([0,1], repeat=len(D)):
        vec = Vec(D, {})
        #print("======")
        for i in range(len(veclist)):
            f = dict(zip(D, veclist[i] * p[i]))
            #print(f)
            vec = vec + Vec(D, f)
            #print(vec)
        res.append(vec)

    print(res)

    return vec
    """

    """
    a = [one, one, one]
    b = [0,   one, one]
    c = [0,     0, one]

    D = {'a', 'b', 'c'}
    """

    """
    for i in [0, 1]:
        for j in [0, 1]:
            for k in [0, 1]:
                a_i = veclist[0] * i
                b_j = veclist[1] * j
                c_k = veclist[2] * k
                v_a = Vec(D, {'a' : a_i[0], 'b' : a_i[1], 'c' : a_i[2]}) if len(a_i) > 0 else Vec(D, {})
                v_b = Vec(D, {'a' : b_j[0], 'b' : b_j[1], 'c' : b_j[2]}) if len(b_j) > 0 else Vec(D, {})
                v_c = Vec(D, {'a' : c_k[0], 'b' : c_k[1], 'c' : c_k[2]}) if len(c_k) > 0 else Vec(D, {})
                v = v_a + v_b + v_c
                print(v)
    """

D = {'a', 'b', 'c'}
L = [Vec(D, {'a': one, 'c': one}), Vec(D, {'b': one})]
GF2_span(D, L)



## Problem 4
# Answer with a boolean, please.

is_it_a_vector_space_1 = ...
is_it_a_vector_space_2 = ...



## Problem 5
is_it_a_vector_space_3 = ...
is_it_a_vector_space_4 = ...


## Problem 6

is_it_a_vector_space_5 = ...
is_it_a_vector_space_6 = ...
