from sklearn.feature_extraction.text import TfidfVectorizer
from  nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
from tokenizer import strip
import time


class TFIDF(object):

    def __init__(self, corpus, ngram):
        self.Corpus = corpus
        self.token_dict = corpus.getTokenDictionary()
        self.files_dict = corpus.getFileDictionary()

        if (ngram):
            self.tfidf_vectorizer = TfidfVectorizer(min_df= 1, norm='l2', analyzer="char", ngram_range=(5,5))
        else:
            self.tfidf_vectorizer = TfidfVectorizer(min_df= 1, norm='l2')

        self.tfs = self.tfidf_vectorizer.fit_transform(self.token_dict.values())

    def findMatchingFiles(self, document_distances):
        test = [sorted(enumerate(x), key=lambda x: x[1], reverse=True) for x in document_distances] #bug with checking against corpus, enumerate will be wrong
        sims = [y[1] for y in test] #must check if it is against itself, not just the second part
        similarFiles = [(self.files_dict[sim[0]], sim[1]) for sim in sims] #figure out a threshold level with more data this is an initial similarity score.
        similarity = []
        for i in range(0, len(similarFiles)):
            similarity.append((self.files_dict[i], similarFiles[i]))
        print()
        print(similarity)
        return similarity

    def findClosestMatch(self, document_distances):
        sims = [sorted(enumerate(x), key=lambda x: x[1], reverse=True) for x in document_distances][0] #must add to a list based on score values
        # similarFiles = []
        # for i in range(0, len(test)):   
        #      if (test[i][1] >= thresholdValue):
        #           similarFiles.append((self.files_dict[test[i][0]], test[i][1])
        # 
        similarFiles = [(self.files_dict[sim[0]], sim[1]) for sim in sims] #figure out a threshold level with more data this is an initial similarity score.
        print(similarFiles)
        return similarFiles

    def withinClass(self):
        document_distances = cosine_similarity(self.tfs, self.tfs)
        # print(document_distances)
        return self.findMatchingFiles(document_distances)

    def againstDefinedCorpus(self, inputString):
        new_term_freq_matrix = self.tfidf_vectorizer.transform([strip(inputString)])
        # print(self.tfidf_vectorizer.vocabulary_)
        # print(new_term_freq_matrix.todense())
        document_distances = cosine_similarity(new_term_freq_matrix, self.tfs)
        # print(document_distances)
        return (inputString, self.findClosestMatch(document_distances))
        # return self.findClosestMatch(document_distances)

    def addtoCorpus(self, inputString):
        self.Corpus.addStringDict(inputString)
        self.tfs = self.tfidf_vectorizer.fit_transform(self.Corpus.getTokenDictionary().values())
        return withinClass()

