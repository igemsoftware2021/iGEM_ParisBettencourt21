### imports ###

from os import path
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.integrate import odeint
import random as rd



#########  implementation ###########


### functions



### culture parameters

OD = 2
volume = 10
strain = "TB43lambda"


### E.coli parameters

g = 0.4                     # growth and division rate
d = 0.04

e_max_size = 5               # limit size accepted
e_min_size = 0


### minicell parameters

m = 0.002
m_size = 2/5 


### initialisation

init_cell_nb = OD*0.8*volume*100000000
init_min_size = 1
init_max_size = 2

sizes = list(np.linspace(e_min_size,e_max_size,501))        # space of different cell sizes
sizes = [round(x,3) for x in sizes]

sizespan = (e_max_size-e_min_size)/len(sizes)               # precision regarding to the size

tmax = 300                             # time of the simulation
time = np.linspace(0,tmax,1000)
tspan = tmax/len(time)                   

for x in sizes:                        # determine indices corresponding to the initial set limits
    if x <= init_min_size:
        init_min_index = sizes.index(x)
    if x <= init_max_size:
        init_max_index = sizes.index(x)
    else:
        break      

# splitting the initial population uniformly in the size space
init_cluster_size = init_cell_nb/(init_max_index-init_min_index)
init_clusters = list(np.zeros(len(sizes)))
init_clusters[init_min_index:init_max_index] = [init_cluster_size for i in range(init_max_index - init_min_index)]



culture = [init_clusters]                                # culture of bacteria clustered by size
m_count = [[0 for i in range(len(init_clusters))]]       # minicells inside the culture clustered by mother's size



''' We considere the growth fragementation problem with:
        G(x)=gx
        D(x)=dx

    We add a newfeature which is minicell production: 
        M(x)=mx

    The solution of the resulting ODE is approximated using Euler explicite method'''


### simulation


for t in time[1:]:
    new_clusters = culture[-1].copy()
    new_m_clusters = m_count[-1].copy()
    for i in range(len(new_clusters)):

        # The ODE
        dndt = 0 - d*sizes[i]*new_clusters[i] - g*sizes[i]*new_clusters[i] - m*sizes[i]*new_clusters[i]
        new_m_clusters[i] = new_m_clusters[i] + m*sizes[i]*new_clusters[i]*tspan   

        # The division of larger cells
        if sizes[i]*2 <= sizes[-1]:               
            dndt = dndt + 4*d*new_clusters[2*i]*sizes[2*i]

        # The growth of smaller cells
        if sizes[i]/(1+g) >= sizes[0]:
            x = round(sizes[i]/(1+g),2)
            j = sizes.index(x)
            dndt = dndt + g*x*new_clusters[j]

        # The production of minicells by larger cells
        if sizes[i]+m_size <= sizes[-1]:
            x = round(sizes[i]+m_size,3)
            j = sizes.index(x)
            dndt = dndt + m*x*new_clusters[j]

        # Euler method
        new_clusters[i] = new_clusters[i] + dndt*tspan

    culture.append(new_clusters)
    m_count.append(new_m_clusters)



culture = np.array(culture)      # [[culture 0],[culture 1]....[culture t-max]]   shape: M(300 lines, 500 columns)
m_count = np.array(m_count)      # [[count 0],[count 1]....[count t-max]]   shape: M(300 lines, 500 columns)

print(np.shape(culture))

df_culture = pd.DataFrame(data=culture, index=time, columns=sizes)
df_m_count = pd.DataFrame(data=m_count, index=time, columns=sizes)

df_culture.to_csv("culture.csv")
df_m_count.to_csv("m_count.csv")



### graphics

totals = [] 
for i in range(len(time)):
    total_e_m = [0,0]
    for x in culture[i]:
        total_e_m[0] = total_e_m[0] + x
    for y in m_count[i]:
        total_e_m[1] = total_e_m[1] + y 
    totals.append(total_e_m)                # [[tt e, tt m], .... , [tt e, tt m]]   shape: (lines 300, col 2)

#counts over time
plt.figure()
plt.plot(time,[x[0] for x in totals],label='total bacteria')
plt.plot(time,[x[1] for x in totals], label='total minicells')
plt.yscale('log')
plt.legend()
plt.xlabel('time (min)')
plt.ylabel('log(count)')
plt.show()
plt.close

# counts over size c
plt.figure()
plt.plot(sizes,culture[-1], label='cell count')
plt.legend()
plt.xlabel('size')
plt.ylabel('count')
plt.show()
plt.close()

# counts over size
plt.figure()
plt.plot(sizes,m_count[-1], label='minicell count', color='orange')
plt.legend()
plt.xlabel('size')
plt.ylabel('count')
plt.show()
plt.close()

# ratio
plt.figure()
plt.plot(time,[x[1]/x[0] for x in totals], label='ratio minicells/mothercells')
plt.legend()
plt.xlabel('time')
plt.ylabel('count')
plt.show()
plt.close()
