# I hope to dig in time constraint issue using cplex

from docplex.mp.model import Model
# The wait time is really biggest trouble that blocks my way to dig in time constraint issue

 # You know, d[i] defines visiting order
distance =  [[0,2,3,0,0,0],
             [0,0,4,5,4,0],
             [0,2,0,6,2,0],
             [0,0,6,0,3,4],
             [0,2,0,9,0,7],
             [0,0,0,0,0,0]]
timeInfor = [[0,30],
             [6,14],
             [12,17],
             [11,21],
             [12,22],
             [0,30]]
N = 6
nodes = [(j) for j in range(N)]
arcs = [(i,j) for i in nodes for j in nodes if i != j]
mdl = Model('Dual_ride')
x = mdl.binary_var_dict(arcs, name = 'x')
d = mdl.continuous_var_dict(nodes, name = 'd')
mdl.minimize(mdl.sum( (x[(i,j)] * distance[i][j]) for i,j in arcs )) #objective funtion
for i,j in arcs:
    mdl.add_indicator(x[(i,j)], d[i] + 1 == d[j], name = 'visiting order')
# I will inversely get index of d variable
solution1 = mdl.solve(log_output = True)
k = []
for i in range(1, 6):
    for j in range(1, i):
        if d[j].solution_value == i:
            k.append(j)
# use k to store index of d variable , which d variable recordes visiting order
# After this, k list the visiting nodes in order
# starting node 0 is treated seperately
mdl.add_constraint(x[(0, k[1])]*distance[0, k[1]]<= timeInfor[k[1]][1])
# after 0, use loop to add constraints
for i in range(1,6):
    sum = 0
    for j in range(i):
        sum = sum + x( k[j-1],k[j] )*distance[ (k[j-1]) ][ (k[j]) ]
    mdl.add_constraint(sum <= timeInfor[ k[i] ][1])
# Maybe I should take a test now? No, it is not time.
solution2 = mdl.solve(log_output = True)

# TypeError: list indices must be integers or slices, not tuple.
