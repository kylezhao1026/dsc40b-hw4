def histogram(points, bins):
    """Efficiently computes a histogram.

    Assumes that both `points` and `bins` are sorted in ascending order to
    avoid looping through all bins for each point.

    """
    # TODO: Implement the histogram function
    n = len(points)
    k = len(bins)
    counts = [0] * k
    i = 0  
    j = 0  

    while i < n and j < k:
        x = points[i]
        a, b = bins[j]

        if x < a:
            i += 1
        elif x < b:   
            counts[j] += 1
            i += 1
        else:      
            j += 1


    total = float(n)
    densities = []
    for (a, b), c in zip(bins, counts):
        width = (b - a)
        densities.append(c /(total*width))

    return densities

# points = [1, 2, 3, 6, 7, 9, 10, 11]
# bins   = [(0, 4), (4, 8), (8, 12)]

# print(histogram(points, bins))
