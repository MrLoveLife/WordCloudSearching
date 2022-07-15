# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 13:03:51 2022

@author: Q027703
"""
import os
import sys
import glob
import string
from pdf_to_wordcloud import pdf_to_wordcloud

# Create a directory for converted text files
txt_directory = "Texts"				
if not os.path.exists(txt_directory):
	os.makedirs(txt_directory)

# Check if PDF directory exists
if os.path.isdir("PDFs") == False:
	print ("There is no PDFs directory, must create PDFs directory and populate with desired pdf files")

# For each file in the PDF directory run pdf2txt.py and direct stdout to txt file
for pdf in glob.glob("../pdf/*.pdf"):
    # i +=1;
    pdf_to_wordcloud(pdf)
# 	ofilename = str.replace(pdf, "PDFs", "Texts")
# 	ofilename = str.replace(ofilename, ".pdf", ".txt")
# 	print ("Converting ", pdf, "to plain text for analysis")
# 	os.system("python ./src/pdf2txt.py \"" + pdf + "\" >> \"" + ofilename+"\"")