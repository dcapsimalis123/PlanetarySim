import numpy as np
import gvars

def dist_calc(pos1, pos2):
    temp = pos1 - pos2
    return np.sqrt(temp[0]**2+temp[1]**2)

class StateManager:
    def __init__(self, iobjList = [], itime = 0, idebug = True):
        self.objList = iobjList
        self.debug = idebug
        self.time = itime
        self.stepNum = 0

        sim_steps = int(gvars.simLength/gvars.dt)
        if self.debug:
            self.yPos = np.zeros((sim_steps, len(self.objList)))
            self.yVel = np.zeros((sim_steps, len(self.objList)))
            self.xPos = np.zeros((sim_steps, len(self.objList)))
            self.xVel = np.zeros((sim_steps, len(self.objList)))

    def collision_handler(self):        
        # probably find some weird way to solve energy momentum discrepency
            # for now assume only two objects can collide at once. If greater than that it will become trickier
        tempPos = np.zeros((2,len(self.objList)))
        for i, obj in enumerate(self.objList):
            tempPos[i,:] = obj.pos + obj.vel*gvars.dt
        
        I = 0

        for i in range(len(self.objList)): # can use i and j to set the obj in objList with objList[var] but I need to be certain that it doesn't change through cycles (it should but I'd want to verify)
            if I != 1: # this is a hack solution to prevent double bouncing in the same listing, I need to remove this and replace it with a setup that instead just ignores the next movement
                # Going to change this out for a logic out for transfer of momentum between the objects only in the distance vector direction. Want to do some reading on how most sims handle collision physics. Feels like solving for both p and K for both every contact. Two object collision is easy, more object collision will take a long time.
                for j in range(len(self.objList)):
                    if dist_calc(tempPos[i],tempPos[j]) <= self.objList[i].radius + self.objList[j].radius and i != j:
                        I += 1
                        bounceSlope = np.array([tempPos[j][1]-tempPos[i][1], tempPos[i][0]-tempPos[j][0]])
                        bounceSlope = bounceSlope/np.sqrt(bounceSlope.dot(bounceSlope))
                        diffSlope   = np.array([tempPos[i][0]-tempPos[j][0], tempPos[i][1]-tempPos[j][1]])
                        diffSlope   = diffSlope/np.sqrt(diffSlope.dot(diffSlope))
                        self.objList[i].vel = self.objList[i].vel.dot(bounceSlope)*bounceSlope - self.objList[i].vel.dot(diffSlope)*diffSlope
                        self.objList[j].vel = self.objList[j].vel.dot(bounceSlope)*bounceSlope - self.objList[j].vel.dot(diffSlope)*diffSlope
                        break

                     

    def step(self):
        for obj in self.objList:
            obj.step_vel()

        if len(self.objList) > 1:
            self.collision_handler()

        for obj in self.objList:
            obj.step_pos()

        if self.debug: # Use this to store all information I may want for graphing purposes
            for i, obj in enumerate(self.objList):
                self.yPos[self.stepNum,i] = obj.pos[0]
                self.yVel[self.stepNum,i] = obj.vel[0]
                self.xPos[self.stepNum,i] = obj.pos[1]
                self.xVel[self.stepNum,i] = obj.vel[1]
        
        self.stepNum += 1



    # Psuedo ===============================================
    # 1.  maybe move the object list into here as global variable (check)
    # 2.  have step be a function in here (check)
    # 2a. have step have as part of debug mode be the trackign of variables like pos and vel (check)
    # 2b: step the velocity (check)
    # 2c: check with velocity calcs if there is going to be a collision, handle appropriately (check)
    # 2d: move positions forward as normal (check)
    # 2e: iterate step number

    # Major Notes for next steps
    # 1. I need to decide on the nature of how to sim collisions
    # 2. I need to iterate on the detection logic for distance
    #   a: I really like the idea of a nxn matrix, or perhaps a nxnx2 matrix? should be linearlizable
    #      and thus be scalable to an O(n) problem also, could allow for multiple detections more easily 
    #      probably decently memory intensive though.
    # 3. Update the vel_step function to adjust for interaction forces. Might need to make dist_calc a 
    #       global function or something so as to be easier to work with. Or I could use the nxn matrix
    #       concept to have large matrix of distance matrix for each object for all others.