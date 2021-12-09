# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 15:38:16 2021

@author: jean-pierre.julien
"""

#	programme dynmol
from math import *
import matplotlib
import matplotlib.pyplot as plt
plt.style.use('dark_background')


#calcul de l'accélération

def computea(x,y): #Calcul des dérivées du potentiel
    ax=-x-2.0*y**2*x #accel x
    ay=-y-2.0*x**2*y #accel y
    return ax,ay

ax,ay=computea(1.0,2.0)
print(ax,ay,"coucou")

#calcul de l'énergie potentielle au point x,y
def vpot(x,y):
	vpot=0.5*((x**2)+(y**2))+(x**2)*(y**2)
	return vpot

# Input
print("Tau,Nsteps?")
tau=input("tau=")
tau=float(tau)
nsteps=input("nsteps=")
nsteps=int(nsteps)
print("x0 y0 vx0 vy0")
xold,yold,vxold,vyold=input("x0 y0 vx0 vy0").split()
xold=float(xold)
yold=float(yold)
vxold=float(vxold)
vyold=float(vyold)
Lx=[xold]
Ly=[yold]

# Calcul de l'energie initiale (cinétique+potentielle)
e0=0.5*((vxold**2)+(vyold**2))+vpot(xold,yold)
print("Energie initiale=",e0)
e_init = e0

# Calcul de l'accélération initiale:
axold,ayold=computea(xold,yold)

# Construction itérative de la trajectoire:
for k in range(1,nsteps,1):
    #print("k=",k)
    xnew=xold+tau*vxold+0.5*tau**2*axold
    ynew=yold+tau*vyold+0.5*tau**2*ayold
    #print("xnew=",xnew,"ynew=",ynew)
    axnew,aynew=computea(xnew,ynew)
    vxnew=vxold+0.5*tau*(axold+axnew)
    vynew=vyold+0.5*tau*(ayold+aynew)
    e0=0.5*(vxnew**2+vynew**2)+vpot(xnew,ynew)
    #print("t ,  x, y energie")
    #print(float(k)*tau,xnew,ynew,e0)
    xold=xnew
    yold=ynew
    vxold=vxnew
    vyold=vynew
    axold=axnew
    ayold=aynew
    Lx.append(xold)
    Ly.append(yold)
#	xold,yold doit etre écrit dans un fichier python
    
print("Energie finale=",e0)    
e_final = e0

delta_e = e_final - e_init

print("Variation d'énergie", delta_e)

plt.plot(Lx,Ly)
plt.grid()
plt.savefig('trajectoire.png') # sauvegarde fichier image au format png
plt.show()	

print("Simulation terminee")
	
