import gurobipy as gp
from gurobipy import GRB

#criando novo modelo
m = gp.Model("cintos")

# criando variaveis
x1 = m.addVar(vtype=GRB.INTEGER, name="x1")
x2 = m.addVar(vtype=GRB.INTEGER, name="x2")

# funcao objetivo
m.setObjective( 4*x1 + 3*x2, GRB.MAXIMIZE)

# adicionando restricoes
m.addConstr(2*x1 + x2 <= 1000, "R1")
m.addConstr(x1 + x2 <= 800, "R2")
m.addConstr(x1 <= 400, "R3")
m.addConstr(x2 <= 700, "R4")

# Otimizando modelo
m.optimize()

for v in m.getVars():
    print('%s %g' % (v.varName, v.x))

print('Obj: %g' % m.objVal)