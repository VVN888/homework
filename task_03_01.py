def get_days_to_new_year():
    import datetime
    now_date = datetime.date.today()
    current_year = now_date.year
    i = current_year + 1
    then_date = datetime.date(i,1,1)
    delta_date = then_date - now_date
    x_days = delta_date.days
    return x_days
