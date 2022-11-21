# Python datetime module makes this easy.
import datetime


def main():
    # Define and
    start = datetime.datetime(1901, 1, 1)
    end = datetime.datetime(2000, 12, 31)
    count = 0
    while start <= end:
        day = start.weekday()
        if day == 6 and start.day == 1:
            count += 1
        start += datetime.timedelta(1)
    return count


print(main())