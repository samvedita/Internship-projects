# Task 4: Linear Programming with PuLP

from pulp import LpMaximize, LpProblem, LpVariable, value

# Create the model
model = LpProblem("Maximize_Profit", LpMaximize)

# Define decision variables
A = LpVariable("Product_A", lowBound=0, cat='Integer')
B = LpVariable("Product_B", lowBound=0, cat='Integer')

# Objective function: Maximize profit
model += 40 * A + 30 * B, "Total Profit"

# Constraints
model += 2 * A + 4 * B <= 100, "Labor Constraint"
model += 3 * A + 2 * B <= 90, "Material Constraint"

# Solve the problem
model.solve()

# Output the results
print("Optimal Production Plan:")
print(f"Produce {A.varValue} units of Product A")
print(f"Produce {B.varValue} units of Product B")
print(f"Maximum Profit: ₹{value(model.objective)}")
