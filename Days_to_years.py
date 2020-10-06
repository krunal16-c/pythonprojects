# Converting days into years using python 3

WEEK_DAYS = 7

# deining a function to find year, week, days
def find(no_of_days):
    # assuming that year is of 365 days
    year = int(no_of_days/365)
    week = int((no_of_days%365)/WEEK_DAYS)
    days = (no_of_days%365)%WEEK_DAYS

    print("years",year,
          "\nWeeks",week,
          "\ndays", days)

# driver code
no_of_days = int(input("Enter number of days.\n"))
find(no_of_days)
