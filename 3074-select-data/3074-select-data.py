import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    students_row=students.loc[students['student_id'] == 101, ['name','age']]
    return students_row   