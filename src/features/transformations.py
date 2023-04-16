"All Transformations in a single file."
import pandas as pd
from sklearn.model_selection import train_test_split


def clean_data(raw_data: pd.DataFrame) -> pd.DataFrame:
    transformed_data = raw_data.copy()

    # rename all columns. Remove spaces and ?.
    transformed_data.columns = transformed_data.columns.str.strip("? ")

    return transformed_data


def split_data(data: pd.DataFrame) -> tuple(
        pd.DataFrame, pd.DataFrame, pd.DataFrame):
    train_set, val_test_set = train_test_split(data, random_state=42, test_size=0.4)
    valid_set, test_set = train_test_split(val_test_set, random_state=42, test_size=0.2)
    return train_set, valid_set, test_set
