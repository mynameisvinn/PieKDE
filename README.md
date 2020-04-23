# PieKDE
piekde is a simple implementation of a kernel density estimator. 

## why kdes?
you have a handful observations but you want a continuous probability distribution (perhaps so you can draw this distribution). a kernel density smooths out distributions.

## intuition
the approximate distribution should have its mass concentrated around observations. it doesnt have to be exact; the point is that - if you were to draw new observations - you should have a higher relative likelihood of drawing a sample near seen observations.