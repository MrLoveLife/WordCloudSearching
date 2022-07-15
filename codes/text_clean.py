# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 10:50:38 2022

@author: Q027703
"""
#importing packeges for cleaning
# import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# from wordcloud import WordCloud
# from textblob import TextBlob
from string import punctuation


#--------------------------------------------------------------------------------------
def text_clean(text):
    #removing numbers
    text = ''.join([i for i in text if not i.isdigit()])

#--------------------------------------------------------------------------------------
#removing punctuation
    def remove_punct(text):
        text = ' '.join(word.strip(punctuation) for word in text.split() if word.strip(punctuation))
        return text

    #executing function
    text = np.vectorize(remove_punct)(text)

#--------------------------------------------------------------------------------------

    #removing other characters
    def remove_u(text):
        text = text.replace('_','')
        text = text.replace('?','')
        text = text.replace('•','')
        text = text.replace("@",'')
        text = text.replace('▯','')
        text = text.replace("'",'')
        text = text.replace(",","")
        return text
    
    #executing function
    text = np.vectorize(remove_u)(text)
    
    #--------------------------------------------------------------------------------------
    
    #removing extra spaces
    def remove_extra_space(text):
        word_list = text.split()
        text = ' '.join(word_list)
        return text
    
    #executing function
    text = np.vectorize(remove_extra_space)(text)
    
    #--------------------------------------------------------------------------------------
    
    #removing very common words
    #reference: https://gist.github.com/sebleier/554280
    stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the","Mr", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    def remove_stopwords(text):
        word_list = text.split()
        word_list = [word for word in word_list if word not in stop_words]
        text = ' '.join(word_list)
        return text

    #executing function
    text = np.vectorize(remove_stopwords)(text)
    return text
# text = text.tolist()
# print(text)