import matplotlib.pyplot as plt
import numpy as np
import gvars

class Planet:
    def __init__(self,iname='Generic',iradius=1,icolor=[255,255,255],ipos=np.array([0,0]),ivel=np.array([0,0])):
        self.name   = iname
        self.radius = iradius
        self.color  = icolor # this should be a list of three ints from 0-255. Going to define a function that allows me to return the value as the hexcode string
        self.pos    = ipos.astype(np.float64)
        self.vel    = ivel.astype(np.float64)

    def return_color(self):
        r = hex(self.color[0])[2:]
        g = hex(self.color[1])[2:]
        b = hex(self.color[2])[2:]
        return f'#{r}{g}{b}'
    
    def step_vel(self):
        self.vel[0] = self.vel[0]+gvars.g*gvars.dt

    def step_pos(self):
        self.pos[0] += self.vel[0]*gvars.dt
        self.pos[1] += self.vel[1]*gvars.dt
        self.ground_collision()
 
    def ground_collision(self):
        if self.pos[0] <= gvars.ybound[0] + self.radius:
            self.pos[0] = -1*(self.pos[0] - gvars.ybound[0] - self.radius) + gvars.ybound[0] + self.radius
            self.vel[0] = -self.vel[0]*gvars.bounce_coef
