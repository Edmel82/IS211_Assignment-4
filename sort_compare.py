import time
import random

def insertion_sort(arr):
    start_time = time.time()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    end_time = time.time()
    return end_time - start_time

def shell_sort(arr):
    start_time = time.time()
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    end_time = time.time()
    return end_time - start_time

def python_sort(arr):
    start_time = time.time()
    arr.sort()
    end_time = time.time()
    return end_time - start_time

def main():
    sizes = [500, 1000, 5000]
    for size in sizes:
        arr = [random.randint(0, 10000) for _ in range(size)]
        
        arr_copy = arr.copy()
        insertion_time = insertion_sort(arr_copy)
        print(f"Insertion Sort for size {size}: {insertion_time:.6f} seconds")
        
        arr_copy = arr.copy()
        shell_time = shell_sort(arr_copy)
        print(f"Shell Sort for size {size}: {shell_time:.6f} seconds")
        
        arr_copy = arr.copy()
        python_time = python_sort(arr_copy)
        print(f"Python Sort for size {size}: {python_time:.6f} seconds")

if __name__ == "__main__":
    main()
