from pulp import *


def q3():
    p = LpProblem('Question 3', LpMaximize)
    yr=LpVariable('yr')
    yg=LpVariable('yg')
    yb=LpVariable('yb')
    yk=LpVariable('yk')
    mr=LpVariable('mr')
    mg=LpVariable('mg')
    mb=LpVariable('mb')
    mk=LpVariable('mk')
    cr=LpVariable('cr')
    cg=LpVariable('cg')
    cb=LpVariable('cb')
    ck=LpVariable('ck')
    r=LpVariable('red')
    g=LpVariable('green')
    b=LpVariable('blue')
    k=LpVariable('black')

    p += 10*r + 15*g + 25*b + 25*k, 'Objective func'
    p += yr + mr == r, 'Red req'
    p += yg + cg == g, 'Green req'
    p += mb + cb == b, 'Blue req'
    p += yk + mk + ck == k, 'Black req'
    p += yr + yg + yb + yk <= 10, 'Yellow req'
    p += mr + mg + mb + mk <= 5, 'Magenta req'
    p += cr + cg + cb + ck <= 11, 'Cyan req'


    p.writeLP('q3.lp')
    p.solve()
    for v in p.variables():
        print(v.name, "=", v.varValue)


def q4a():
    p = LpProblem('Question 4a', LpMaximize)
    A = LpVariable('A', 0, 1, LpInteger)
    B = LpVariable('B', 0, 1, LpInteger)
    C = LpVariable('C', 0, 1, LpInteger)
    D = LpVariable('D', 0, 1, LpInteger)
    E = LpVariable('E', 0, 1, LpInteger)
    F = LpVariable('F', 0, 1, LpInteger)

    p += 60*A + 70*B + 40*C + 70*D + 17*E + 100*F, 'Objective func'
    p += 6*A + 7*B + 4*C + 9*D + 3*E + 8*F <= 20, 'main constraint'

    p.writeLP('q4a.lp')
    p.solve()
    for v in p.variables():
        print(v.name, "=", v.varValue)


def q4b():
    p = LpProblem('Question 4b', LpMaximize)
    A = LpVariable('A', 0, 1, LpInteger)
    B = LpVariable('B', 0, 1, LpInteger)
    C = LpVariable('C', 0, 1, LpInteger)
    D = LpVariable('D', 0, 1, LpInteger)
    E = LpVariable('E', 0, 1, LpInteger)
    F = LpVariable('F', 0, 1, LpInteger)

    p += 60*A + 70*B + 40*C + 70*D + 17*E + 100*F, 'Objective func'
    p += 6*A + 7*B + 4*C + 9*D + 3*E + 8*F <= 20, 'main constraint'
    p += D >= C, 'additional constraint'

    p.writeLP('q4b.lp')
    p.solve()
    for v in p.variables():
        print(v.name, "=", v.varValue)


def q4c():
    p = LpProblem('Question 4c', LpMaximize)
    A = LpVariable('A', 0, 1, LpInteger)
    B = LpVariable('B', 0, 1, LpInteger)
    C = LpVariable('C', 0, 1, LpInteger)
    D = LpVariable('D', 0, 1, LpInteger)
    E = LpVariable('E', 0, 1, LpInteger)
    F = LpVariable('F', 0, 1, LpInteger)
    O = LpVariable('O', 0, None, LpInteger)

    p += 60*A + 70*B + 40*C + 70*D + 17*E + 100*F -15*O, 'Objective func'
    #p += 6*A + 7*B + 4*C + 9*D + 3*E + 8*F <= 20, 'main constraint'
    p +=  6*A + 7*B + 4*C + 9*D + 3*E + 8*F - 20 - O == 0


    p.writeLP('q4c.lp')
    p.solve()
    for v in p.variables():
        print(v.name, "=", v.varValue)


if __name__ == '__main__':
    q4c()
