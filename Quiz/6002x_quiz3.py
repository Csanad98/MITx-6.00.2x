#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 16:09:43 2018

@author: macintosh
"""
def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    answer = "no solution"
    multipSum = 0 #sum of multiplier numbers
    multipList = []
    currentSum = 0
    
    for numL in L:
        multip = 0 #multiplying number
        while True:
            if (((multip+1) * numL)+ currentSum) > s:
                multipSum +=multip
                multipList.append(multip)
                currentSum += (numL * multip)
                break
            else:
                multip +=1
    product = 0
    for i in range(len(L)):
        product += (multipList[i]*L[i])
    if product == s:
        return multipSum
        
    else:
        return answer
   
    
    
    
    
    
    
    
    
print(greedySum([10, 5, 1], 14))