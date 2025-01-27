import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    heavy_animal=animals[
        animals['weight']>100
    ].sort_values(
        'weight', ascending=False
    )[['name']]
    return heavy_animal
    