# utilities to help with date and time manipulation
import numpy as np

# create weeks range number
import datetime
from datetime import date
def weeks_for_year(year):
    # returns the number of weeks for the year
    last_week = date(year, 12, 28)
    return last_week.isocalendar()[1]

def week_start_date(week_number, year):
    # returns a datetime.datetime of the Monday for specific week number & given year 
    d = f'{year}-W{week_number}'
    return datetime.datetime.strptime(d + '-1', "%Y-W%W-%w")

def week_end_date(week_number, year):
    # returns a datetime.datetime of the Friday for specific week number & given year
    d = f'{year}-W{week_number}'
    return week_start_date(week_number, year) + datetime.timedelta(days = 4)

# create all start day dates for a year
def week_start_dates(year):
    # returns a list of trading week start dates string
    # e.g. ['2022-12-22', ...]
    week_numbers = np.arange(1,(weeks_for_year(2022)+1)) # gets the number
    week_start_dates = []
    for i in week_numbers:
        item = week_start_date(i, year).strftime('%Y-%m-%d') # string for start date
        week_start_dates.append(item)
    return week_start_dates

def week_end_dates(year):
    # returns a list of trading week end dates string
    # e.g. ['2022-12-26', ...]
    week_numbers = np.arange(1,(weeks_for_year(2022)+1)) # gets the number
    week_end_dates = []
    for i in week_numbers:
        item = week_end_date(i, year).strftime('%Y-%m-%d') # string for start date
        week_end_dates.append(item)
    return week_end_dates

def main():
    print(weeks_for_year(2023))
main()