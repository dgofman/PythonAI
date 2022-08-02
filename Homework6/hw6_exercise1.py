# -*- coding: utf-8 -*-

"""

python hw6_exercise1.py > my_output.txt

"""

#pip install PyPDF2
#pip install inflector
import re
from collections import defaultdict

import PyPDF2
from inflector import Inflector, English
inflector = Inflector(English)

class WordAnalysis(defaultdict):
    def __init__(self, exclude=("this", "here’s", "media")):
        self.__excludeList = exclude
        self.__removed = set()
        self.__listWords = list()

    def __missing__(self, key):
        word = Word(key)
        self[word.name] = word
        return word
        
    def __str__(self):
        s = ""
        for i, word in enumerate(self.__listWords):
            s += ("{:<14} {:<3}".format(word.name, word.frequency))
            if (i + 1) % 4 == 0:
                s += "{}".format("\n")
        return s
           
    def AddRemovedWords(self, word):
        self.__removed.add(word)
        
    def DelRemovedWords(self, word):
        self.__removed.remove(word)
        
    def ExtractWords(self, text):
        words = re.findall(r"[a-z’]+", text.lower())
        #clean empty or single character and restricted words
        words = [i for i in words if len(i) > 1 and i not in self.__removed]
        #plural to singular
        singularWords = [word if len(word) < 3 or word in self.__excludeList else inflector.singularize(word) for word in words]
        # Get frequency count of duplicate elements in the given list
        for word in singularWords:
            self[word].frequency += 1
        
        self.__listWords = sorted(self.values(), key=lambda w: w.frequency, reverse = True)
        return self
    
    def Show(self, freq):
        print("\n".join( [str(w) for w in self.__listWords if w.frequency > freq]))
        print()

class Word:
    def __init__(self, name):
        self.name = re.sub("’", "'", name).rstrip("'") #replace ’ -> " and remove if on the of string
        self.frequency = 0
    
    def __str__(self):
       return "word -- {:^15} -- frequency: {}".format(self.name, self.frequency)

    def __repr__(self):
        return str(self)

def main():
    pdfFileObj = open("SampleCh7.pdf", "rb")
    # pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # number of pages in pdf
    pages=pdfReader.numPages
    #remove the words that are not meaningful. You can add back any word. Please test yourself.
    wordAnalysis = WordAnalysis()
    wordAnalysis.AddRemovedWords("and")
    wordAnalysis.AddRemovedWords("a")
    wordAnalysis.AddRemovedWords("the")
    # analys 4 pages. max pages is pages calculated above
    for i in range(4):
        pageObj = pdfReader.getPage(i)
        # extracting the words from page.into database
        wordAnalysis.ExtractWords(pageObj.extractText())
    # show words with frequency > 10
    wordAnalysis.Show(10)
    #print out all the words in the dictionary
    print (wordAnalysis)
    #close the file.
    pdfFileObj.close() 

if __name__ == "__main__":
    main()