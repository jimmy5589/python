def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here 
    if len(aDict)==0:
        return None
    imax=0
    vmax=0
    for i, v in aDict.items():
        if len(v) >= vmax:
           vmax=len(v)
           imax=i
    return imax
