# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 12:37:58 2022

@author: Q027703
"""
def write_text(textname,text):
    text_file = open(textname,"w")
    text = str(text.encode('utf-8'))
    text_file.write(text)
    text_file.close()
    return