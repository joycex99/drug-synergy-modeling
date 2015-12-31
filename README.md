# Modeling Drug Synergy
This repository holds the code for a machine learning-based model for predicting synergistic drug behaviors on cancer cell lines. 
The ML is largely performed on top of the [scikit-learn](http://scikit-learn.org/stable/) library, with additional work done in [numpy](http://www.numpy.org/)/[scipy](http://www.scipy.org/)/[pandas](http://pandas.pydata.org/). 
Each IPython Notebook holds a different version of the model and/or a major step in data manipulation or feature engineering. 
Research is still in process.

Several key components include:
  * Cross-validation of several different regressors and classifiers, including random forest, adaboost, gradient boosting, and svms.
  * Drug-drug mapping through shared targets
  * Construction of a PPI (protein-protein interaction) network and implementation of a path-searching algorithm to map target interactions to drug interactions
  * Implementation of a genetic algorithm to perform parameter tuning and feature selection 
  
The model currently achieves ~0.63 average pearson correlation for regression, and a 0.72 average classification accuracy of synergistic vs. non-synergistic 
compound/compound/cell line combinations (0.67 AUC, 0.79 F1).
