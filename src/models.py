import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

class Helicopter:
    def __init__(self, data):
        self.name = data.get('name')
        self.rho = data.get('rho')
        self.f_factor = data.get('f_factor')

        self.weight = data.get('weight')
        self.k_factor = data.get('k_factor')
        self.rotor_radius = data.get('rotor_radius')

    def CalculateDrag(self, v_range):
        Dp = 0.5 * self.rho * v_range**2 * self.f_factor
        Di = (self.k_factor * self.weight**2) / (2 * self.rho * v_range**2 * (np.pi) * self.rotor_radius**2)
        return Dp, Di
    
    def FindOptimalVelocity(self, v_range):
        Dp, Di = self.CalculateDrag(v_range)
        Dt = Dp + Di
        index_opt = np.argmin(Dt)
        v_opt = v_range[index_opt]
        D_min = Dt[index_opt]
        return v_opt, D_min
    
    def GetResult(self, v_range):
        v_otp, d_min = self.FindOptimalVelocity(v_range)
        return {
            "name": self.name,
            "weight": self.weight,
            "v_optimal_mps": round(v_otp, 2),
            "min_total_drag_n": round(d_min, 2)
        }

