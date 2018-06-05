import numpy as np
from scipy import cluster

# Load the data from the file, numbers are separated by commas.
data = np.loadtxt('expression_parsed.dat', delimiter=',')

centroids, indexes = cluster.vq.kmeans2(data, 3)
print(indexes)

