year = int(input())
def is_year_leap(year):
    if year % 4 == 0 and year % 400 == 0:
        print(year, "Год высокосный")
    else:
        print(year, "Год не высокосный")
is_year_leap(year)
        