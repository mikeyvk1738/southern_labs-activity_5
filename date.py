#AUTHOR : VUSI 

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def get_month_code(month):
    if month == 1:
        return 1
    elif month == 2:
        return 4
    elif month == 3:
        return 4
    elif month == 4:
        return 0
    elif month == 5:
        return 2
    elif month == 6:
        return 5
    elif month == 7:
        return 0
    elif month == 8:
        return 3
    elif month == 9:
        return 6
    elif month == 10:
        return 1
    elif month == 11:
        return 4
    else:
        return 6


def get_day_of_the_week(month, day, year):
    yy = year % 100
    twelves = yy // 12
    remainder = yy % 12
    fours = remainder // 4

    month_code = get_month_code(month)

    # Special offsets
    if (month == 1 or month == 2) and is_leap_year(year):
        month_code += 6

    century = year // 100
    if century == 16:
        month_code += 6
    elif century == 17:
        month_code += 4
    elif century == 18:
        month_code += 2
    elif century == 20:
        month_code += 6
    elif century == 21:
        month_code += 4

    total = twelves + remainder + fours + day + month_code
    result = total % 7

    if result == 0:
        return "Saturday"
    elif result == 1:
        return "Sunday"
    elif result == 2:
        return "Monday"
    elif result == 3:
        return "Tuesday"
    elif result == 4:
        return "Wednesday"
    elif result == 5:
        return "Thursday"
    else:
        return "Friday"


def main():
    # Required tests
    print("Sunday" == get_day_of_the_week(12, 25, 2022))
    print("Friday" == get_day_of_the_week(8, 26, 2022))
    print("Thursday" == get_day_of_the_week(10, 5, 1972))
    print("Wednesday" == get_day_of_the_week(2, 3, 2016))
    print("Monday" == get_day_of_the_week(12, 18, 1899))

    # Interactive loop
    while True:
        month = int(input("\nMonth (1-12), or 0 to quit: "))
        if month == 0:
            break
        while month < 1 or month > 12:
            month = int(input("Invalid. Month (1-12): "))

        day = int(input("Day (1-31): "))
        while day < 1 or day > 31:
            day = int(input("Invalid. Day (1-31): "))

        year = int(input("Year: "))

        print(f"{month}/{day}/{year} is a {get_day_of_the_week(month, day, year)}")


if __name__ == "__main__":
    main()
