import time
import random

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []
    
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
    
    return quick_sort(left) + middle + quick_sort(right)


# Quick Sort - modified
def quick_sort_mod(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = []
    middle = []
    right = []
    
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
    
    return quick_sort_mod(left) + middle + quick_sort_mod(right)

# Function to generate test lists
def generate_lists(size):
    """Generates a random and sorted list of given size"""
    random_list = [random.randint(1, 10001) for _ in range(size)]
    sorted_list = sorted(random_list)  # Already sorted version
    return random_list, sorted_list

# Function to measure execution time
def measure_time(sort_function, arr):
    """Measures execution time of sorting function in seconds"""
    start_time = time.perf_counter()
    sort_function(arr)  # Sorting in-place (for selection sort)
    end_time = time.perf_counter()
    
    return end_time - start_time  # elapsed time in seconds

# Main Execution
if __name__ == "__main__":
    size = 1000

    # Generate test lists
    rand_list, sorted_list = generate_lists(size)

    # Measure Selection Sort on Random List
    rand_list_copy = rand_list[:]
    time_selection_rand = measure_time(selection_sort, rand_list_copy)

    # Measure Selection Sort on Sorted List
    sorted_list_copy = sorted_list[:]
    time_selection_sorted = measure_time(selection_sort, sorted_list_copy)

    # Measure Quick Sort on Random List
    rand_list_copy = rand_list[:]  # Copy to avoid modifying the original
    time_quick_rand = measure_time(quick_sort, rand_list_copy)

    # Measure Quick Sort on Sorted List
    sorted_list_copy = sorted_list[:]
    time_quick_sorted = measure_time(quick_sort, sorted_list_copy)

    # Measure Quick Sort - modified on Random List
    rand_list_copy = rand_list[:]
    time_quick_mod_rand = measure_time(quick_sort_mod, rand_list_copy)

    # Measure Quick Sort - modified on Sorted List
    sorted_list_copy = sorted_list[:]   
    time_quick_mod_sorted = measure_time(quick_sort_mod, sorted_list_copy)

    # Display results
    print("\nExecution Time Results (in seconds):")
    print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(
        "Size", "SelSort Random", "SelSort Sorted", "QuickSort Random", "QuickSort Sorted", "QuickSort-mod Random", "QuickSort-mod Sorted"))

    print(f"{size:<10} {time_selection_rand:<20.6f} {time_selection_sorted:<20.6f} "
          f"{time_quick_rand:<20.6f} {time_quick_sorted:<20.6f} {time_quick_mod_rand:<20.6f} {time_quick_mod_sorted:<20.6f}")

