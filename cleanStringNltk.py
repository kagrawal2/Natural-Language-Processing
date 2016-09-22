from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize
import re
from PyDictionary import PyDictionary

stop_words = set(stopwords.words('english'))
stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}']) # remove it if you need punctuation 


def removePunct(sentence):
    """
    >>> getSentence("Example paragraph. of words, 'with randomness?")
    Example paragraph of words with randomness
    """
    return re.sub(r'[^\w\s]','', sentence)    

def getListofWords(sentence):
    """
    >>> getListofWords("Example paragraph. of words, 'with randomness?")
    ['example', 'paragraph', 'words', 'randomness']
    """
    return [i.lower() for i in wordpunct_tokenize(sentence) if i.lower() ] # not in stop_words]

def splitAtPunct(paragraph):
    """
    >>> print(splitAtPunct("Example paragraph. of words, 'with randomness?"))
    ['Example paragraph', 'of words with randomness']
    """
    #splits paragraphs into lists of sentences based on punctuation ['.!?']
    return [getSentence(elem).strip() for elem in re.split('[.!?]', paragraph) if elem != '']

def convertSynonyms(sentenceOne, sentenceTwo):
    senX = getListofWords(sentenceOne)
    senY = getListofWords(sentenceTwo)
    dictionary = PyDictionary()

    result = []
    found = False
    for w in senY:
        for word in senX:
            if w in dictionary.synonym(word):
                result.append(word)
                found = True
                break
        if not found:
            result.append(w)
    return result

#     [entry for tag in tags for entry in entries if tag in entry]

# for tag in tags:
#     for entry in entries:
#         if tag in entry:
#             result.extend(entry)

#     print(removePunctSplit(sentenceOne))
#     oneDict = PyDictionary(removePunctSplit(sentenceOne))
#     print(oneDict.getSynonyms())

#     return 

# print(convertSynonyms("you are a can't yesterday", "you are a humbug past"))
# print(getListofWords("you are a can't yesterday. you test!",))
# print(splitAtPunct('hello how are you today? I am good you. great!'))



