def is_prime_recursive(n, divisor=None):
    if divisor is None:
        divisor = n - 1

    if n <= 1:
        return "Not Prime"
    if divisor == 1:
        return "Prime"
    if n % divisor == 0:
        return "Not Prime"
    return is_prime_recursive(n, divisor - 1)


num = int(input("Enter a number: "))
result = is_prime_recursive(num)
print(f"{num} is {result}.")
