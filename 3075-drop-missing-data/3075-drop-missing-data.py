import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    unique_names=students.dropna(subset=['name'])
    return unique_names
    