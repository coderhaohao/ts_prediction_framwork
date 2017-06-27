#coding=utf-8
from keras.models import Sequential
from keras.layers import Dense
import numpy
from model import Model

class MLP():
    def __init__(self, input_dim, neural_list, activation_list, loss, optimizer, metrics):
        self.model = Sequential()
        self.model.add(Dense(neural_list[0], input_dim=input_dim, activation=activation_list[0]))
        for i in range(1, len(neural_list)):
            self.model.add(Dense(neural_list[i], activation=activation_list[i]))
        self.model.compile(loss=loss,optimizer=optimizer, metrics=metrics)

    def fit(self, X, y, epooch, batch_size):
        history = self.model.fit(X, y, nb_epoch=epooch, batch_size=batch_size)

    def test(self, X, y):
        loss, accuracy = self.model.evaluate(X,y)
        print("\nLoss: %.2f, Accuracy: %.2f%%" % (loss, accuracy * 100))

    def predict(self, X):
        probabilities = self.model.predict(X)
        return probabilities