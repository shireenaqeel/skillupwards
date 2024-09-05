def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
def main():
    n_terms = 10  # You can change this to generate more or fewer terms
    print(f"Fibonacci sequence up to {n_terms} terms (recursive):")
    for i in range(n_terms):
        print(fibonacci_recursive(i), end=" ")
    print()  # For a new line after the sequence

if __name__ == "__main__":
    main()
