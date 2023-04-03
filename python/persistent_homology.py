import gudhi
import numpy as np

theta = np.linspace(0, 2 * np.pi, 50)
phi = np.linspace(0, np.pi, 50)
theta, phi = np.meshgrid(theta, phi)
theta, phi = theta.flatten(), phi.flatten()
x = np.sin(phi) * np.cos(theta)
y = np.sin(phi) * np.sin(theta)
z = np.cos(phi)
data = np.array([x, y, z]).T


rips_complex = gudhi.RipsComplex(points=data, max_edge_length=2)
simplex_tree = rips_complex.create_simplex_tree(max_dimension=2)
diag = simplex_tree.persistence()


gudhi.plot.plot_persistence_barcode(diag)
