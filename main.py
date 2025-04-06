import matplotlib.pyplot as plt
import numpy as np
import gvars
from planets import Planet
from stateManager import StateManager
import sys, os

test = 2
idt = 0.0001
simLength = 10
sim_steps = int(simLength/idt)

def sim_setup(test):
    # This function allows the conglomeration of many unit test setups
    if test == 0: # basic gravity test
        gvars.init(ig=-10.0,idt=0.0001,iBounceCoef = 0.5)
        Earth = Planet(iname='Earth', ivel = np.array([0,  0.25]), ipos=np.array([10, 0]), iradius=0.25)
        state = StateManager(iobjList=[Earth])

    if test == 1: # basic collision test
        gvars.init(ig=0.0,idt=0.0001,iBounceCoef = 0.5)
        Earth = Planet(iname='Earth', ivel = np.array([0,  0.25]), ipos=np.array([0, 0]), iradius=0.25)
        Mars  = Planet(iname='Mars',  ivel = np.array([0, -0.25]), ipos=np.array([0, 2]), iradius=0.25)
        state = StateManager(iobjList=[Earth, Mars])

    if test == 2: # complex collision test CURRENTLY BROKEN
        gvars.init(ig=0.0,idt=0.0001,iBounceCoef = 0.5)
        Earth = Planet(iname='Earth', ivel = np.array([1,  1]), ipos=np.array([1, 0]), iradius=0.25)
        Mars  = Planet(iname='Mars',  ivel = np.array([-1, -1]), ipos=np.array([6, 5]), iradius=0.25)
        state = StateManager(iobjList=[Earth, Mars])

    if test == 3: # complex collision simple gravity test LIKELY BROKEN
        gvars.init(ig=-10.0,idt=0.0001,iBounceCoef = 0.5)
        Earth = Planet(iname='Earth', ivel = np.array([0,  0.25]), ipos=np.array([0, 0]), iradius=0.25)
        Mars  = Planet(iname='Mars',  ivel = np.array([10, 0.25]), ipos=np.array([5, 0]), iradius=0.25)
        state = StateManager(iobjList=[Earth, Mars])
    return state

def Main(inputTest):
    state = sim_setup(inputTest)
    for i in range(sim_steps):
        state.step()
        state.time += gvars.dt
    if state.debug:
        debug_printout(state)

def debug_printout(state):
    t = np.linspace(0,10,sim_steps)
    # 13412:13417

    f = plt.figure()
    ax = f.subplots(2,2)
    ax[0,0].set_title('Y Pos')
    [ax[0,0].plot(t,state.yPos[:,i]) for i in range(len(state.objList))]

    ax[0,1].set_title('Y Vel')
    [ax[0,1].plot(t,state.yVel[:,i]) for i in range(len(state.objList))]

    ax[1,0].set_title('X Pos')
    [ax[1,0].plot(t,state.xPos[:,i]) for i in range(len(state.objList))]

    ax[1,1].set_title('X Vel')
    [ax[1,1].plot(t,state.xVel[:,i]) for i in range(len(state.objList))]
    plt.show()


    [plt.plot(state.xPos[:,i],state.yPos[:,i]) for i in range(len(state.objList))]
    plt.show()

Main(test)