def swap_sum(A, B):
    """Swaps two elements in two sorted arrays to obtain a target sum 
    difference of 10.

    Assumes that both arrays are sorted in ascending order and only 
    contain integers.

    """
    # TODO: Implement the swap_sum function
    
    sumA = sum(A)
    sumB = sum(B)
    
    d_num = (sumA + 10) - sumB
    
    if d_num % 2 != 0:
        return None
    target = d_num // 2
    
    i, j = 0, 0
    nA, nB = len(A), len(B)

    while i < nA and j < nB:
        diff = A[i] - B[j]
        
        if diff == target:
            return (i, j)
        elif diff < target:
            i+=1
        else:
            j+=1

    return None


# A = [1, 6, 50]
# B = [4, 24, 35]
# print(swap_sum(A, B))
# A = [1, 2, 3]
# B = [10, 20, 30]
# print(swap_sum(A, B))
