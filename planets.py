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
        # returns list of velocity changes and calculations from momentum changing effects
        # zero index will be gravity/universal changes
        # index beyond that will be interactions with other objects
        # first index will be dist calc
        # second through fourth index (expand as needed) will be unit vectors values
        # third index will be gravity
        velDeltas = np.array(len(objList),3) 
        k = 0
        velDeltas[k,0] = self.vel[0]+gvars.g*gvars.dt
        for obj in objList:
            if self.name != obj.name:
                k += 1
                velDeltas[k,0]   = gvars.dist_calc(  self.pos, obj.pos)
                velDeltas[k,1:2] = gvars.unit_vector(self.pos, obj.pos)
                velDeltas[k,3]   = obj.mass
                # -= gvars.G*self.mass*obj.mass/(dist**2)*gvars.dt*unitVector
        return velDeltas

    # iterates the position and velocity values for the sim
    def RK4_Method(self,obj):
        for i in range(len(self.pos)):
            temp = self.step_vel()
            dist = temp[1:,0]
            unitVector = temp[1:,1:]
            k = np.zeros((2,4))
            k[0,:] = self.pos[i] + self.vel[i]*gvars.dt
            k[0,:] = sum([-1*gvars.G*self.mass*obj[i].mass/(dist[i]**2)*gvars.dt*unitVector[i]])
            k[1,:] = (self.pos[i] + self.vel[i]*gvars.dt*0.5) + k[0,:]*gvars.dt*0.5
            k[2,:]= (self.pos[i] + self.vel[i]*gvars.dt*0.5) + k[1,:]*gvars.dt*0.5
            k[3,:] = (self.pos[i] + self.vel[i]*gvars.dt*0.5) + k[2,:]*gvars.dt*0.5
            self.pos[i] += gvars.dt*(k[0,:]+2*k[1,:]+2*k[2,:]+k[3,:])/6 

    # returns the kinetic energy of the object
    def return_ke(self):
        return 0.5*self.mass*(self.vel.dot(self.vel))

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
