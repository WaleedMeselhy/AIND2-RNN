import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras
import string

# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series, window_size):
    # containers for input/output pairs
    X = []
    y = []
    length = np.size(series)
    X = [ series[i: i+window_size] for i in range(length-window_size) ]
    y =[ series[i+window_size] for i in range(length-window_size) ]
    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)

    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(window_size):
    model = Sequential()
    model.add(LSTM(5, input_shape=(window_size, 1),  activation='tanh'))
    model.add(Dense(1))  # default linear output ie. regression
    return model


### TODO: return the text input with only ascii lowercase and the punctuation given below included.
def cleaned_text(text):
    punctuation = ['!', ',', '.', ':', ';', '?']
    not_ascii_not_punctuation = [char for char in text if char not in punctuation and char not in string.ascii_uppercase and char not in string.ascii_lowercase]
    for char in set(not_ascii_not_punctuation):
        text = text.replace(char, ' ')  
    return text

### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text, window_size, step_size):
    # containers for input/output pair
    length = len(text) 
    inputs = [ text[i: i+window_size] for i in range(0,length-window_size,step_size) ]
    outputs =[ text[i+window_size] for i in range(0,length-window_size,step_size) ]
    return inputs,outputs

# TODO build the required RNN model: 
# a single LSTM hidden layer with softmax activation, categorical_crossentropy loss 
def build_part2_RNN(window_size, num_chars):
    model = Sequential()
    model.add(LSTM(200, input_shape=(window_size, num_chars)))
    model.add(Dense(num_chars, activation='softmax'))
    return model
