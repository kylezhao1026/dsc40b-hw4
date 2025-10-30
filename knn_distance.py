import random

def knn_distance(arr, q, k):
    
    pairs = [(abs(x - q), x) for x in arr]
    idx = k - 1

    def quickselect(a, left, right, idx):
        while True:
            if left == right:
                return a[left]

            pivot_index = random.randint(left, right)
            pivot_dist = a[pivot_index][0]

            a[pivot_index], a[right] = a[right], a[pivot_index]

            lt = left
            eq = left
            gt = right

            while eq <= gt:
                if a[eq][0] < pivot_dist:
                    a[lt], a[eq] = a[eq], a[lt]
                    lt += 1
                    eq += 1
                elif a[eq][0] > pivot_dist:
                    a[eq], a[gt] = a[gt], a[eq]
                    gt -= 1
                else:
                    eq += 1

            if idx < lt:
                right = lt - 1
            elif idx > gt:
                left = gt + 1
            else:
                return a[idx]

    kth_pair = quickselect(pairs, 0, len(pairs) - 1, idx)
    
    return kth_pair
