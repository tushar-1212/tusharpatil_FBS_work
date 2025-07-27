def recursive_sum(n):
    #sum of 0 is 0
    if n == 0:
        return 0
    # add current number to sum of previous numbers
    else:
        return n + recursive_sum(n - 1)

n = int(input("Enter a positive integer: "))
if n < 0:
    print("Please enter a non-negative number.")
else:
    result = recursive_sum(n)
    print(f"Sum of first {n} numbers is: {result}")