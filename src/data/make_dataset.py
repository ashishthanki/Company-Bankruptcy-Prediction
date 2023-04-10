"File to create a pandas DataFrame from raw data file."
from pathlib import Path

import pandas as pd


def load_data(file: str = "data/raw/data.csv") -> pd.DataFrame:
    """Loads raw company bankruptcy data.

    Args:
        file (str, optional): Path to raw data file. Defaults to "data/raw/data.csv".

    Raises:
        FileNotFoundError: Raises error if file not found in directory. Pull data from kaggle site.

    Returns:
        pd.DataFrame: DataFrame object of company bankruptcy data.
    """
    # raise error if file does not exist
    if not Path(file).exists():
        raise FileNotFoundError
    return pd.read_csv(Path(file))
