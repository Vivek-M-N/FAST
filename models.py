'''
Bicycle model simulation using Python with
GUI, input file and visualization.

config data in order: timestep, total time, mass, wheelbase, track, cg distance from front
'''

import numpy as np

class Bicycle:
    def __init__(self, config):
        self.dt = config[0]  #Timestep
        self.total_time = config[1]  #Total simulation time
        self.__m = config[2]  #Mass
        self.__L = config[3]  #Wheelbase
        self.__W = config[4]  #Track width
        self.__a = config[5]  #CG distance from front axle
        self.__b = self.__L - self.__a  #CG distance from rear axle

        print("Bicycle created with mass {}kg, wheelbase {}m, track {}m".format(self.__m, self.__L, self.__W))

        #Velocities
        self.__vx = 0  #Longitudinal velocity
        self.__vy = 0  #Lateral velocity
        self.__vz = 0  #Vertical Velocity
        self.__wx = 0  #Roll velocity
        self.__wy = 0  #Pitch velocity
        self.__wz = 0  #Yaw velocity

        self.__delta = 0  #Steering angle

        #Accelerations
        self.__ax = 0   #Longitudinal acceleration
        self.__ay = 0   #Lateral acceleration
        self.__az = 0   #Vertical acceleration
        self.__alx = 0  #Roll acceleration
        self.__aly = 0  #Pitch acceleration
        self.__alz = 0  #Yaw acceleration

        #Global position
        self.__x = 0  #X position
        self.__y = 0  #Y position
        self.__z = 0  #Z position

    def update(self, vx_input, delta):
        self.__delta = delta  #Update steering angle
        self.__vx = vx_input  #Directly set longitudinal velocity

        #Yaw rate calculation
        self.__wz = self.__vx/(self.__L/np.tan(self.__delta)) if abs(self.__delta) > 1e-5 else 0

        #Lateral velocity and acceleration calculation
        self.__ay = self.__wz * self.__vx
        self.__vy = self.__wz * self.__b

        #Global position calculation
        self.__x += self.__vx * self.dt * np.cos(self.__wz)
        self.__y += self.__vx * self.dt * np.sin(self.__wz)
        self.__z = 0

        self.states = [self.__x, self.__y, self.__z, self.__vx, self.__vy, self.__vz, 
                       self.__wx, self.__wy, self.__wz, self.__ax, self.__ay, self.__az,]
        return self.states
