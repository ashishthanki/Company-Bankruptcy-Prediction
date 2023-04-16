"""Main module."""
from pathlib import Path

from data.make_dataset import load_data
from features.transformations import clean_data, split_data


def main():
    dataset_path = Path().absolute() / "data/raw/data.csv"
    # load data
    raw_data = load_data(dataset_path)

    # explore data - see Jupyter Notebooks in notebooks folder.
    # clean data names
    cleaned = clean_data(raw_data)

    # create train test validation splits
    train_set, valid_set, test_set = split_data(cleaned)

    # transform data

    # preprocess data and prepare for modelling

    # build models and shortlist best

    # run hyperparameter optimizer

    # fit model again with best_config
    
    # evaluate model

    # visual best features with Synergy
    return train_set, valid_set, test_set


if __name__ == "__main__":
    main()