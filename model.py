#coding=utf-8


class Model(object):
    """
    The model class is the superclass of all ml models in TS predicton
    This class has 3 functions
    fit(train_data, train): using fit func to fit the model with train data
    predict(test_data): using model.predict to get predict value
    test():use a shared function to evaluate the ability of each model
    """
    def __init__(self):
        pass

    def fit(self, train_data, train_label):
        pass

    def predict(self, test_data):
        pass

    def test(self, test_data, test_label):
        pass