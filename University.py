# I hope really solve time constraint and get answer today

from docplex.mp.model import Model
import math

timeInfor = [[0,30],
             [6,14],
             [12,17],
             [11,21],
             [12,22],
             [0,30]]

mdl = Model('Dual_ride')
x = mdl.binary_var_dict(arcos, name = 'x') # decision variables, whether the arc between two nodes is pircked or not


sets= [0,2,4] # for example

arrival_time = start_time_previous + distance[i][j]
start_time_previous = max(arrival_time_previous, timeInfor[i][0])

time = 

for i in cnodes:
    mdl.add_constraint( arrival_time[i] <= timeInfor[i][1], name='upper bound constraint')



solution = mdl.solve(log_output = True)
