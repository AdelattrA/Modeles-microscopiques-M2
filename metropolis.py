# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 13:15:49 2021

@author: jean-pierre.julien
"""


# programme Metropolis
from math import *
from random import *
import matplotlib
import matplotlib.pyplot as plt
def proba(x):
    proba=(exp(-x**2))/sqrt(pi)
    return proba
def f(x,g):
    f=exp(-g*x**4)
    return f
print("pi=",pi)
#  Input 
delta,nsteps,g=input("delta,nsteps,g").split()
delta=float(delta)
nsteps=int(nsteps)
g=float(g)
# Configuration initiale tiree au sort
# uniform(0,1) génère un nombre aléatoire uniformément réparti entre 0 et 1 
xrand=uniform(0,1)
xold=xrand-0.5     
# Initialisation des accumulateurs
valint=0.   
naccep=0  
#  Generation  des  configurations  successives 
for k in range(1,nsteps,1):
    xrand=uniform(0,1)
    xnew=xold+(xrand-0.5)*delta
    ratio=proba(xnew)/proba(xold)
    xrand2=uniform(0,1)
    if (ratio >= xrand2):
        naccep=naccep+1
    else:
        xnew=xold
    valint=valint+f(xnew,g)  
    xold=xnew
valint=valint/float(nsteps)
print('integrale=',valint)
tauxaccep=float(naccep)/float(nsteps)
print('taux acceptation=',tauxaccep)
print("Simulation terminee")
