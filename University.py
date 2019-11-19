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

N = 4
nodes = [i+1 for i in range(N)]
sets={(a,b,c,d) for a in nodes for b in nodes for c in nodes for d in nodes if a!=b and b!=c and c!=d}

//////SET
int c = ...;
range Customers = 1...c;
int v = ...;
range Vehicles = 1..v;
int n = ...;
range Nodes = 1..n;
int t = ...;
range Workdays = 1..t;
int d = ...;
range Drivers = 1..d;

//////PARAMETER
tuple timewindow{
int e;
int l;
}
int q[Nodes] =...;   //Demand at node i
timewindow tw[Customers] =...; //Time windows of customers
float pv[Vehicles] =...;
float p[Customers] =...;
float tvmax[Vehicles]=...;

int delivery[Customers][Workdays]=...;
int Q[Vehicles]=...;
float cost[Customers][Customers]=...;
float l[Customers]=...;
float s[Customers]=...;

int M = 100000;

//////VARIABLE
dvar boolean x[i in Customers][j in Customers][v in Vehicles];
dvar boolean y[d in Drivers][v in Vehicles];
dvar float+ r[d in Drivers][t in Workdays];
dvar float+ u[i in Nodes][v in Vehicles][t in Workdays];
dvar float+ T[i in Nodes];
dvar float+ TV[v in Vehicles];
dvar float+ b[i in Customers][v in Vehicles][t in Workdays];
dvar float+ dentaT[v in Vehicles];
dvar float+ dentae[i in Customers];
dvar float+ dental[i in Customers];
dvar float+ theta[j in Customers][v in Vehicles][t in Workdays];
dvar float+ o[j in Customers][v in Vehicles][t in Workdays];
dvar int+ D[Nodes];


execute CPX_PARAM{
    cplex.tilim = 120;
    cplex.nodefileind = 3;
}
minimize sum(j in Customers, v in Vehicles)(cost[0][j]*x[0][j][v]) + sum(i in Customers, j in Customers:j>i)(cost[i][j]) + \
pv[v]*dentaT[v in Vehicles]+sum(i in Nodes)(p[i]*(dentae[i]+dental[i]));
# I hope I can really solve time constraint problem today
subject to{
    ct01: forall(i in Customers)
          sum(j in Customers, v in Vehicles)(x[i][j][v]) == 1;
          forall(k in Customers, v in Vehicles)
          sum(i in Nodes)(x[i][k][v]) - sum(j in Nodes)(x[k][j][v]) == 0;
    ct02: forall(v in Vehicles)
          sum(i in Customers)(q[i])*sum(j in Nodes)(x[k][j][v])<=Q[v];
    ct03: forall(i in Nodes, j in Nodes:j!=i)
          b[i][v][t] + M*(1-y[i][v]) <= b[j][v][t];
    ct04: forall(i in Nodes, j in Customers)
          b[i][v][t] + M*(1-y[d][v]) >= tw[j].e;
          forall(i in Nodes, j in Customers)
          b[i][v][t] - M*(1-y[d][v]) <= tw[j].l;
    ct05: forall(v in Vehicles)
          dentaT[v] >= TV[v] - tvmax[v];
    ct06: forall(i in Nodes, j in Nodes:i!=j)
          D[j] >= D[i] + delivery[c][t] - Q[v]*(1-x[i][j][v]);
          forall(i in Nodes)
          delivery[c][t] <= D[i] <=Q[v];
    ct07: forall(i in Nodes, j in Customers)
          dentae[i] >= tw[j].e - T[i];
    ct08: forall(i in Nodes, j in Customers)
          dental[i] >= T[i] - tw[j].l;
    ct09: forall(v in Vehicles)
          sum(j in Nodes:j>0)(x[0][j][v]) == 1;
          forall(v in Vehicles)
          sum(i in Nodes: i>n+1)(x[i][n+1][v]) == 1;
    ct10: forall(d in Drivers, v in Vehicles, t in Workdays, i in Customers)
          r[d][t] >= u[n+1][v][t] - tw[i].e - M*(1-y[d][v]);
}


solution = mdl.solve(log_output = True)
