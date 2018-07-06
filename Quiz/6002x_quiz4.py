#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 17:07:32 2018

@author: macintosh
"""

def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    maxSum = 0
    for n in L:
        if n > maxSum:
            maxSum = n
    for num in range(len(L)):
        for i in range(len(L)):
            start = i
            if (i+num) < (len(L)-1):
                end = i+num+2
                currentSum = 0
                for e in L[start:end]: 
                    currentSum +=e

                
                if currentSum > maxSum:
                    maxSum = currentSum
                    
    return maxSum




print(max_contig_sum([-2, 6, 8, 10]))   