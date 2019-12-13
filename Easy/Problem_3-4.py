"""
    n=1	n=2	n=3	n=4     n=5
    *	**	* *	*  *	*   *
        **	 * 	 **      * *
            * *	 **       *
                *  *	 * *
                        *   *
"""


def x_shape(n):
    i = 0
    j = n - 1
    for row in range(n):
        for col in range(n):
            if row == i and col == j:
                print("*", end="")
                i = i + 1
                j = j - 1
            elif row == col:
                print("*", end="")
            else:
                print(end=" ")
        print()


if __name__ == '__main__':
    n = 5
    pattern = x_shape(n)
    print(pattern)
