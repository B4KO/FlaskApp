from datetime import datetime, timedelta

def gen_datetime(min_year=1900, max_year=datetime.now().year):
    
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()