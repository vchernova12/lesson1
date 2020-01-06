import pulp as p 
  
# Create a LP Maximize problem 
Lp_prob = p.LpProblem('Display problem', p.LpMaximize)  
  
# Create problem Variables  
x1 = p.LpVariable("BB1", lowBound = 4, upBound= 4, cat= p.LpInteger)   # Create a variable x1 >= 2
x2 = p.LpVariable("BB2", lowBound = 4, upBound = 10, cat= p.LpInteger)   # Create a variable x2 >= 2 
y1 = p.LpVariable("SS1", lowBound = 4, upBound= 18, cat= p.LpInteger)   # Create a variable x3 >= 2  
y2 = p.LpVariable("SS2", lowBound = 4, upBound= 18, cat= p.LpInteger)   # Create a variable x3 >= 2  
y3 = p.LpVariable("SS3", lowBound = 4, upBound= 4, cat= p.LpInteger)   # Create a variable x3 >= 2  
# Objective Function 
Lp_prob += 1.96721*64.15 * x1 + 1.5985*64.15*x2 + 3.29025*96.22*y1 +4.03891*96.22*y2+3.73469*96.22*y3
  
# Constraints: 
#Lp_prob += x1 <= 10
#Lp_prob += x2 <= 8
#Lp_prob += x3 <= 20
Lp_prob += 1967.21*x1+1598.5*x2+3290.25*y1 + 4038.91*y2+3734.69*y3 <= 81848.86
Lp_prob += x2-x1 <= 10-4
Lp_prob += y1-x1 <= 18-4
Lp_prob += y2-x1 <= 18-4
Lp_prob += y3-x1 <= 0
Lp_prob += y1-x2 <= 18-10
Lp_prob += y2-x2 <= 18-10
Lp_prob += x2-y3 <= 18-4
Lp_prob += y1-y2 <= 0
Lp_prob += y1-y3 <= 18-4
Lp_prob += y2-y3 <= 18-4
# Display the problem 
print(Lp_prob) 
  
status = Lp_prob.solve()   # Solver 
print(p.LpStatus[status])   # The solution status 
  
# Printing the final solution 
print(p.value(x1), p.value(x2),p.value(y1),p.value(y2),p.value(y3), p.value(Lp_prob.objective))   