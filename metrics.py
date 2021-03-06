# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 13:03:24 2014

@author: Caner Turkmen

Own implementation of Non-Negative Matrix Factorization 
"""
import numpy as np
import sys

def frobenius(A, B):
    """
    Function for calculating the Euclidean distance / Frobenius norm between two matrices
    """
    return np.linalg.norm(A-B, 2)
    
def kldivergence(A,B):
    """
    Function for determining the divergence of A from B
    as presented in Lee and Seung, otherwise known as generalized Kullback-Leibler 
    divergence or I-divergence.
    
    :param A: first matrix
    :type A: numpy.ndarray
    :param B: second matrix
    :type B: numpy.ndarray
    
    :returns: the divergence
    :rtype: float
    """
    return np.sum((A*np.log(A/B) - A + B))



