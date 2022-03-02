import numpy as np

# mock feature matrix
feature = np.array([[4, 2, 6],
                    [4, 9, 6],
                    [2, 5, 0],
                    [2, 0, 9],
                    [5, 3, 0]])


def euclidean_distance(x, y):
    """The distance between two vectors
    
    Computs the eucladian distance between vectors x and y.
    
    Parameters
    ----------
    x : array_like
        the first feature vector
    y : array_like
        the second feature vector
   
    Returns
    -------
    distance : ndarray
        the euclidean distance between the two vectors
    """
    distance = np.sqrt(sum(((x - y)) ** 2))
    return distance


def pairwise_distance(z):
    """Pairwise distance between vectors

    Computes the pairwise distance between each vector in a given array.
    
    Parameters
    ----------
    z : ndarray
        an m by n array
    
    Returns
    -------
    per_dist : ndarray
        the condensed pairwise distance matrix
    """
    per_dist = []
    for i in range(0, (len(z) - 1)):
        for j in range(i + 1, (len(z))):
            per_dist.append(euclidean_distance(z[i],z[j]))
    return per_dist


if __name__ == "__main__":
    print(pairwise_distance(feature))
