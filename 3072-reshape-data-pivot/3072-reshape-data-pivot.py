import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    pvt_table=weather.pivot_table(index='month', columns='city', values='temperature')
    return pvt_table
    