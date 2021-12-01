import json

import datetime
from datetime import date

class Day():
    def __init__(self, day):
        self.day = day

    def __str__(self):
        return f'{self.day}'

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        if not isinstance(day, int):
            raise TypeError('Must be integer type')
        if day <= 0:
            raise ValueError('Days must be > 0')

        self.__day = day


class Month():
    def __init__(self, month):
        self.month = month

    def __str__(self):
        return f'{self.month}'

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month):
        if not isinstance(month, int):
            raise TypeError('Must be integer type')
        if month <= 0:
            raise ValueError('Month must be > 0')

        self.__month = month


class Year():
    def __init__(self, year):
        self.year = year

    def __str__(self):
        return f'{self.year}'

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise TypeError('Must be integer type')
        if year <= 0:
            raise ValueError('Year must be > 0')

        self.__year = year


class Calendar:
    today = date.today()

    def __init__(self, day=today.day, month=today.month, year=today.year):
        self.__day = day
        self.__month = month
        self.__year = year

    def __str__(self):
        return f'year-month-day: {self.year}-{self.month}-{self.day}'

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        if not isinstance(day, int):
            raise TypeError('Must be integer type')
        if not 0 < day <= 31:
            raise ValueError('Must be: 0 < day <= 31')

        self.__day = day

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month):
        if not isinstance(month, int):
            raise TypeError('Must be integer type')
        if not 0 < month <= 12:
            raise ValueError('Must be: 0 < month <= 12')

        self.__month = month

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise TypeError('Must be integer type')
        if year <= 0:
            raise ValueError('Must be: year > 0')

        self.__year = year

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        # if not isinstance(date, datetime.date):
        #     raise TypeError('Must be datetime type')
        # if date <= 0:
        #     raise ValueError('Must be: year > 0')

        self.__date = date

    # арифметичні операції
    # +=
    def __iadd__(self, other):
        with open('C:/MinGW/bin/cpp/Python/4/1/month.json') as month:
            data_of_month = json.load(month)

        if not isinstance(other, (Day, Month, Year)):
            raise TypeError('Invalid input data type')

        if self.is_leap_year():
            data_of_month['2']['days'] = 29

        if isinstance(other, Day):
            self.add_days(other, data_of_month)
            return Calendar(self.day, self.month, self.year)
        elif isinstance(other, Month):
            self.add_month(other, data_of_month)
            return Calendar(self.day, self.month, self.year)
        elif isinstance(other, Year):
            self.year += other.year
            return Calendar(self.day, self.month, self.year)

    def add_days(self, other, data_of_month):
        change_days = other.day
        while change_days > 0:
            if self.day + 1 <= data_of_month[str(self.month)]['days']:
                self.day += 1
                change_days -= 1
            else:
                if self.month + 1 <= 12:
                    self.month += 1
                    self.day = 1
                    change_days -= 1
                else:
                    self.year += 1
                    if self.is_leap_year():
                        data_of_month['2']['days'] = 29
                    else:
                        data_of_month['2']['days'] = 28
                    self.day = 1
                    self.month = 1
                    change_days -= 1

    def add_month(self, other, data_of_month):
        change_month = other.month
        while change_month > 0:
            if self.month + 1 <= 12:
                self.month += 1
                change_month -= 1
            else:
                self.year += 1
                self.month = 1
                change_month -= 1

    # +=
    def __isub__(self, other):
        with open('C:/MinGW/bin/cpp/Python/4/1/month.json') as month:
            data_of_month = json.load(month)

        if not isinstance(other, (Day, Month, Year)):
            raise TypeError('Invalid input data type')

        if self.is_leap_year():
            data_of_month['2']['days'] = 29

        if isinstance(other, Day):
            self.sub_days(other, data_of_month)
            return Calendar(self.day, self.month, self.year)
        elif isinstance(other, Month):
            self.sub_month(other, data_of_month)
            return Calendar(self.day, self.month, self.year)
        elif isinstance(other, Year):
            self.year -= other.year
            return Calendar(self.day, self.month, self.year)

    def sub_days(self, other, data_of_month):
        change_days = other.day
        while change_days > 0:
            if self.day - 1 > 0:
                self.day -= 1
                change_days -= 1
            else:
                if self.month - 1 > 0:
                    self.month -= 1
                    if self.is_leap_year():
                        data_of_month['2']['days'] = 29
                    else:
                        data_of_month['2']['days'] = 28
                    self.day = data_of_month[str(self.month)]['days']
                    change_days -= 1
                else:
                    self.year -= 1
                    self.month = 12
                    if self.is_leap_year():
                        data_of_month['2']['days'] = 29
                    else:
                        data_of_month['2']['days'] = 28
                    self.day = data_of_month[str(self.month)]['days']
                    change_days -= 1

    def sub_month(self, other, data_of_month):
        change_month = other.month
        while change_month > 0:
            if self.month - 1 > 0:
                self.month -= 1
                change_month -= 1
            else:
                self.year -= 1
                self.month = 12
                change_month -= 1

    def is_leap_year(self):
        if not self.year % 4 and self.year % 100 or not self.year % 400:
            return True
        else:
            return False

    # оператори порівняння
    # ==
    def __eq__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError('Invalid input data type')
        if self.year == other.year and self.month == other.month and self.day == other.day:
            return True
        return False

    # !=
    def __ne__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError('Invalid input data type')
        if self.year != other.year or self.month != other.month or self.day != other.day:
            return True
        return False

    # >
    def __gt__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError('Invalid input data type')
        if self.year > other.year:
            return True
        if self.year == other.year:
            if self.month > other.month:
                return True
            if self.month == other.month:
                if self.day > other.day:
                    return True
        return False

    # >=
    def __ge__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError('Invalid input data type')
        if self.year > other.year:
            return True
        if self.year == other.year:
            if self.month > other.month:
                return True
            if self.month == other.month:
                if self.day >= other.day:
                    return True
        return False
    
    # <
    def __lt__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError('Invalid input data type')
        if self.year < other.year:
            return True
        if self.year == other.year:
            if self.month < other.month:
                return True
            if self.month == other.month:
                if self.day < other.day:
                    return True
        return False

    # <=
    def __le__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError('Invalid input data type')
        if self.year < other.year:
            return True
        if self.year == other.year:
            if self.month < other.month:
                return True
            if self.month == other.month:
                if self.day <= other.day:
                    return True
        return False

date1 = Calendar()
print(date1)

day = Day(1000)
month = Month(5)
year = Year(10)

date1 += day
print(date1)
date1 += month
print(date1)
date1 += year
print(date1)

print()

date2 = Calendar(1, 1, 2032)
print(date2)

date2 -= day
print(date2)
date2 -= month
print(date2)
date2 -= year
print(date2)

print(f'{date1} < {date2}: {date1 < date2}')
print(f'{date1} <= {date2}: {date1 <= date2}')
print(f'{date1} > {date2}: {date1 > date2}')
print(f'{date1} >= {date2}: {date1 >= date2}')
print(f'{date1} == {date2}: {date1 == date2}')
print(f'{date1} != {date2}: {date1 != date2}')