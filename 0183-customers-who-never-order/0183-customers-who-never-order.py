import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    bc_customer = customers[~customers['id'].isin(orders['customerId'])]
    bc_customer = bc_customer[['name']].rename(columns={'name':'Customers'})
    return bc_customer
    