"""
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
"""

import datetime
import calendar
from sys import argv


def check_date(date: str) -> bool:
    format = '%d.%m.%Y'
    try:
        date = datetime.datetime.strptime(date, format)
        return True
    except:
        return False


def check_year(date: str) -> bool:
    year = int(date.split(".")[-1])
    return calendar.isleap(year)


if __name__ == '__main__':
    print('Valid value' if check_date(argv[1]) else 'Invalid value')
    if check_date(argv[1]) and check_year(argv[1]):
        print(f'{argv[1]} is a leap year')
    else:
        print(f'{argv[1]} is not a leap year')
