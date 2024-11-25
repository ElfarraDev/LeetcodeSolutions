def fixed_window(arr, k):
    # Initialize pointers and variables
    low = 0
    high = 0
    window_size = k
    n = len(arr)
    result = []  # or any other variable to store results
    window_sum = 0  # or any other variable to track window state
    # Continue until we reach end of array
    while high < n:
        # Step 1: Create window that's one element smaller than desired size
        if high - low + 1 < window_size:
            # Add current element to window state
            window_sum += arr[high]
            # Generate window by increasing high index
            high += 1
        # Step 2: Process the window
        else:
            # Window size is now equal to desired window size
            # Step 2a: Calculate answer based on elements in window
            window_sum += arr[high]  # Add the last element to complete window
            result.append(window_sum)  # or any other result calculation
            # Step 2b: Remove oldest element from window
            window_sum -= arr[low]
            # Proceed to next window by incrementing both pointers
            low += 1
            high += 1
    return result

# Example usage:
def main():
    # Example: Finding sum of all windows of size k
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    sums = fixed_window(arr, k)
    print(f"All window sums of size {k}: {sums}")
    # Output: All window sums of size 3: [6, 9, 12, 15, 18]

if __name__ == "__main__":
    main()
