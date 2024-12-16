# second.py
# second-order linear ODE
# Dec. 2018 by Kenji Doya

import numpy as np

# Right-hand-side function of the ODE
def dynamics(y, t, a):
    """second-order linear ODE:
        d2y/dt2 = a[0]*dy/dt + a[1]*y + a[2]"""
    yt, dydt = y
    return np.array([dydt, a[0]*dydt + a[1]*yt + a[2]])

# Default parameters
parameters = [-0.1, -1, 0]

# Default initial state
initial_state = [-1, 0]
