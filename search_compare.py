import random
import time

def sequential_search(alist, item):
    start_time = time.time()
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1

    end_time = time.time()
    return found, end_time - start_time

def ordered_sequential_search(alist, item):
    start_time = time.time()
    pos = 0
    found = False
    stop = False

    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos + 1

    end_time = time.time()
    return found, end_time - start_time

def binary_search_iterative(alist, item):
    start_time = time.time()
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    end_time = time.time()
    return found, end_time - start_time

def binary_search_recursive(alist, item):
    start_time = time.time()
    
    def _binary_search_recursive(alist, item, first, last):
        if first > last:
            return False
        else:
            midpoint = (first + last) // 2
            if alist[midpoint] == item:
                return True
            else:
                if item < alist[midpoint]:
                    return _binary_search_recursive(alist, item, first, midpoint - 1)
                else:
                    return _binary_search_recursive(alist, item, midpoint + 1, last)
    
    found = _binary_search_recursive(alist, item, 0, len(alist) - 1)
    end_time = time.time()
    return found, end_time - start_time

def generate_random_lists(size, num_lists):
    return [[random.randint(1, 100000) for _ in range(size)] for _ in range(num_lists)]

def main():
    sizes = [500, 1000, 5000]
    num_lists = 100
    search_item = 99999999

    for size in sizes:
        lists = generate_random_lists(size, num_lists)
        
        seq_times = []
        ord_seq_times = []
        bin_iter_times = []
        bin_rec_times = []

        for alist in lists:
            _, time_taken = sequential_search(alist, search_item)
            seq_times.append(time_taken)

            alist.sort()
            _, time_taken = ordered_sequential_search(alist, search_item)
            ord_seq_times.append(time_taken)

            _, time_taken = binary_search_iterative(alist, search_item)
            bin_iter_times.append(time_taken)

            _, time_taken = binary_search_recursive(alist, search_item)
            bin_rec_times.append(time_taken)

        print(f"Sequential Search took {sum(seq_times) / num_lists:10.7f} seconds to run, on average for list size {size}")
        print(f"Ordered Sequential Search took {sum(ord_seq_times) / num_lists:10.7f} seconds to run, on average for list size {size}")
        print(f"Binary Search Iterative took {sum(bin_iter_times) / num_lists:10.7f} seconds to run, on average for list size {size}")
        print(f"Binary Search Recursive took {sum(bin_rec_times) / num_lists:10.7f} seconds to run, on average for list size {size}")

if __name__ == "__main__":
    main()
