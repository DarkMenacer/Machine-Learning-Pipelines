'''

Class Pipeline Runner
- Implements
    - Run Classification Pipeline (Wrangling, Exploring, Spltting, Classifying)

- Parameters in the constructor
    - file_path: str => Absolute path of the file containing the data (currently only .csv supported)
    - target_column_name: str => Name of the target column in the dataset
    - classifer_name: str => Name of the classifier to be used for classification
    - cols_to_hot_encode: list[str] => Names of the attributes which are in string and need to be converted into 0/1, i.e. one hot encoded (pass None if no such column)
    - yn_tf_cols: list[str] => Names of the columns which contains values in the form of yes/no/true/false and need to be converted to binary (pass None if no such column)
    - minimum_correlation_threshold: float = Takes input the minimum correlation value for the feature to be used for training the model. Must be between 0 and 1
    - columns_to_remove_pre_processing: list[str] => List of column names to remove before training the model (like id, name...). Pass None if no such column
    - split_ratio: float => The split ratio of train and test. 0.2 implies 20% test and 80% train
    - iterations: int => Number of times a new data split has to be generated and model to be trained and evaluated over the new split

- Public Methods
    - run_classification_pipeline
        - kwargs
            - k: int => K of the KNeighborsClassifier in case of KNN classifier

- TODO
    - Setup DataClusterer Class
    - Setup Reinforcement Learner
    - Setup whatever LLMs are

'''

from typing import Union
from classes.DataClassifier import DataClassifierClass
from classes.DataExplorer import DataExplorerClass
from classes.DataSplitter import DataSplitterClass
from classes.DataWrangler import DataWranglerClass
from utils.LogHandling import log_val


class PipelineRunnerClass:

    def __init__(
        self,
        file_path: str,
        target_column_name: str,
        classifier_name: str,
        split_ratio: float,
        iterations: int,
        columns_to_hot_encode: Union[list[str], None] = None,
        yn_tf_columns: Union[list[str], None] = None,
        minimum_correlation_threshold: float = 0,
        columns_to_remove_right_before_classification: Union[list[str], None] = None
    ) -> None:
        # Dataset settings
        self.__file_path = file_path
        self.__columns_to_hot_encode = columns_to_hot_encode
        self.__yn_tf_columns = yn_tf_columns
        self.__target_column_name = target_column_name
        self.__columns_to_remove_right_before_classification = columns_to_remove_right_before_classification

        # Parameter settings
        self.__minimum_correlation_threshold = minimum_correlation_threshold
        self.__split_ratio = split_ratio
        self.__classifier_name = classifier_name
        self.__iterations = iterations

    def run_classification_pipeline(self, **kwargs):

        sep = kwargs.get('sep', ';')

        # Data Wrangling
        dataset = DataWranglerClass(self.__file_path, cols_to_hot_encode = self.__columns_to_hot_encode, yn_tf_cols = self.__yn_tf_columns, sep = sep)
        df = dataset.get_processed_dataframe()

        # Data Exploring
        data_explorer = DataExplorerClass(df, target_column_name = self.__target_column_name)
        log_val(data_explorer.correlation_values_dataframe())
        log_val(data_explorer.trim_columns_with_correlation_less_than(min_correlation = self.__minimum_correlation_threshold))

        for _ in range(self.__iterations):

            evaluation_dataFrame_row = {}

            # Data Splitting here
            train_set, test_set = DataSplitterClass(df).random_split(self.__split_ratio)

            # Data Classifying
            clf = DataClassifierClass(train_set, test_set, target_column_name = self.__target_column_name, columns_to_remove_pre_processing = self.__columns_to_remove_right_before_classification)
            clf.evaluate_using_model(classifer_name = self.__classifier_name)
            log_val(clf.predicted_target_appended_test_set())
            log_val(clf.performance_metrics())
            log_val(clf.performance_through_confusion_matrix())
            evaluation_dataFrame_row.update(clf.performance_metrics())
