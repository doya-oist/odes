# odes.py
# An Ordinary Differential Equation Simulator
# 2022 by Kenji Doya

import numpy as np
from scipy.integrate import odeint

import matplotlib.pyplot as plt

import importlib  # import module from string

class odes():
    """An ODE Simulator"""
    time = 0
    trun = 10
    dt = 0.1
    
    def __init__(self, odename):
        """create a new ODE"""
        print('Importing ODE:', odename)
        self.ode = importlib.import_module( odename)
        importlib.reload(self.ode) # for updated module
        self.state = self.ode.initial_state
        #self.reset()
        plt.ion()

    def reset(self):
        """reset the state"""
        self.time = 0
        self.state = self.ode.initial_state
        plt.clf()

    def simulate(self):
        """simulate the ODE"""
        # +dt/2 to include time+trun
        self.t = np.arange(self.time, self.time+self.trun+self.dt/2, self.dt)
        self.y = odeint(self.ode.dynamics, self.state, self.t, args=(self.ode.parameters,))
        # update the time and state
        self.time = self.t[-1]
        self.state = self.y[-1,:]
        print("t=", self.time, "; state=", self.state)
        
    def plot(self):
        """plot in time"""
        plt.plot(self.t, self.y)
        plt.xlabel('t'); plt.ylabel('y')

    def run(self):
        """simulate the ODE"""
        self.simulate()
        self.plot()
