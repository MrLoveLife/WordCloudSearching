# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 12:16:19 2022

@author: Q027703
"""
# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns
from wordcloud import WordCloud
# from textblob import TextBlob
from PIL import Image


# filename = '../PDFs/Akhil_Resume.pdf'
def pdf_to_wordcloud(filename):
    from pdf_to_text import extract_text_from_pdf
    text = extract_text_from_pdf(filename)
    textname = str.replace(filename,".pdf",".txt")
    textname = str.replace(textname,"/PDFs/","/Texts/")
    
    #  Write pdf->text file
    from write_text import write_text
    write_text(textname, text)
    
    
    # Remove the text number,
    
    from text_clean import text_clean
    text = text_clean(text)
    text = str(text)
    
    #--------------------------------------------------------------------------------------
    
    #setting mask image
    mask = np.array(Image.open(r'..\PPG_logo.png'))
    plt.imshow(mask)
    plt.axis("off")
    
    # lower max_font_size, change the maximum number of word and lighten the background:
    from wordcloud import ImageColorGenerator
    
    #--------------------------------------------------------------------------------------
    
    #creating wordcloud
    wordcloud = WordCloud(mask=mask, width=2000, height=1000,contour_color="black", max_words=10000,relative_scaling = 0, background_color = "white").generate(text)
    image_colors = ImageColorGenerator(mask)
    plt.figure(figsize=[20,15])
    plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis("off")
    _=plt.show()
    
    # store to file
    pngname = str.replace(textname, ".txt", ".png")
    pngname = str.replace(pngname, "/Texts/", "/WordClouds/")
    
    wordcloud.to_file(pngname)
    return