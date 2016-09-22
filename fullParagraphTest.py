from tokenizer import stripText
from  nltk.stem.porter import PorterStemmer
import os
from winnowing import dual_winnow
import Levenshtein
from NCD_Algo import ncd
from vectorSim import cosineSim
from ngram import NGram
import time
from corpusTFIDF import TFIDF
from readText import splitFileParagraph
from fullDocTest import CompareDictionary


path = "/Users/kireet/Projects/MyReviewers/PlagiarismDetection/testFiles/"

class ParagraphCorpus():

    def __init__(self):
        self.token_dict = {}
        self.paragraph_dict = {}
        self.stemmer = PorterStemmer()
        self.paragraphID = 0
        print("Must call dict from File or dict from Strings to add to Corpus")

    def paragraphDictFile(self, filePath):
        # for subdir, dirs, files in os.walk(path):
        #     for file in files:
        #         if file.endswith('.txt'):
        #             filePath = subdir + os.path.sep + file
        text = splitFileParagraph(filePath) #should return a list of paragraphs in the file

        for paragraph in text:

            self.paragraph_dict[self.paragraphID] = str(self.paragraphID) #str(filePath) + str(self.paragraphID)

            self.token_dict[self.paragraphID] = stripText(paragraph)

            self.paragraphID += 1

    def paragraphDictStrings(self, listofStrings): #list of strings will be each paragraph
        for text in listofStrings:
            self.paragraph_dict[self.paragraphID] = "Paragraph" + str(self.paragraphID)
            self.token_dict[self.paragraphID] = stripText(text)
            self.paragraphID += 1

    def getTokenDictionary(self):
        return self.token_dict

    def getFileDictionary(self):
        return self.paragraph_dict


"""
Testing Guide: 
1. Paragraph corpus must be instantiated
2. Add files/paragraph strings to the dictionary for any matching file
3. TEST: TFIDFAGAINST with the paragraphs from the input docX by calling splitFileParagraph for True(Ngram) and False(regular words)
4. Add docX to paragraph corpus with paragraphDictFile() 
5. TEST: perform TFIDF withinClass()
6. TEST: 5 other tests, winnow, levenshtein, ncd, vectorSim, ngram

"""

class CompareParagraphDictionary(object):

    def __init__(self, paragraphCorpus, function):
        self.pCorpus = paragraphCorpus
        self.function = function
        self.paragraphs = []
        self.pCompareDictionary = {}

    def compareParagraphs(self, filePath):
        self.paragraphs = splitFileParagraph(filePath)
        for i in range(0, len(self.paragraphs)):
            self.pCompareDictionary[i] = CompareDictionary(self.pCorpus, self.function).compareString(self.paragraphs[i])
        print(self.pCompareDictionary)
        return self.pCompareDictionary


"""
p = ParagraphCorpus()
p.paragraphDictFile(path + 'test8.txt')
filePath = path + "copy"

paragraphTFIDF = TFIDF(p, True)
# paragraphTFIDF = TFIDF(p, False)

paragraphs = splitFileParagraph(filePath)
# print(enumerate(paragraphs))

[paragraphTFIDF.againstDefinedCorpus(paragraphs[i]) for i in range(0, len(paragraphs))]

# print([(p, paragraphTFIDF.againstDefinedCorpus(p)) for p in paragraphs])

p.paragraphDictStrings(paragraphs)
"""

#Build hash function that is more effective for winnowing
# winnowTest = CompareParagraphDictionary(p, dual_winnow)
# winnowTest.compareParagraphs(filePath)

# levenshteinTest = CompareParagraphDictionary(p, Levenshtein.seqratio)
# levenshteinTest.compareParagraphs(filePath)

# ncdTest = CompareParagraphDictionary(p, ncd)
# ncdTest.compareParagraphs(filePath)

# vectorSimTest = CompareParagraphDictionary(p, cosineSim)
# vectorSimTest.compareParagraphs(filePath)

# ngramTest = CompareParagraphDictionary(p, NGram.compare) #remove spaces in words
# ngramTest.compareParagraphs(filePath)



















