'''
    This script tries to use a random number generator
    that samples a value from a uniform distribution 
    between (0,1) to estimate the value of pi.
    
    The intuition behind the function created is that the
    ratio of the areas of a circle and a square having a 
    length equal to the circles diameter is pi/4.
    
    So if we are able to estimate the number of times a point in 
    2D space falls within a circle versus outside the circle bounded 
    by a square out of a number of trials, we will be able to estimate pi
'''

import numpy as np


def estimate_pi(n_trials):
    #counter variable to estimate the probability
    ctr = 0
    for i in range(n_trials):
        #sample a 2d coordinate
        x = np.random.random()
        y = np.random.random()
        #count the number of times the coordinate falls within the circle radius
        if (x**2+y**2) < 1:
           ctr+=1
    #multiply by 4 to get pi since the probability is equal to pi/4           
    return 4*(ctr/n_trials)


