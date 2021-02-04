import numpy as np

def greater_than_mean(arr):
    '''
    Takes an array of numbers and returns
    only the values in that array which are
    greater than the mean.

    Example:

        arr = np.array([0,1,2,3,4,5])
        greater_than_mean(arr)

    Would return:

        np.array([3,4,5])
    '''
    # your code here!
    return arr[arr > arr.mean()]

if __name__ == '__main__':
    # Test your code here!
    arr = np.array([0,1,2,3,4,5])
    print(greater_than_mean(arr))
