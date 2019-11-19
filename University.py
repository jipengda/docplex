# I hope really solve time constraint and get answer today

from docplex.mp.model import Model
import math

timeInfor = [[0,30],
             [6,14],
             [12,17],
             [11,21],
             [12,22],
             [0,30]]
N = 6
nodes = [i for i in range(N)]
arcs = [(i,j) for i in nodes for j in nodes if i!=j]

mdl = Model('Dual_ride')
x = mdl.binary_var_dict(arcs, name = 'x') # decision variables, whether the arc between two nodes is picked or not
d = mdl.continuous_var_dict(nodes, name = 'd') # d is a variable recording visiting order

sets= [0,2,4] # for example

arrival_time = start_time_previous + distance[i][j]
start_time_previous = max(arrival_time_previous, timeInfor[i][0])

time =

for i in cnodes:
    mdl.add_constraint( arrival_time[i] <= timeInfor[i][1], name='upper bound constraint')

# However, arrival_time depends on visiting order of nodes , how should I deal with that ?
# I can use d to deal with that. d is a variable recording visiting order

for i,j in arcs:
    mdl.add_indicator(x[(i,j)], d[i] + 1 == d[j], name = 'visiting order')

# So now d is fixed. Then how about next step?
# Take advantage of d, add time window constraint

x[(0,1)]distance[0][1]<=timeInfor[1][1]
x[(0,2)]*distance[0][2]<=timeInfor[2][1]

#[0,1,2]
 max( x[(0,1)]*distance[0][1], timeInfor[1][1] ) + x[ (1,2) ] * distance[1][2] <= timeInfor[2][1]

#[0,2,4]
 max( x[(0,2)]*distance[0][2], timeInfor[2][1] ) + x[ (2,4) ] * distance[2][4] <= timeInfor[4][1]

#[0,1,5]
 max( x[(0,1)]*distance[0][1], timeInfor[1][1] ) + x[ (1,5) ] * distance[1][5] <= timeInfor[5][1]

#[0,2,1,3,4,5]
 x[(0,2)]*distance[0][2] + x[(2,1)]*distance[2][1] + x[(1,3)]*distance[1][3]+x[(3,4)]*distance[3][4]+x[4,5]*distance[4][5]

for i in nodes:
    for j in nodes:
for i,j in arcs:
    x[(i,j)]*distance[i][j] <= timeInfor[i][1]

# States that a vehicle cannot start the service at the assigned node i before the earliest time ei
 ct07: forall(i in Nodes, j in Customers)
        dentae[i] >= tw[j].e - T[i];
# [0,1]
 x[0,1] * distance[0][1] <= timeInfor[1][1]
# [0,2]
 x[0,2] * distance[0][2] <= timeInfor[2][1]
# [0,1,2]
 x[0,1] * distance[0][1] + x[1,2] * distance[1][2] <= timeInfor[2][1]
# The reason this path [0,1,2] is valid because it matches time window constraint
 x[0,1] * distance[0][1] + x[1,2] * distance[1][2] <= timeInfor[2][1]
# The reason this path [0,1,2,4] is valid or invalid depends on whether it matches time window constraint or not
 x[0,1] * distance[0][1] + x[1,2] * distance[1][2] + x[2,4] * distance[2][4] <= timeInfor[4][1]
# The reason this path [0,2,1,3,4,5] is valid or invalid depends on whether it matches time window constraint or not
 x[0,2] * distance[0][2] + x[(2,1)] * distance[2][1] + x[(1,3)] * distance[1][3] + x[(3,4)] * distance[3][4] + x[(4,5)] * distance[4][5] <= timeInfor[5][1]

# The reason this path [0,1,3,2,4,5] is valid or invalid depends on whether it matches time window constraint or not
x[0,1] * distance[0][1] + x[(1,3)] * distance[1][3] + x[(3,2)] * distance[3][2] + x[(2,4)] * distance[2][4] + x[(4,5)] * distance[4][5] <= timeInfor[5][1]



solution = mdl.solve(log_output = True)
