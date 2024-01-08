import datetime
import calendar


def get_all_info():
    all_info = {
        "month_info": get_month_info(),
        "year_info": get_year_info()
    }
    return all_info


def get_now_info():
    return {"now": datetime.datetime.now()}


# gets how many days of current month left
# gets how many percents of month left to the end of the month
def get_month_info():
    today = datetime.date.today()
    _, days_in_month = calendar.monthrange(today.year, today.month)
    days_left = days_in_month - today.day

    days_passed = today.day
    percent_left = (days_in_month - days_passed) / days_in_month * 100

    return {
        "days_passed_in_current_month": today.day,
        "days_left_in_current_month": days_left,
        "percents_passed_in_current_month": round(100 - percent_left, 4),
        "percents_left_in_current_month": round(percent_left, 4)
    }


# gets how many days to the end of the year left
# gets how many percents of the year left to the end of the year
def get_year_info():
    today = datetime.date.today()
    end_of_year = datetime.date(today.year, 12, 31)
    days_left = (end_of_year - today).days

    end_of_year = datetime.date(today.year, 12, 31)
    days_passed = (today - datetime.date(today.year, 1, 1)).days
    percent_left = (days_passed / (end_of_year - datetime.date(today.year, 1, 1)).days) * 100

    return {
        "days_passed_in_current_year": days_passed + 1,
        "days_left_to_year_end": days_left - 1,
        "percents_passed_in_current_year": round((100 - percent_left), 4),
        "percents_left_in_year": round(percent_left, 4)
    }
