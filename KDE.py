import math
import numpy as np

class KDE(object):
    def __init__(self):
        self.observations = 0

    def _kernel(self, point, observation, bandwidth):
        """
        each observation refers to the point where the gaussian is centered. 
    
        formula from https://medium.com/analytics-vidhya/kernel-density-estimation-kernel-construction-and-bandwidth-optimization-using-maximum-b1dfce127073

        code from https://stackoverflow.com/questions/12412895/calculate-probability-in-normal-distribution-given-mean-std-in-python
        """
        denom = bandwidth * ((2*math.pi)**.5)    
        num = math.exp(-0.5 * ((point-observation)/bandwidth)**2)
        return num/denom


    def fit(self, observations, low, high, size, bandwidth):
        self.observations = observations
        self.bandwidth = bandwidth
        
        sum_densities = np.zeros(size)
        for obs in observations:
            sum_densities += np.array(list(
                map(lambda pt: self._kernel(pt, observation=obs, bandwidth=bandwidth), np.linspace(low, high, size))))
        sum_densities /= len(observations)
        return sum_densities

    
    def sample(self, size):
        """draw samples from a fitted KDE.

        sampling from KDE can be viewed as uniform sampling of its gaussians.
        """
        if len(self.observations) == 0:
            raise ValueError("need to fit KDE with observations")

        samples = np.zeros(size)
        for i in range(size):
            
            # randomly select an anchor point for a gaussian
            anchor_point = np.random.choice(self.observations)

            # then sample from that gaussian
            sample = np.random.normal(loc=anchor_point, scale=self.bandwidth)
            samples[i] = sample
        return samples