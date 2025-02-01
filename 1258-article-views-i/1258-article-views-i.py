import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    bc_author=views[views['author_id']==views['viewer_id']][['author_id']]
    bc_author=bc_author.rename(columns={'author_id':'id'})
    distinct_bc_author=bc_author[['id']].drop_duplicates()
    sorted_bc = distinct_bc_author.sort_values(by='id', ascending=True)
    return sorted_bc
    