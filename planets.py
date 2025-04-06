import matplotlib.pyplot as plt
import numpy as np
import gvars

class Planet:
    # initializer for the planet object
    def __init__(self,iname='Generic',iradius=1,icolor=[255,255,255],ipos=np.array([0.0,0.0]),ivel=np.array([0.0,0.0]),imass = 0):
        self.name   = iname
        self.radius = iradius
        self.color  = icolor # this should be a list of three ints from 0-255. Going to define a function that allows me to return the value as the hexcode string
        self.pos    = ipos.astype(np.float64)
        self.vel    = ivel.astype(np.float64)
        self.mass   = imass

    # for coloration during visualizers and debugging
    def return_color(self):
        r = hex(self.color[0])[2:]
        g = hex(self.color[1])[2:]
        b = hex(self.color[2])[2:]
        return f'#{r:02}{g:02}{b:02}'

    # changes the velocity of the objects during the basic steps
    def step_vel(self,objList):
        self.vel[0] = self.vel[0]+gvars.g*gvars.dt
        # self.vel += [(gvars.G*self.mass*obj.mass)/(gvars.dist_calc(self.pos,obj.pos)**2)*gvars.dt*gvars.unit_vector(self.pos, obj.pos) for obj in objList]

    # changes position of the object based on its current velocity
    def step_pos(self):
        self.pos[0] += self.vel[0]*gvars.dt
        self.pos[1] += self.vel[1]*gvars.dt
        self.ground_collision()
 
    # simple ground collision physical simulation.
    def ground_collision(self):
        if self.pos[0] <= gvars.ybound[0] + self.radius:
            self.pos[0] = -1*(self.pos[0] - gvars.ybound[0] - self.radius) + gvars.ybound[0] + self.radius
            self.vel[0] = -self.vel[0] * gvars.bounce_coef
