import numpy as np
from simpleInitialization import simpleInitialization

def kmeans(X, k):
    # Intialize centroids
    centroids = simpleInitialization(X, k)
    labels = np.zeros(X.shape[0])
    n_it = 100
     # ====================== ADD YOUR CODE HERE ======================
    # Instructions: Run the main k-means algorithm. Follow the steps 
    #               given in the description. Compute the distance 
    #               between each instance and each centroid. Assign 
    #               the instance to the cluster described by the closest
    #               centroid. Repeat the above steps until the centroids
    #               stop moving or reached a certain number of iterations
    #               (e.g., 100).




    
    # ===============================================================
    
    # Run main k-means algorithm
    for i in range(n_it):
        # Compute distances from the centroid to points
        distances = np.array([np.linalg.norm(X-centroid, axis = 1)
                             for centroid in centroids]).T
        
        #Compute nearest centroid indices      
        labels = np.argmin(distances, axis = 1)
        
        # Find new centroids 
        before_centroids = np.copy(centroids)
        centroids = np.array([np.mean(X[labels == i], axis = 0)
                              for i in range(k)])
        
        if (np.array_equal(before_centroids,centroids)):
            break
    print('We found the solution in ' + str(i) + ' iterations!')

    return labels