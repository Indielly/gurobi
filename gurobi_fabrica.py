import gurobipy as gp
from gurobipy import GRB

#criando novo modelo
m = gp.Model("fabrica")

# criando variaveis
x1 = m.addVar(vtype=GRB.INTEGER, name="x1")
x2 = m.addVar(vtype=GRB.INTEGER, name="x2")

# funcao objetivo
m.setObjective( 100*x1 + 150*x2, GRB.MAXIMIZE)

# adicionando restricoes
m.addConstr(2*x1 + 3*x2 <= 120, "R1")
m.addConstr(x1 <= 40, "R2")
m.addConstr(x2 <= 30, "R3")

# Otimizando modelo
m.optimize()

for v in m.getVars():
    print('%s %g' % (v.varName, v.x))

print('Obj: %g' % m.objVal)