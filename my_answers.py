import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, LSTM, Activation

# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series, window_size):
    # containers for input/output pairs
    X = [series[k:k+window_size] for k in range(len(series)-window_size)]
    y = [series[window_size+k] for k in range(len(series)-window_size)]
    
    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)
    
    return X, y
    
# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(window_size):
    model = Sequential()
    model.add(LSTM(5, input_shape=(window_size, 1), kernel_initializer='truncated_normal'))
    model.add(Dense(1, activation='tanh', kernel_initializer='truncated_normal'))
    return model

### TODO: return the text input with only ascii lowercase and the punctuation given below included.
def cleaned_text(text):
    punctuation = ['!', ',', '.', ':', ';', '?', ' ']
    unwanted_chars = set([c for c in set(list(text)) if not c.isalpha()]) - set(punctuation)
    text = text.translate({ord(c):None for c in unwanted_chars})
    return text

### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text, window_size, step_size):
    # containers for input/output pairs
    inputs = [text[k:k+window_size] for k in range(0, len(text)-window_size, step_size)]
    outputs = [text[window_size+k] for k in range(0, len(text)-window_size, step_size)]
    return inputs,outputs

# TODO build the required RNN model: 
# a single LSTM hidden layer with softmax activation, categorical_crossentropy loss 
def build_part2_RNN(window_size, num_chars):
    model = Sequential()
    model.add(LSTM(200, input_shape=(window_size, num_chars), kernel_initializer='truncated_normal'))
    model.add(Dense(num_chars))
    model.add(Activation('softmax'))
    return model

