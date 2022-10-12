import numpy as np
from scipy import optimize, stats
import matplotlib.pyplot as plt


mean = np.array([1., 2.])
cov = np.array([[1., 0.9], [0.9, 1.]])
x, y = np.random.multivariate_normal(mean, cov, 100).T
X = np.stack([np.ones_like(x), x], axis=1)

ngrid = 100
mu_1, mu_2, sd_1, sd_2 = 0, 10, 2**2, 10**2
A = np.linspace(-4, 4, ngrid)
B = np.linspace(-10, 30, ngrid)

mu = np.array([0, 10])
s = np.array([[22, 102]])
Rho = np.array([[1, 0.5], [0.5, 1]])
Sigma = Rho * np.outer(s, s)
prior = stats.multivariate_normal([mu_1, mu_2], Sigma)

def prop_likelihood(input_values):
    ilogit_abx = 1 / (np.exp(-(input_values[...,0][...,None]*np.ones(x.shape) + input_values[...,1][...,None] * x)) + 1)
    return np.prod(ilogit_abx**y * (1 - ilogit_abx)**(n - y), axis=ilogit_abx.ndim -1)

grid_a , grid_b = np.meshgrid(A,B)
grid = np.empty(grid_a.shape + (2,)) 
grid[:, :, 0] = grid_a
grid[:, :, 1] = grid_b

posterior_density = prior.pdf(grid)*prop_likelihood(grid)