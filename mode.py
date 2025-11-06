from typing import Iterable, Any

def mode(numbers):
   
    counts = {}
    best_item = None
    best_count = 0
    seen_any = False

    for x in numbers:
        seen_any = True
        c = counts.get(x, 0) + 1
        counts[x] = c
        if c > best_count:
            best_count = c
            best_item = x

    if not seen_any:
        raise ValueError("mode() arg is an empty iterable")

    return best_item
