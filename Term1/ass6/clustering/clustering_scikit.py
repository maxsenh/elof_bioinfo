import numpy as np
from sklearn import cluster

# Load the data from the file, numbers are separated by commas.
data = np.loadtxt('expression_parsed.dat', delimiter=',')

ids = open("ids.txt")
listid=[]
for line in ids:
    line1 = line.strip().split('|')
    listid.append(line1[1].strip())
# Start the clustering object
km = cluster.KMeans(4)
hc = cluster.AgglomerativeClustering(4)

# Find the centroids and predict to which cluster would they belong on the same data.
indexeskm = km.fit_predict(data)
indexeshc = hc.fit_predict(data)
for i in range(len(listid)):
    print("%d Sequencename: %s clustKM %d clustHC %d"%(i+1,listid[i],indexeskm[i],indexeshc[i]))

        


