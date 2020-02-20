from pulp import *


p = LpProblem('q3', LpMaximize)
yr=LpVariable('yr', 0)
yg=LpVariable('yg', 0)
yb=LpVariable('yb', 0)
yk=LpVariable('yk', 0)
mr=LpVariable('mr', 0)
mg=LpVariable('mg', 0)
mb=LpVariable('mb', 0)
mk=LpVariable('mk', 0)
cr=LpVariable('cr', 0)
cg=LpVariable('cg', 0)
cb=LpVariable('cb', 0)
ck=LpVariable('ck', 0)
r=LpVariable('red', 0)
g=LpVariable('green', 0)
b=LpVariable('blue', 0)
k=LpVariable('black', 0)

p += 10*r + 15*g + 25*b + 25*k, 'objective_function'
p += yr + mr == r, 'red_req'
p += yr == mr
p += yg + cg == g, 'green_req'
p += yg == cg
p += mb + cb == b, 'blue_req'
p += mb == cb
p += yk + mk + ck == k, 'black_req'
p += yk == mk
p += yk == ck
p += ck == mk
p += yr + yg + yb + yk <= 10, 'yellow_req'
p += mr + mg + mb + mk <= 5, 'magenta_req'
p += cr + cg + cb + ck <= 11, 'cyan_req'


p.solve()
for v in p.variables():
    print(v.name, "=", v.varValue)