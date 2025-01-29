import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    best_food = products[(products['low_fats']=='Y') & (products['recyclable']=='Y')][
        ['product_id']
    ]
    return best_food
    