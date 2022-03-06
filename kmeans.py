import matplotlib.pyplot as plt
import numpy as np
from sklearn import cluster


np.random.seed(42) # for reproducibility 


def euclidean_distance(x, y):   # x, y are numpy arrays of the same length 
    return np.sqrt(np.sum((x - y) ** 2))

class KMeans:
  def __init__(self, K=5, max_iters=100, plot_steps=False):  #initialize the KMeans class
    self.K = K
    self.max_iters = max_iters   #maximum number of iterations
    self.plot_steps = plot_steps    #plot the steps of the algorithm
 

    # list of sample indices for each cluster
    self.clusters = [[] for _ in range(self.K)] #initialize clusters to empty lists

    # mean of each cluster
    self.centroids = []  #initialize centroids to empty list


  def predict(self, X):   #predict the cluster for each sample
    self.X = X
    self.n_samples, self.n_features = X.shape

    # initialize centroids   
    random_sample_indices = np.random.choice(self.n_samples, self.K, replace=False)   #randomly choose k samples from the dataset
    self.centroids = [self.X[i] for i in random_sample_indices]      #initialize centroids to the randomly chosen samples



    # optimization      iterate until centroids are the same
    for _ in range(self.max_iters):
      # Assign samples to closest centroids (create clusters)
      self.clusters = self._create_clusters(self.centroids)   
      
      if self.plot_steps:
          self.plot()


      # update centroids   for each cluster, return the mean of the samples in the cluster
      centroids_old = self.centroids
      self.centroids = self._get_centroids(self.clusters)   #will assign mean values to each cluster


      # check if converged
      if self._is_converged(centroids_old, self.centroids):           #if centroids are the same, then we have converged
        break

      if self.plot_steps:
          self.plot()

    # return cluster labels
    return self._get_cluster_labels(self.clusters)   #for each cluster, return the index of the sample in the cluster


  def _get_cluster_labels(self, clusters):  #get the cluster label for each sample in the dataset
    labels = np.empty(self.n_samples)

    for cluster_index, cluster in enumerate(clusters):
      for sample_index in cluster:
        labels[sample_index] = cluster_index
    return labels


  def _create_clusters(self, centroids):    #assign the samples to the closest centroids to create clusters
    clusters = [[] for _ in range(self.K)]

    for sample_index, sample in enumerate(self.X):
      centroids_index = self._closest_centroid(sample, centroids)
      clusters[centroids_index].append(sample_index)

    return clusters

  
  def _closest_centroid(self, sample, centroids):    #find the closest centroid to the sample
    distances = [euclidean_distance(sample, point) for point in centroids] #find the distance between the sample and each centroid
    closest_index = np.argmin(distances)
    return closest_index


  def _get_centroids(self, clusters):  #for each cluster, return the mean of the samples in the cluster
    centroids = np.zeros((self.K, self.n_features))  #initialize centroids to 0
    for cluster_index, cluster in enumerate(clusters):
      cluster_mean = np.mean(self.X[cluster], axis=0)  #get the mean of the samples in the cluster
      centroids[cluster_index] = cluster_mean
    return centroids

  def _is_converged(self, centroids_old, centroids):   #check if centroids are the same
    distances = [euclidean_distance(centroids_old[i], centroids[i]) for i in range(self.K)]   #find the distance between the old centroids and the new centroids
    return sum(distances) == 0

    
  def plot(self):
      fig, ax = plt.subplots(figsize=(12, 8))

      for i, index in enumerate(self.clusters):
          point = self.X[index].T
          ax.scatter(*point)

      for point in self.centroids:
          ax.scatter(*point, marker="x", color='black', linewidths=2)

      plt.show()

# Testing
if __name__ == "__main__":
    from sklearn.datasets import make_blobs

    X, y = make_blobs(
        centers=3, n_samples=500, n_features=2, shuffle=True, random_state=40
    )
    print(X.shape)

    clusters = len(np.unique(y))
    print(clusters)

    k = KMeans(K=clusters, max_iters=150, plot_steps=True)
    y_pred = k.predict(X)

    k.plot()