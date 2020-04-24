# PieKDE
piekde is a implementation of a kernel density estimator. 

## why kdes?
you have a handful of observations but not the true data generating function `P(X)`. 

you can approximate `P(x)` using a kde. you could then draw from this approximation for new samples (eg digits, faces).

## kdes are gmms but with lots and lots of gaussians
with gaussian mixture models, we have a k gaussians that emit observations, where k < n. 

with kdes, we assume each data point represents a gaussian. because we no longer need to specify the number of gaussians for our approximating function, kdes are considered non-parametric.