# Machine-Learning-Pipelines
## Perform end-to-end machine learning on any system capable of running Python

### Technologies used
	1. Python 3.9.6

### Purpose

All of (traditional statistical) machine learning follows a straight-forward pipeline regardless of for which domain it is being used in. The purpose of this repository is to generalise and parameterise those steps.\
All the gory details of machine learning can be abstracted from the user and information can be asked through parameters wherever necessary. 

### Progress Status

The repository currently supports:

```
- Reading data from .csv files
- One-hot encoding and binarisation of data
- Finding correlation between different features (and filtering based on it)
- Randomly split the data into Train and Test data sets
- Train and Test Classifiers models: K-Neighbors, Support Vector, Gaussian Naive Bayes, Decision Trees
- Determine Accuracy, Precision and Recall of the performance of the Classifier
```

GitHub issues for this repository include further plan to generalise the repository and truly become an one-stop solution for all of Machine learning models. Check them out [here](https://github.com/DarkMenacer/Machine-Learning-Pipelines/issues).

Further, I also plan to develop such a pipeline for Reinforcement learning and LLMs if time permits me to do so. 


### How to use (Steps)

	1. Update the parameters in src/run.py
	2. Execute run.py
	3. Rest of the things are handled by the many different classes present in the repository


---

### Log

    Created: 11 October 2024
    Last Edit: 11 October 2024
    
---
