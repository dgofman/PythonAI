# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 16:45:43 2020

@author: qin790
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:50:16 2020

@author: qin790
"""

#
#file = open("news.txt", 'r')
#total = file.read()
#file.close()
#total=total.lower()

#pip install PyPDF2
from pattern.text.en import singularize
import PyPDF2

class WordAnalysis:
    def __init__(self):
        self.__removed=[]
        self.__dictWords = dict()
        
    def __str__(self):
        s=''
        n = 0
        for key, value in self.__dictWords.items():
            s+=('{:<14} {:<3}'.format( key, value))
            n += 1
            n = n%4
            if n == 0:
                s+='{}'.format('\n')
        return s
           
    def AddRemovedWords(self, word):
        self.__removed.append(' '+word+' ')
        #print (self.__removed)
        
    def DelRemovedWords(self, word):
        word = ' '+ word +' '
        if word in self.__removed:
            self.__removed.remove(word)
        
    def ExtractWords(self, text):
        
        cleanText = ''        
        for i in range(len(text)):
            #if text[i].isalpha():
            if text[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZa\
            bcdefghijklmnopqrstuvwxyz':
                cleanText += text[i].lower()
            else:
                cleanText += ' '
                
        for i in self.__removed:
                cleanText = cleanText.replace(i," ") 
        
        wordList=list(cleanText.split())
        singularWords = [singularize(plural) for plural in wordList]  
        
                    
        ''' Get frequency count of duplicate elements in the given list '''
        # Iterate over each element in list
        for word in singularWords:
            if len(word) != 1: 
                if word in self.__dictWords:
                    # If element exists in dict then increment its value else add it in dict
                    self.__dictWords[word] += 1
                else:
                    self.__dictWords[word] = 1    
        # Filter key-value pairs in dictionary. Keep pairs whose value is greater than 1 i.e. only duplicate elements from list.
        #self.__dictOfWords = {key:value for key, value in self.__dictOfWords.items()
        #                        if value > 1}
        # Returns a dict of duplicate elements and thier frequency count
        return self.__dictWords
    
    def Show(self, freq):
        s=''
        dictOfWords = {key:value for key, value in self.__dictWords.items()
                                if value > freq}
        
        for key, value in sorted(dictOfWords.items(),key=lambda x: x[1], 
                                 reverse = True):
            s+=('{} {:^15} {} {} {}'.format( "word --", key,'-- frequency:', 
                value, "\n"))
        print(s)


# pdf file object   
# you can find find the pdf file with complete code in below
pdfFileObj = open('Samplech7.pdf', 'rb')
# pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# number of pages in pdf
pages=pdfReader.numPages

wordAnalysis = WordAnalysis()


wordAnalysis.AddRemovedWords("and")
wordAnalysis.AddRemovedWords("a")
wordAnalysis.AddRemovedWords("the")
wordAnalysis.AddRemovedWords("is")
# a page object



for i in range(4):
    pageObj = pdfReader.getPage(i)
    
# extracting text from page.
# this will print the text you can also save that into String
    wordAnalysis.ExtractWords(pageObj.extractText())

wordAnalysis.Show(10)
print (wordAnalysis)

pdfFileObj.close() 