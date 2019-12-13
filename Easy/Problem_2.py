"""
Write a program that determine whether or not an integer input is a leap year.
Definition of leap year:
    Rule 1: A year is called leap year if it is divisible by 400.
    Example: 1600, 2000 etc. are leap year while 1500, 1700 are not leap year.

    Rule 2: If year is not divisible by 400 as well as 100 but it is divisible by 4 then that year are also leap year.
    Example: 2004, 2008, 1012 are leap year.

Example Output:
1600 -> true
2000 -> true
1500 -> false
2004 -> true
2008 -> true
2010 -> false
"""


def check_leap_year(year):
    if year % 400 == 0:
        print(str(year) + " -> " + "true")
    elif year % 4 == 0 and year % 400 != 0 and year % 100 != 0:
        print(str(year) + " -> " + "true")
    else:
        print(str(year) + " -> " + "false")


if __name__ == '__main__':
    year = int(input("Enter a year to check if it's a leap year:"))
    check_leap_year(year)