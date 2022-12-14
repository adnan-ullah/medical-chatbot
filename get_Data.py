import imp
import pickle
from queue import Empty
import numpy as np
import json
import tensorflow as tf
import random
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

intents_file = json.loads(open('assetsPhysical/ChatData (2).json').read())
lem_words = pickle.load(open('assetsPhysical/lem_words (2).pkl', 'rb'))
classes = pickle.load(open('assetsPhysical/classes (2).pkl', 'rb'))
bot_model = tf.keras.models.load_model('assetsPhysical/chatbot_model (2).h5')

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

def cleaning(text):
    words = nltk.word_tokenize(text)
    words = [lemmatizer.lemmatize(word.lower()) for word in words]
    return words

def bag_ow(text, words, show_details=True):
    sentence_words = cleaning(text)
    bag_of_words = [0]*len(words) 
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                bag_of_words[i] = 1
    return (np.array(bag_of_words))



def class_prediction(sentence, model):
    p = bag_ow(sentence, lem_words,show_details=False)
    result = model.predict(np.array([p]))[0]
    ER_THRESHOLD = 0.20
    f_results = [[i,r] for i,r in enumerate(result) if r > ER_THRESHOLD]
    f_results.sort(key=lambda x: x[1], reverse=True)
    intent_prob_list = []
    for i in f_results:
        intent_prob_list.append({"intent": classes[i[0]], "probability": str(i[1])})
    
    print(intent_prob_list)
    return intent_prob_list


def getbotResponse(ints, intents):
    tag = ints[0]['intent']
    intents_list = intents['intents']
    
    for intent in intents_list:
        if(intent['tag'] == tag):
            result = random.choice(intent['responses'])
            context = intent['context']
                
           

            break
    return (result, context)


def bot_response(text):
    ints = class_prediction(text, bot_model)
    response = getbotResponse(ints, intents_file)
    return response



