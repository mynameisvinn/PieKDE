import math
import numpy as np

def _kernel(point, observation, bandwidth):
    """
    observation refers to the point where the kernel is centered. think of it as the
    anchor point. 
    
    formula from https://medium.com/analytics-vidhya/kernel-density-estimation-kernel-construction-and-bandwidth-optimization-using-maximum-b1dfce127073
    
    code from https://stackoverflow.com/questions/12412895/calculate-probability-in-normal-distribution-given-mean-std-in-python
    """
    denom = bandwidth * ((2*math.pi)**.5)    
    num = math.exp(-0.5 * ((point-observation)/bandwidth)**2)
    return num/denom

def kde(observations, bandwidth):

    delta = np.max(observations) - np.min(observations) 
    low = np.min(observations) - delta
    high = np.max(observations) + delta
    
    k = high - low  # number of points
    sum_densities = np.zeros(k)
    for obs in observations:
        sum_densities += np.array(list(
            map(lambda pt: _kernel(pt, observation=obs, bandwidth=bandwidth), np.arange(low, high))))
    sum_densities /= len(observations)
    return sum_densities