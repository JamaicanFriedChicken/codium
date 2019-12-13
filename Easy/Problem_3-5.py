"""
n=1  n=2  n=3   n=4    n=5        n=9
*    *     *     *      *          *
     *    ***   ***    ***        ***
           *    ***   *****      *****
                 *     ***      *******
                        *      *********
                                *******
                                 *****
                                  ***
                                   *
Analysis:
n = 9
Row1: 4 spaces, 1 star, 4 spaces
Row2: 3 spaces, 3 stars, 3 spaces
Row3: 2 spaces, 5 stars, 2 spaces
Row4: 1 space, 7 stars, 1 space
Row5: 0 spaces, 9 stars, 0 spaces
Row6: 1 space, 7 stars, 1 space
Row7: 2 spaces, 5 stars, 2 spaces
Row8: 3 spaces, 3 stars, 3 spaces
Row9: 4 spaces, 1 star, 4 spaces

From row 1 to (n+1)/2, the number of spaces decreases as the number of stars increase.
So from 1 to 5, the # of stars = (row number * 2) - 1, while # of spaces before stars = 5 - row number.

Now from row (n+1)/2 + 1 to row 9, the number of spaces increase while the number of stars decrease.
So from 6 to n, the # of stars = ((n+1 - row number) * 2) - 1, while # of spaces before stars = row number - 5.
"""


def diamond_shape(rows):
    for i in range(1, (rows + 1) // 2 + 1):
        for j in range((rows + 1) // 2 - i):
            print(" ", end="")
        for k in range((i * 2) - 1):
            print("*", end="")
        print()

    for i in range((rows + 1) // 2 + 1, rows + 1):  # from row 6 to 9
        for j in range(i - (rows + 1) // 2):
            print(" ", end="")
        for k in range((rows + 1 - i) * 2 - 1):
            print("*", end="")
        print()


if __name__ == '__main__':
    rows = 9
    diamond_shape(rows)