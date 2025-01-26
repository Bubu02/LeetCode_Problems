import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customer_unique=customers.drop_duplicates(subset=['email'])
    return customer_unique    