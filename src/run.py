from classes.PipelineRunner import PipelineRunnerClass
import warnings
from sklearn.exceptions import UndefinedMetricWarning

warnings.filterwarnings("ignore", category = UndefinedMetricWarning)


def all_functions(name: str) -> int:
    # print('Import all functions to this file and run only this file: ', end = '')
    # print(name)

    # Dataset settings: https://archive.ics.uci.edu/dataset/320/student+performance
    file_path = '<abs-path>/Machine-Learning-Pipelines/data/student-mat.csv'
    columns_to_hot_encode = ['school', 'sex', 'address', 'famsize', 'Pstatus', 'Mjob', 'Fjob', 'reason', 'guardian']
    yn_tf_columns = ['schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic']
    target_column_name = 'G3'
    columns_to_remove_right_before_classification = ['G1', 'G2']

    # Parameter settings
    minimum_correlation_threshold = 0.1
    classifier_name = 'SVC'
    split_ratio = 0.25
    iterations = 100

    pf = PipelineRunnerClass(
        file_path = file_path,
        columns_to_hot_encode = columns_to_hot_encode,
        yn_tf_columns = yn_tf_columns,
        target_column_name = target_column_name,
        minimum_correlation_threshold = minimum_correlation_threshold,
        columns_to_remove_right_before_classification = columns_to_remove_right_before_classification,
        classifier_name = classifier_name,
        split_ratio = split_ratio,
        iterations = iterations,
    )
    pf.run_classification_pipeline()
    return 1


if __name__ == "__main__":
    all_functions('run.py')

