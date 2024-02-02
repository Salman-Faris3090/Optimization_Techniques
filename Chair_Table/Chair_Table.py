from scipy.optimize import linprog
obj = [-20, -30]# Objective Function Values 
lhs = [[ 1, 5], [3,  1]] #LHS Constraints 
rhs =[125, 80] #RHS Constraints
bnd = [(0, float("inf")),(0, float("inf"))] #Bounds Of X and Y
result = linprog(c=obj, A_ub=lhs, b_ub=rhs, bounds=bnd) #function
print(result.x)