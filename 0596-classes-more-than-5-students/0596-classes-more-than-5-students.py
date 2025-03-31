import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df= courses["class"].value_counts().reset_index()
    a=df[df["count"]>=5][["class"]]
    return a