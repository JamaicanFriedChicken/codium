"""
Write a program that finds all prime numbers up to n for input n. Example Output:
20 -> 2 3 5 7 11 13 17 19
"""


def sieve(n):

    # Creates a boolean array of prime_number[0...n] and initializes all entries to be True.
    prime_number = [True for i in range(n+1)]

    p = 2
    while(p * p <= n):

        # if prime_number[p] has not changed then it is a prime number
        if (prime_number[p] == True):
            # Updates all multiples of p
            for i in range(p * 2, n + 1, p):
                prime_number[i] = False
        p += 1
    number = []

    # Stores all prime numbers in the array number
    for p in range(2, n):
        if prime_number[p]:
            number.append(p)
    return number


# Change the variable num to an integer of your choice.
num = 20
list_of_numbers = sieve(num)
print(str(num) + " -> " + str(list_of_numbers)[1:-1])
