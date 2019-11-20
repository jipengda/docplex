# I hope to dig in time constraint issue using cplex

from docplex.mp.modle import Model
import math

# The wait time is really biggest trouble that blocks my way to dig in time constraint issue

 # You know, d[i] defines visiting order

N = 5
nodes = 
for i,j in arcs:
    mdl.add_indicator(x[(i,j)], d[i] + 1 == d[j], name = 'visiting order')

N = 5

k = []

# I will inversely get index of d variable
for i in range(1, 6):
    for j in range(1,6):
        if d[j] == i:
            k.append(j)
# use k to store index of d variable , which d variable recordes visiting order
# After this, k list the visiting nodes in order

for i in range(1,6)
    x[(k[i]
# starting node 0 is treated seperately
mdl.add_constraint(x[(0, k[1])]*distance[0, k[1]]<= timeInfor[k[1]][1])

sum = 0
# after 0, use loop to add constraints
for i in range(1,6):
    sum = 0
    for j in range(i):
        sum = sum + x( k[j-1],k[j] )*distance[ (k[j-1]) ][ (k[j]) ]
    mdl.add_constraint(sum <= timeInfor[ k[i] ][1])
# Maybe I should take a test now? No, it is not time.
