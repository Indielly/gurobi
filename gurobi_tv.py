import gurobipy as gp
from gurobipy import GRB

#criando novo modelo
m = gp.Model("rede de televisao")

# criando variaveis
x1 = m.addVar(vtype=GRB.INTEGER, name="x1")
x2 = m.addVar(vtype=GRB.INTEGER, name="x2")

# funcao objetivo
m.setObjective( 30000*x1 + 10000*x2, GRB.MAXIMIZE)

# adicionando restricoes
m.addConstr(20*x1 + 10*x2 <= 80, "R1")
m.addConstr(x1 + x2 >= 5, "R2")

# Otimizando modelo
m.optimize()

for v in m.getVars():
    print('%s %g' % (v.varName, v.x))

print('Obj: %g' % m.objVal)