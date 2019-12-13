"""
n=3    n=4      n=6
  *      *        *
 **     **       **
***    ***      ***
      ****     ****
              *****
             ******
"""


def inverse_triangle(n):
    for i in range(1, n+1):
        print(" " * n, end="")
        print("*" * i)
        n -= 1


if __name__ == '__main__':
    num = 6
    pattern = inverse_triangle(num)
    print(pattern)