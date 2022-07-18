import pandas as pd


def add_records(olympics):
    new_olympics = {2021: 'Tokyo', 2024: 'Paris', 2028: 'Los Angeles'}
    return olympics.append(pd.Series(new_olympics))
