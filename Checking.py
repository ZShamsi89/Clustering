import numpy as np
import msmbuilder.cluster
clust_1=msmbuilder.cluster.KMeans(n_clusters=2)
clust_2=msmbuilder.cluster.KMeans(n_clusters=2)
clust_3=msmbuilder.cluster.KMeans(n_clusters=3)
clust_0=msmbuilder.cluster.KMeans(n_clusters=3)
threshold=0.01

# a=np.array([[1, 0],[2,1],[3,0.2],[5,1],[5.1,0.1],[6,1],[6.1,0]])
a=np.array([[1, 0],[2,1.5],[3,0.2],[5,1],[5.1,-0.1],[6,1],[8,0],[10, 0],[2.5,1.5],[3.7,0.2],[5.4,0.8],[5.5,-0.1],[0.9,1],[8.9,1.2],[1.7, 0.8],[2.5,1],[2.4,0.1],[0.5,1],[2.1,-0.1],[2.3,1]])
A=[a]

clust_1.fit(A)
clust_2.fit(A)
clust_3.fit(A)
clust_0.fit(A)
"""
clust_1.labels_[0][0]=0
clust_1.labels_[0][1]=0
clust_1.labels_[0][2]=0
clust_1.labels_[0][3]=1
clust_1.labels_[0][4]=1
clust_1.labels_[0][5]=1
clust_1.labels_[0][6]=1
clust_2.labels_[0][0]=0
clust_2.labels_[0][1]=0
clust_2.labels_[0][2]=0
clust_2.labels_[0][3]=1
clust_2.labels_[0][4]=1
clust_2.labels_[0][5]=1
clust_2.labels_[0][6]=1
clust_3.labels_[0][0]=0
clust_3.labels_[0][1]=0
clust_3.labels_[0][2]=1
clust_3.labels_[0][3]=1
clust_3.labels_[0][4]=1
clust_3.labels_[0][5]=2
clust_3.labels_[0][6]=2
clust_0.labels_[0][0]=0
clust_0.labels_[0][1]=0
clust_0.labels_[0][2]=0
clust_0.labels_[0][3]=1
clust_0.labels_[0][4]=1
clust_0.labels_[0][5]=2
clust_0.labels_[0][6]=2

nFrame=7
"""

nFrame=20
D=np.empty((nFrame, nFrame))
nClusters=4

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

# Second step, making np(nCluster) different clusters of D
A=[D]
nClusters=4
myn_clusters=3

for i in range(nClusters):
	exec("clust2_" + str(i) + " =msmbuilder.cluster.KMeans(n_clusters=" + str(myn_clusters) + ")" )
	exec("clust2_" + str(i) + ".fit(A)" ) 

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

# Third step

A=[D2]
nClusters=4
myn_clusters=3
D3=np.empty((nFrame, nFrame))

for i in range(nClusters):
        exec("clust2_" + str(i) + " =msmbuilder.cluster.KMeans(n_clusters=" + str(myn_clusters) + ")" )
        exec("clust2_" + str(i) + ".fit(A)" )
"""
clust2_1=msmbuilder.cluster.KMeans(n_clusters=3)
clust2_2=msmbuilder.cluster.KMeans(n_clusters=3)
clust2_3=msmbuilder.cluster.KMeans(n_clusters=3)
clust2_0=msmbuilder.cluster.KMeans(n_clusters=3)

clust2_1.fit(A)
clust2_2.fit(A)
clust2_3.fit(A)
clust2_0.fit(A)
"""
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
