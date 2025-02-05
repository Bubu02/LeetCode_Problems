import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # Define a regex pattern for a valid email format
    email_pattern = r'^[a-zA-Z][a-zA-Z0-9._-]*@leetcode\.com$'

    # Filter the DataFrame to get rows with valid email addresses
    users = users[users['mail'].str.contains(email_pattern, regex=True)]


    return users