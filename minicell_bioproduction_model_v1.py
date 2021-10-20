### imports ###

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.integrate import odeint
import random as rd


### parameters ###

### E.coli parameters
growing_rate = 0.04
e_max_size = 2
e_min_size = 1

### minicell parameters
minicell_production_rate = 0
m_max_size = 1/5 * e_max_size
m_min_size = 1/5 * e_min_size




#########  implementation ###########


### initialisation
cell_count = [1]
minicell_count = []
tmax = 300
time = np.linspace(0,tmax,1000)
tspan = tmax/len(time)
counts = []   # [[[]=cell_count,[]=minicell_count]=t0 , []=cell_count,[]=minicell_count]=t1 , ...]
div = []
mini = []

''' a) exponential growth, constant minicells production'''

minicell_production_rate = 0.03

### functions ###

def minicell_production(cell,t,tspan):
    minicell = 0
    if cell > e_min_size + m_max_size:
        if ((t-tspan)*minicell_production_rate)%1 > (t*minicell_production_rate)%1 :
            minicell = m_max_size
        cell = cell - minicell
    return cell, minicell

### simulation
for t in time:
    for i in range(len(cell_count)):
        cell_count[i] = round(cell_count[i] + cell_count[i]*growing_rate*tspan,5)
        cell_count[i], minicell  = minicell_production(cell_count[i],t,tspan)
        if minicell > 0:
            minicell_count.append(minicell)
            mini.append(t)
        if cell_count[i] >= 2:
            div.append(t)
            cell_count[i] = cell_count[i]/2
            new_cell = cell_count[i]
            cell_count.append(new_cell)
    counts.append([cell_count.copy(),minicell_count.copy()])


### plot


plt.figure()
prev = 0
col = 0
for i in range(len(counts)):
    if prev < len(counts[i][0]):
        style = ["-","--","-."]
        prev = len(counts[i][0])
        life = time[i:]
        plt.plot(life, [l[0][col] for l in counts[i:]], style[col%3], label='cell'+str(prev))
        col = col + 1
for t in div:
    plt.axvline(x=t, color='lightgrey', linestyle=':')

for t in mini:
    plt.axvline(x=t, color='darkgrey', linestyle='--')

plt.ylim([1,2.5])
plt.xlabel("time (m)")
plt.ylabel("size of the bacteria (micron)")
plt.legend()
plt.show()
plt.close()


## counts

final_population = counts[-1]

print("cellule=", len(final_population[0]),"   minicellule=", len(final_population[1]))

plt.figure()
plt.plot(time,[len(x[0]) for x in counts], label='n of cells')
plt.plot(time,[len(x[1]) for x in counts], label='n of minicells')
plt.legend()
plt.show()
plt.close()




''' b) exponential growth, exponential minicell production'''

minicell_production_rate = 0.02
rate_sum = 0

### functions ###

def minicell_production(cell,t,tspan,rate_sum):
    minicell = 0
    if cell > e_min_size + m_max_size:
        if (rate_sum - (minicell_production_rate*cell*tspan))%1 > rate_sum%1 :
            minicell = m_max_size
        cell = cell - minicell
    return cell, minicell

### simulation
for t in time:
    for i in range(len(cell_count)):
        cell_count[i] = round(cell_count[i] + cell_count[i]*growing_rate*tspan,5)
        if i == 0:
            rate_sum = rate_sum + (minicell_production_rate*cell_count[i]*tspan)
        cell_count[i], minicell  = minicell_production(cell_count[i],t,tspan,rate_sum)
        if minicell > 0:
            minicell_count.append(minicell)
            mini.append(t)
        if cell_count[i] >= 2:
            div.append(t)
            cell_count[i] = cell_count[i]/2
            new_cell = cell_count[i]
            cell_count.append(new_cell)
    counts.append([cell_count.copy(),minicell_count.copy()])


### plot


plt.figure()
prev = 0
col = 0
for i in range(len(counts)):
    if prev < len(counts[i][0]):
        style = ["-","--","-."]
        prev = len(counts[i][0])
        life = time[i:]
        plt.plot(life, [l[0][col] for l in counts[i:]], style[col%3], label='cell'+str(prev))
        col = col + 1
for t in div:
    plt.axvline(x=t, color='lightgrey', linestyle=':')

for t in mini:
    plt.axvline(x=t, color='darkgrey', linestyle='--')

plt.legend()
plt.ylim([1,2.5])
plt.xlabel("time (m)")
plt.ylabel("size of the bacteria (micron)")
plt.show()
plt.close()


### counts

final_population = counts[-1]

print("cellule=", len(final_population[0]),"   minicellule=", len(final_population[1]))


plt.figure()
plt.plot(time,[len(x[0]) for x in counts], label='n of cells')
plt.plot(time,[len(x[1]) for x in counts], label='n of minicells')
plt.legend()
plt.show()
plt.close()


''' c) exponential growth, constant minicells '''

minicell_production_rate = 0.03

### functions ###

def minicell_production(cell,tspan):
    minicell = 0
    if cell > e_min_size + m_max_size:
        threshold = minicell_production_rate*tspan*10000
        random = rd.randint(1,10000)
        if random <= threshold:
            minicell = m_max_size
        cell = cell - minicell
    return cell, minicell

### simulation
for t in time:
    for i in range(len(cell_count)):
        cell_count[i] = round(cell_count[i] + cell_count[i]*growing_rate*tspan,5)
        cell_count[i], minicell  = minicell_production(cell_count[i],tspan)
        if minicell > 0:
            minicell_count.append(minicell)
            mini.append(t)
        if cell_count[i] >= 2:
            div.append(t)
            cell_count[i] = cell_count[i]/2
            new_cell = cell_count[i]
            cell_count.append(new_cell)
    counts.append([cell_count.copy(),minicell_count.copy()])


### plot


plt.figure()
prev = 0
col = 0
for i in range(len(counts)):
    if prev < len(counts[i][0]):
        style = ["-","--","-."]
        prev = len(counts[i][0])
        life = time[i:]
        plt.plot(life, [l[0][col] for l in counts[i:]], style[col%3], label='cell'+str(prev))
        col = col + 1
for t in div:
    plt.axvline(x=t, color='lightgrey', linestyle=':')

for t in mini:
    plt.axvline(x=t, color='darkgrey', linestyle='--')

plt.ylim([1,2.5])
plt.xlabel("time (m)")
plt.ylabel("size of the bacteria (micron)")
plt.legend()
plt.show()
plt.close()


## counts

final_population = counts[-1]

print("cellule=", len(final_population[0]),"   minicellule=", len(final_population[1]))


plt.figure()
plt.plot(time,[len(x[0]) for x in counts], label='n of cells')
plt.plot(time,[len(x[1]) for x in counts], label='n of minicells')
plt.yscale('log')
plt.legend()
plt.show()
plt.close()



''' d) exponential growth, constant minicells '''

minicell_production_rate = 0.02

### functions ###

def minicell_production(cell,tspan):
    minicell = 0
    if cell > e_min_size + m_max_size:
        threshold = minicell_production_rate*tspan*10000*cell
        random = rd.randint(1,10000)
        if random <= threshold:
            minicell = m_max_size
        cell = cell - minicell
    return cell, minicell

### simulation
for t in time:
    for i in range(len(cell_count)):
        cell_count[i] = round(cell_count[i] + cell_count[i]*growing_rate*tspan,5)
        cell_count[i], minicell  = minicell_production(cell_count[i],tspan)
        if minicell > 0:
            minicell_count.append(minicell)
            mini.append(t)
        if cell_count[i] >= 2:
            div.append(t)
            cell_count[i] = cell_count[i]/2
            new_cell = cell_count[i]
            cell_count.append(new_cell)
    counts.append([cell_count.copy(),minicell_count.copy()])


### plot


plt.figure()
prev = 0
col = 0
for i in range(len(counts)):
    if prev < len(counts[i][0]):
        style = ["-","--","-."]
        prev = len(counts[i][0])
        life = time[i:]
        plt.plot(life, [l[0][col] for l in counts[i:]], style[col%3], label='cell'+str(prev))
        col = col + 1
for t in div:
    plt.axvline(x=t, color='lightgrey', linestyle=':')

for t in mini:
    plt.axvline(x=t, color='darkgrey', linestyle='--')

plt.ylim([1,2.5])
plt.xlabel("time (m)")
plt.ylabel("size of the bacteria (micron)")
plt.legend()
plt.show()
plt.close()


### counts

final_population = counts[-1]

print("cellule=", len(final_population[0]),"   minicellule=", len(final_population[1]))


plt.figure()
plt.plot(time,[len(x[0]) for x in counts], label='n of cells')
plt.plot(time,[len(x[1]) for x in counts], label='n of minicells')
plt.yscale('log')
plt.legend()
plt.show()
plt.close()
