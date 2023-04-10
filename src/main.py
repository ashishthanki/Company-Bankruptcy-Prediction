"""Main module."""
from data.make_dataset import load_data


def main(path: str = "data/raw/data.csv"):
    # load data
    raw_data = load_data(path)

    # create train test validation splits

    # transform data

    # explore data - see Jupyter Notebooks in notebooks folder.

    # preprocess data and prepare for modelling

    # build models and shortlist best

    # run hyperparameter optimizer

    # fit model again with best_config
    
    # evaluate model

    # visual best features with Synergy
    return raw_data


if __name__ == "__main__":
    main()