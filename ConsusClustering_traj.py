import numpy as np
import msmbuilder.cluster

def save_object(obj, filename):
        import pickle
        with open(filename, 'wb') as output:
                pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

# dataset = [np.load('phi_psi_chi/00000000.npy')]
dataset = [np.load('phi_psi_chi2/00000000.npy')]
assert dataset[0].ndim == 2
myn_clusters=5
nClusters=4
threshold=0.01

for i in range(nClusters):
        exec("clust_" + str(i) + " =msmbuilder.cluster.KMeans(n_clusters=" + str(myn_clusters) + ")" )
        exec("clust_" + str(i) + ".fit(dataset)" )
	exec("save_object(clust_" + str(i) + ", 'clust_" + str(i) + ".pkl' )")

nFrame=len(clust_1.labels_[0])

D=np.empty((nFrame, nFrame))

for i in range(nFrame):
        for j in range(nFrame):
                sum=0
                cons_sum=0
                for c1 in range(nClusters):
                        exec("cl = clust_" + str(c1))
                        if cl.labels_[0][i]==cl.labels_[0][j]:
                                cons_sum=cons_sum+1                       
			sum=sum+1
                D[i][j]=cons_sum/float(sum)
		if D[i][j]<threshold:
			D[i][j]=0
print "D"
print D
print "Is 0.75 in D?"
print 0.75 in D
print "Is 0.5 in D?"
print 0.5 in D
save_object(D, 'D.pkl')

# Second step, making np(nCluster) different clusters of D
A=[D]
#nClusters=4
#myn_clusters=3
for i in range(nClusters):
	exec("clust2_" + str(i) + " =msmbuilder.cluster.KMeans(n_clusters=" + str(myn_clusters) + ")" )
	exec("clust2_" + str(i) + ".fit(A)" ) 
	exec("save_object(clust2_" + str(i) + ", 'clust2_" + str(i) + ".pkl' )")
D2=np.empty((nFrame, nFrame))
for i in range(nFrame):
        for j in range(nFrame):
                sum=0
                cons_sum=0
                for c1 in range(nClusters):
                        exec("cl = clust2_" + str(c1))
                        if cl.labels_[0][i]==cl.labels_[0][j]:
                                cons_sum=cons_sum+1
                        sum=sum+1
                D2[i][j]=cons_sum/float(sum)
		if D[i][j]<threshold:
			D[i][j]=0
print "D2"
print D2
save_object(D2, 'D2.pkl')
print "0.75 in D2"
print 0.75 in D2
print "0.5 in D2"
print 0.5 in D2

"""
# Third step

A=[D2]
nClusters=4
myn_clusters=3
D3=np.empty((nFrame, nFrame))

for i in range(nClusters):
        exec("clust2_" + str(i) + " =msmbuilder.cluster.KMeans(n_clusters=" + str(myn_clusters) + ")" )
        exec("clust2_" + str(i) + ".fit(A)" )

clust2_1=msmbuilder.cluster.KMeans(n_clusters=3)
clust2_2=msmbuilder.cluster.KMeans(n_clusters=3)
clust2_3=msmbuilder.cluster.KMeans(n_clusters=3)
clust2_0=msmbuilder.cluster.KMeans(n_clusters=3)

clust2_1.fit(A)
clust2_2.fit(A)
clust2_3.fit(A)
clust2_0.fit(A)
for i in range(nFrame):
        for j in range(nFrame):
                sum=0
                cons_sum=0
                for c1 in range(nClusters):
                        exec("cl = clust2_" + str(c1))
                        if cl.labels_[0][i]==cl.labels_[0][j]:
                                cons_sum=cons_sum+1
                        sum=sum+1
                D3[i][j]=cons_sum/float(sum)
		if D3[i][j]<threshold:
			D[i][j]=0

print "D3"
print D2

"""
# How to open pkl file:
# from msmbuilder.cluster import load
# myvar = load('myfile.pkl')
