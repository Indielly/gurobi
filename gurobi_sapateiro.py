import gurobipy as gp # importando o gurobi gurobipy definindo gp
from gurobipy import GRB # do gurobipy vai importar a classe grb que vamos usar para resolver os problemas

#criando novo modelo
m = gp.Model("sapateiro") # criando variavel de modelo

# criando variaveis
x1 = m.addVar(vtype=GRB.INTEGER, name="sapato")
x2 = m.addVar(vtype=GRB.INTEGER, name="cinto")

# funcao objetivo
m.setObjective( 5*x1 + 2*x2, GRB.MAXIMIZE)

# adicionando restricoes
m.addConstr(2*x1 + 1*x2 <= 6, "R1")
m.addConstr(10*x1 + 12*x2 <= 60, "R2")

# Otimizando modelo
m.optimize() # chama variavel modelo . optimize

for v in m.getVars():
    print('%s %g' % (v.varName, v.x))

print('Obj: %g' % m.objVal)