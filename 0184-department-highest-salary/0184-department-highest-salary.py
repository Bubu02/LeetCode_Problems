import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(employee, department, left_on='departmentId', right_on='id', how='left', suffixes=('_emp','_dep'))
    df2 = employee.groupby('departmentId')['salary'].max().reset_index().rename(columns={'salary':'max_salary'})
    df3 = df.merge(df2, on='departmentId', how='left')
    return df3[df3['salary']==df3['max_salary']][['name_dep','name_emp','salary']].rename(columns={'name_dep':'Department', 'name_emp':'Employee','salary':'Salary'})
    