import numpy as np

def normalize(arr):
    '''
    Takes a numpy array and normalizes it - compressing 
    the values into the range [0, 1]

    Example:

        arr = np.array([5, 6, 7, 8, 9, 10])
        normalize(arr)

    Would return:

        np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
    '''
    # your code here!
    return (arr-arr.min())/(arr.max()-arr.min())

if __name__ == '__main__':
    # Test your code here!
    arr = np.array([0, 2, 4, 6, 8, 10])
    print(normalize(arr))
