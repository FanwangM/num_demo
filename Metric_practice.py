import numpy as np

# mock feature matrix
feature = np.array([  [4, 2, 6],
                      [4, 9, 6],
                      [2, 5, 0],
                      [2, 0, 9],
                      [5, 3, 0]])


def euclidean_distance(x, y):
    """
    Computes the euclidean distance between two vectors
    ----------
    Parameters
    ----------
    x : first vector
    y : second vector
    -------
    Returns
    -------
    distance : euclidan distance between x and y
    """
    intermdiate = 0
    for i in range(0, len(x)):
        intermdiate += ((x[i] - y[i])**2)
    distance = np.sqrt(intermdiate)
    return distance


def pairwaise_distance(matrix):
    """
    Computes the pairwise distance between each vectore
    in a given matrix
    ----------
    Parameters
    ----------
    matrix : given matrix
    -------
    Returns
    -------
    perwise_distance : the condensed pairwise distance
    """
    per_dist = []
    for i in range(0,(len(matrix)-1)):
        for j in range(i + 1,(len(matrix))):
            per_dist.append(euclidean_distance(matrix[i],matrix[j]))
    return per_dist

print(pairwaise_distance(feature))
