This is a simple sim so far for planetary motion. At start I wanted to create a better architecture of the sim first then apply more interesting physics. Will flesh this out further later.

Base functionality understanding.
There is singular state object.
This object contains all objects that are interacted with per step.
State has an overall step function.
State has subprocesses for iterating the velocity and then the position of each object in its list.
State will check for collisions between velocity changes and position changes.
Test type is determined by a command line input