# PieKDE
piekde is a simple implementation of a kernel density estimator. 

## why kdes?
you have a handful observations but not the true data generating function. you want this  distribution (or an approximation) so you can do things like generate new samples.

## kdes are gmms but with lots of gaussians
with gaussian mixture models, we have a k gaussians that emit observations, where k < n. with kdes, we assume each data point anchors a gaussian. (because we no longer need to specify the number of gaussians underlying the true data generating function, kdes are considered non-parametric.)