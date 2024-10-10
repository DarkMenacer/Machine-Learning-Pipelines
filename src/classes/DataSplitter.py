'''

class Data Splitter
- Implements
    - Split dataset into training and testing set based on user provided ratio

- Parameters in the constructor
    - dataset: pd.DataFrame => The entire dataset

- Public methods
    - random_split: returns randomly split training and testing dataframes (without overlap) based on ratio provided in the argument
    - split_ratio: float => test-to-entire set ratio, i.e. 0.2 implies 20% test set and the rest is train set

- TODO
    - Look into validation set and epochs
    - Look into other ways of data splitting other than random split
    - Check inbuilt sklearn datasplit function as well

'''

import pandas as pd
import time

from utils.LogHandling import log_prog


class DataSplitterClass:

    def __init__(self, dataset: pd.DataFrame) -> None:
        self.__dataset: pd.DataFrame = dataset

    def random_split(self, split_ratio: float = 0.1, random_state: int = int(time.time())) -> tuple:
        log_prog('Enter DataSplitterClass.random_split')
        dataset = self.__dataset
        test_set = dataset.sample(frac = split_ratio, random_state = random_state)
        train_set = dataset.drop(test_set.index)
        log_prog('Exit DataSplitterClass.random_split')
        return train_set, test_set
