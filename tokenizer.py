import nltk
from nltk.corpus import stopwords
import string
from  nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
import time

stemmer = PorterStemmer()
wordnet_lemmatizer = WordNetLemmatizer()
cachedStopWords = set(stopwords.words('english'))
token_dict = {}
files = {}
fileID = 0

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems

def stripText(text):
    lowers = text.lower()
    lowers = "".join(i for i in lowers if ord(i) < 128)
    no_punctuation = lowers.translate(str.maketrans({key: None for key in string.punctuation}))
    removeStop = " ".join((filter(lambda word: word not in cachedStopWords, no_punctuation.split())))
    tokened = " ".join(tokenize(removeStop))
    # lemma = "".join(wordnet_lemmatizer.lemmatize(no_punctuation))
    return tokened

# print(stripText('hello today you are sir throwing sir you are hello throws'))
# x = 'hello today'
# print(x.split())

def stripSentence(text):
    return " ".join(tokenize(text.lower().translate(str.maketrans({key: None for key in string.punctuation}))))

# print(stripSentence('hello today you are sir throwing sir you are hello throws'))

def buildStringDict(path):
    for subdir, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.txt'):
                filePath = subdir + os.path.sep + file
                with open(filePath, 'r') as myfile:
                    text = myfile.read()
                    no_punctuation = strip(text)
                    files[fileID] = file
                    fileID += 1
                    token_dict[fileID] = no_punctuation

corpus = token_dict.values()

def getStringfromFile(filePath):
    with open(filePath, 'r') as myfile:
        return strip(myfile.read())

def timeit(function, *args):
    s = time.time()
    function(*l)
    print(time.time() - s)

