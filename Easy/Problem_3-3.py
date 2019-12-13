"""
n=1    n=2      n=3    	  n=4       n=5
*       *        *         *         *
       * *      * * 	  * *       * *
               *   *	 *   *     *   *
                        *     *   *     *
                                 *       *

"""


def cone(n):
    for row in range(1, n + 1):
        for col in range(1, 2 * n):
            if (row + col == n + 1) or (col - row == n - 1):
                print("*", end="")
            else:
                print(end=" ")
        print()


if __name__ == '__main__':
    n = 5
    pattern = cone(n)
    print(pattern)