from pulp import *


p = LpProblem('q4c', LpMaximize)
A = LpVariable('A', 0, 1, LpInteger)
B = LpVariable('B', 0, 1, LpInteger)
C = LpVariable('C', 0, 1, LpInteger)
D = LpVariable('D', 0, 1, LpInteger)
E = LpVariable('E', 0, 1, LpInteger)
F = LpVariable('F', 0, 1, LpInteger)
X = LpVariable('X', 0, None, LpInteger)

p += 60*A + 70*B + 40*C + 70*D + 17*E + 100*F -15*X, 'objective_function'
p +=  6*A + 7*B + 4*C + 9*D + 3*E + 8*F - 20 - X == 0, 'modified_constraint'


p.solve()
for v in p.variables():
    print(v.name, "=", v.varValue)