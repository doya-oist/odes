# first.py
# first-order linear ODE
# Dec. 2018 by Kenji Doya

import numpy as np

# Right-hand-side function of the ODE
def dynamics(y, t, a):
    """first-order linear ODE: dy/dt = a[0]*y + a[1]"""
    return a[0]*y + a[1]

# Default parameters
parameters = [-0.1, 0]

# Default initial state
initial_state = -1
