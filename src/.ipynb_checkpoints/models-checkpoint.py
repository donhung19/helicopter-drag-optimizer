class Helicopter:
    def __init__(self, data):
        self.name = data['name']
        self.W = data['weight']
        self.f = data['flat_plate_area']
        self.R = data['rotor_radius']
        self.k = data['k_factor']
        self.sigma = data['solidity']
        self.V_tip = data['tip_speed']
        self.rho = 1.225