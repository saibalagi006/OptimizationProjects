# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 15:39:57 2020

@author: balag
"""

#######Simle production problem
from docplex.mp.model import Model

m = Model(name="telephone production")
desk = m.continuous_var(name="desk")
cell = m.continuous_var(name="cell")


##Write constraints
m.add_constraint(desk>=100)
m.add_constraint(cell>=100)
m.add_constraint(0.2*desk+0.4*cell<=400)
m.add_constraint(0.5*desk+0.4*cell<=490)
m.maximize(12*desk+20*cell)
m.print_information()
m.solve()
m.print_solution()


opt_model = cpl.Model(NAME="MIP Model")


##############

from docplex.mp.model import Model
import os
import pandas as pd
path = "C:\\Users\\balag\\Desktop\\PythonProjects\\Optimization Projects"
os.chdir(path)
input_file = pd.read_excel("transportation101.xlsx")

#input_file.columns


no_supply =2
no_demand=3
set_I = range(1,no_supply+1)
set_J = range(1,no_demand+1)
a={}
a[1]=15
a[2]=20
b={}
b[1]=7
b[2]=10
b[3]=15


m=Model("Transportation_probem")
#m.con

c = {(i,j):1000 for i in set_I for j in set_J}

for i in range(len(input_file)):
    m = input_file.loc[i,"supply"]
    n = input_file.loc[i,'demand']
    p = input_file.loc[i,'cost']
    c[m,n]=p


m=Model("Transportation_probem")    
x_vars = {(i,j):m.continuous_var(name="x_{0}_{1}".format(i,j)) for i in set_I for j in set_J}

for i in set_I:
    m.add_constraint(ct = m.sum(x_vars[i,j] for j in set_J)<=a[i])

for j in set_J:
    m.add_constraint(ct = m.sum(x_vars[i,j] for i in set_I)>=b[j])

m.minimize(m.sum(c[i,j]*x_vars[i,j] for i in set_I for j in set_J))

tms = m.solve()
tms.display()

