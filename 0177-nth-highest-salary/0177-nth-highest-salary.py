import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee['rank'] = employee['salary'].rank(method='dense', ascending=False)
    nthighest = employee[employee['rank'] ==N]
    return pd.DataFrame({f'getNthHighestSalary({N})':[None if len(nthighest) == 0 else nthighest['salary'].iloc[0]]})