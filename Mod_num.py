from scipy import *
from cmath import *
import matplotlib 
import matplotlib.pyplot as plt
from numpy import *

#Création des objets et paramètres
t = 1.0  #énergie de saut
e0=0.0 #énergie de site
eps = 0.00001  #élement infinitésimal
L=50
psimoins = zeros((2*L+1, 2*L+1));  #tableau indicé de 0 à 2L compris
psiplus = zeros((2*L+1, 2*L+1));  #tableau indicé de 0 à 2L compris
listea = zeros(L+1);  #tableau indicé de 0 à L compris
listeb = zeros(L+1);  #tableau indicé de 0 à L compris

#Initialisation
psimoins[L][L] = 1.0;  #psi 0
psiplus[L][L] = 0.0;
a = 0.0;  #a0
b = 0.0;  #b1
listea[0] = a; #rentre le a0 dans la liste
listeb[0] = b; #rentre le b0 dans la liste


########################################

#Calculs des coefs
for n in range(1,L):#parcours les nombres de 1 à L-1 compris
        aplus=0  #remet à zero la variable locale
        for i in range(L-n,L+n+1) :#application du Hamiltonien
            for j in range(L-n,L+n+1) :#application du Hamiltonien
                a=a+t*psimoins[i][j] *(psimoins[i-1][j] + psimoins[i+1][j] + psimoins[i][j-1]+psimoins[i][j+1])
        bplus = 0
        for i in range(L-n,L+n+1) :#application du Hamiltonien à psi_n
            for j in range(L-n,L+n+1):
                bplus = bplus + (t*(psimoins[i-1][j] + psimoins[i+1][j] + psimoins[i][j-1] + psimoins[i][j+1]))
        bplus = bplus **(1/2)
        
        for i in range(L-n,L+n+1) :  #parcours les nombres de L-n à L+n compris
            for j in range(L-n,L+n+1):
                psiplus[i][j] = (1/bplus)*(t*(psimoins[i-1][j] + psimoins[i+1][j] + psimoins[i][j-1] + psimoins[i][j+1]))
                
        temp = psiplus  #pour inverser psiplus et psimoins
        psiplus = psimoins  #pour inverser psiplus et psimoins
        psimoins = temp  #pour inverser psiplus et psimoins
        b = bplus
    
        listea[n] = a  #modifie la liste petit à petit
        listeb[n] = b

      
#Calculs des coefs infinis
ainf = 0.0
binf = 0.0        
for k in range(L-10,L):  #parcours les nombres de L-10 à L-1 compris
    ainf = ainf + listea[k]
    binf = binf + listeb[k]
ainf = ainf/10
binf = binf/10
listea[L] = ainf
listeb[L] = binf
print("a=",listea)
print("b=",listeb)


#Calcul de la densité sous forme de fonction        
def densite(E):
    G = (E - ainf -1j*sqrt(-(E - ainf)**2 + 4*binf**2))/(2*binf**2)  #calcul de Ginfini
    for i in range(L,0,-1): #parcours les nombres de L à 0 compris
        print("in densité i=",i,"b=",listeb[i])
        G = 1/(E - listea[i] - G*listeb[i]**2)  #calcul de la fraction continue
    nmu = abs((1/pi)*G.imag)  #calcul de la densite en prenant la valeur absolue
    return nmu

energy = arange(ainf - 2*binf,ainf + 2*binf, 0.01)  #découpe des valeurs d'énergie      
dos = densite(energy)       
plt.plot(energy,dos) 
plt.grid()
plt.show() # trace le graphique