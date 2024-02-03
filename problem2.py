import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Define functions 
def f(r):
    return r

def g(r, R0):
    return 1 - np.exp(-R0 * r)

def r_equation(r, R0):
    return r - (1 - np.exp(-R0 * r))

R0_value = 1.2

## Array of values for r
r_values = np.linspace(0, 5, 1000)

f_values = f(r_values)
g_values = g(r_values, R0_value)
r_equation_values = r_equation(r_values, R0_value)

intersection_points = fsolve(lambda r: r_equation(r, R0_value), [1.0, 3.0])

plt.plot(r_values, f_values, label='f(r) = r')
plt.plot(r_values, g_values, label='g(r) = 1 - e^(-R0*r)')

plt.scatter(intersection_points, [f(r) for r in intersection_points], color='blue', marker='o', label='Intersection Points')

plt.xlabel('r')
plt.ylabel('Function values')
plt.legend()
plt.title('f(r) and g(r)')

plt.show()

out_file = 'prob2'

plt.savefig(out_file,bbox_inches='tight')
