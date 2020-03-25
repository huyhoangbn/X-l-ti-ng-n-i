import numpy 
import os



def getText():
   f = open("Text.txt", encoding="utf8")
   listText = f.read().split("///\n")
   f.close()
   return listText

open('Text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

text = re.sub('[\n]+', ' ', text)
sentences = re.split(r' [\.\?!][\'"\)\]] *', text)

f = open('demo_file2.txt', 'w')
f.close()

