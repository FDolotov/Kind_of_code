import numpy as np
from numba import compiler, types
from scipy import integrate
import matplotlib.pyplot as plt
import time


t0 = 0.
t1 = 100.   
vars = np.array([1.,1.])
params = np.array([1., 1.5, 2., 1.5])

def f(t,vas, params):
    return np.array([(params[0] - params[1]*vas[1])*vas[0], (-params[2] + params[3]*vas[0])*vas[1]])



start_time1 = time.time()
f(t1, vars, params)
print('time -', time.time() - start_time1)

start_time2 = time.time()
prop = integrate.ode(f)
prop.set_integrator('dop853').set_f_params(params).set_initial_value(vars, t0)
prop.integrate(t0)
print('time2 -', time.time() - start_time2)

values = np.array([prop.integrate(x) for x in np.linspace(t0,t1,10000)])

start_time3 = time.time()
crtbp_compiled = compiler.compile_isolated(f, [types.double, types.double[:], types.double[:]], return_type=types.double[:]).entry_point
print('time3 -', time.time() - start_time3)

start_time4 = time.time()
prop2 = integrate.ode(crtbp_compiled)
prop.set_integrator('dop853').set_f_params(params).set_initial_value(vars, t0)
prop.integrate(t0)
print('time4 -', time.time() - start_time4)

cringe = np.array([params[2]/params[1], params[0]/params[1]])

start_time5 = time.time()
for i in np.linspace(0.1, 0.9, 9):
    x0 = i * cringe
    x = np.array([prop.set_initial_value(x0, t0).integrate(t) for t in np.linspace(t0, 10, 100)])
    #print(x)
    plt.plot(x[:, 0], x[:, 1])
#
print('time5 -', time.time() - start_time5)
plt.show()

pog = np.array([])
pog = np.array([f(t1, values[i], params) for i  in range(len(values))])
#print(pog)
plt.plot(pog[:, 0], values[:, 0])
plt.plot(pog[:, 1], values[:, 1])
