"""
n=3   n=4    n=6
*     *      *
**    **     **
***   ***    ***
      ****   ****
             *****
             ******
"""

def number_triangle(n):
    for i in range(1, n+1):
        for j in range(i):
            print("*", end="")
        print()
    print("")


if __name__ == '__main__':
    n = 6
    pattern = number_triangle(n)
    print(pattern)

