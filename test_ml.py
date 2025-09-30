import pytest
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
# TODO: add necessary import
from ml.model import train_model, compute_model_metrics, inference
# TODO: implement the first test. Change the function name and input as needed
def test_train_model():
    """
    Test that train_model returns a RandomForestClassifier
    """
    # Create Sample Data
    X_train = np.random.rand(100, 10)
    y_train = np.random.randint(0, 2, 100)
    # train model 
    model = train_model(X_train, y_train)
    #Check that it returns RCF
    assert isinstance(model, RandomForestClassifier)


# TODO: implement the second test. Change the function name and input as needed
def test_calculate_model_metrics():
    """
    Test that compute_model_metrics returns correct values
    """
    # create sample true and predicted values
    y_true = np.array([1, 0, 1, 1, 0, 1, 0, 0])
    y_pred = np.array([1, 0, 1, 1, 0, 1, 0, 0])
    # calculate metrics
    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)

    assert precision == 1.0
    assert recall == 1.0
    assert fbeta == 1.0


# TODO: implement the third test. Change the function name and input as needed
def test_inference():
    """
    Test that inference returns predictions of correct shape
    """
    # Create and trains simple model
    X_train = np.random.rand(100, 10)
    y_train = np.random.randint(0, 2, 100)
    model = train_model(X_train, y_train)
    # Create test data
    X_test = np.random.rand(20, 10)
    # Get predictions
    preds = inference (model, X_test)
    # Check predictions
    assert preds.shape[0] == X_test.shape[0]
    assert all(p in [0, 1] for p in preds)
