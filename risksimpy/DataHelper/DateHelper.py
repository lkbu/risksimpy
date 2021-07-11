DaysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def GetDaysInMonth(i = int):
    if (i<1 || i>12):
        ValueError("Invalid parameter supplied to GetDaysInMonth should be 1 to 12.")
    return DaysInMonth[i]

def IsLeapYear(year = int):
    return (((year % 4) == 0) && ((year % 100) != 0)) || ((year % 400) == 0)

#TODO
def IsBusinessDay(date):
    pass