# install tensorflow, matplotlib , pil
# check different types of images, metrix
import numpy as np
from numpy import array
import matplotlib.pyplot as plt

import string
import os
import glob
#from time import time
#import datetime

import tensorflow

from gtts import gTTS # Google Text to Speech API

from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.models import Model,load_model
from tensorflow.keras.utils import to_categorical
from PIL import Image
import pickle

from datetime import datetime

# inception model
inception_model = load_model('Inception_model.h5')
# encoder- decoder model
new_model=load_model('simple_model.h5')

max_length=80

with open('wordtoix.pickle','rb') as f:
    wordtoix=pickle.load(f)

with open('ixtoword.pickle','rb') as f:
    ixtoword=pickle.load(f)

generated_captions='Encountered some error!'

data_path='static/'

def preprocess(image_path):
    img = image.load_img(image_path, target_size=(299, 299)) #224
    x = np.asarray(img)
    x = image.img_to_array(x)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return x

def encode(imag):
    imag = preprocess(imag) 
    fea_vec = inception_model.predict(imag)  #inception model
    fea_vec = np.reshape(fea_vec, fea_vec.shape[1])
    return fea_vec


def getCaption(file_name):
    generated_captions = []

    feature_vector = encode(data_path+file_name).reshape((1,2048))
    print('feature_vector:',feature_vector)

    generated_captions.append(greedySearch(feature_vector))
    generated_captions.append(beam_search_predictions(feature_vector,3))
    generated_captions.append(beam_search_predictions(feature_vector,5))
    generated_captions.append(beam_search_predictions(feature_vector,7))
    # audio = generate_audio(generated_captions)
    # print('done processing')
    # print(datetime.now().time())
    # print('generated_captions are:',generated_captions,'\naudio:',audio)
    # return_value = list()
    # return_value.append(generated_captions)
    # return_value.append(audio)
    # return return_value
    return generated_captions
    
def greedySearch(feature_vector):
    print('greedy search')
    print(datetime.now().time())
    in_text = 'startseq'
    for i in range(max_length):
        sequence = [wordtoix[w] for w in in_text.split() if w in wordtoix]
        sequence = pad_sequences([sequence], maxlen=max_length)
        yhat = new_model.predict([feature_vector,sequence], verbose=0) #lstm model
        yhat = np.argmax(yhat)
        word = ixtoword[yhat]
        in_text += ' ' + word
        if word == 'endseq':
            break

    final = in_text.split()
    final = final[1:-1]
    final = ' '.join(final)
    return final

def beam_search_predictions(feature_vector, beam_index = 3):
    print('beam search')
    print(datetime.now().time())
    start = [wordtoix["startseq"]]
    start_word = [[start, 0.0]]
    while len(start_word[0][0]) < max_length:
        temp = []
        for s in start_word:
            par_caps = sequence.pad_sequences([s[0]], maxlen=max_length, padding='post')
            preds = new_model.predict([feature_vector,par_caps], verbose=0)
            word_preds = np.argsort(preds[0])[-beam_index:]
            # Getting the top <beam_index>(n) predictions and creating a 
            # new list so as to put them via the model again
            for w in word_preds:
                next_cap, prob = s[0][:], s[1]
                next_cap.append(w)
                prob += preds[0][w]
                temp.append([next_cap, prob])
                    
        start_word = temp
        # Sorting according to the probabilities
        start_word = sorted(start_word, reverse=False, key=lambda l: l[1])
        # Getting the top words
        start_word = start_word[-beam_index:]
    
    start_word = start_word[-1][0]
    intermediate_caption = [ixtoword[i] for i in start_word]
    final_caption = []
    
    for i in intermediate_caption:
        if i != 'endseq':
            final_caption.append(i)
        else:
            break

    final_caption = ' '.join(final_caption[1:])
    return final_caption


def generate_audio(text):
    # print('-'*40)
    # print('generate_audio')
    # print(datetime.now().time())
    # print(glob.glob('static/Audio/'))
    # i=1
    # for text in list_of_audio:
    #     language = 'en' # English
    #     speech = gTTS(text = text, lang = language, slow=False)
    #     #speech.save('static/Audio/audio'+str(i)+'.mp3')
    #     speech.save('static/Audio/testaudio1.mp3')
    #     i+=1
    # audio_name_list=['audio1','audio2','audio3','audio4']
    # return audio_name_list
    language = 'en'
    speech = gTTS(text = text, lang = language, slow=False)
    fileName = ''.join(datetime.now().strftime("%d%m%Y%f").split()) + '.mp3'
    speech.save(f'static/Audio/{fileName}')

    return fileName
