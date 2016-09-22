

"""The following is research and initial tests to check the conceptual possibility of this technique."""


indexes = {} #endValue indexes for all files. dicionary mapping {lastsentence index : fileName/fileID}
corpusVectors = [] #serialized sparseMatrix that will be appended to on inputted file

    # wordlist1 = [line.strip() for line in open('/usr/share/dict/words')]

wordlist = getWordList('vocab.p')
"""
This TFIDFvectorizer must be consistent for all inputted files & all files must be inputted either in their class or on their own.
The vectorizer can work with complete strings for each file, or more effectively with sentences or paragraph splits. Each inputted file
will be added to the library of vectors(corpusVectors) and indexes dictionary. Different vocabularies can be used for different subjects.
"""
vectorizer = TfidfVectorizer(min_df= 1, norm='l2', analyzer='word', vocabulary=wordlist, preprocessor=stripText, lowercase=True)
# print(vectorizer.vocabulary)


def dictFromFile(path):
    """
    Obtain a corpus by giving a path to a folder with txt files that will become the corpus
    to be tested and used to compare any input file.
    """
    for subdir, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.txt'):
                filePath = subdir + os.path.sep + file
                with open(filePath, 'r') as fileName:
                    text = fileName.read()
                    #splitFile is the list of sentences/paragraphs that will be inputted for the corpus
                    splitFile = splitStringSentence(text)
                    #assumes unique filenames (will edit this for fileIDs in the future)
                    indexes[len(splitFile) - 1] = file
                    #add to corpus vectors by vectorizing


# file1 = ['hello today you are sir less', 'sir you are', 'hello']
# file2 = ['these are test sentences', 'to get an idea of hello']
# inputSentences = ['hello today', 'you sir are less']


"""
First time will go through files in a folder and will populate the indexes dictionary and the corpusVectors.

Independent Files:
For each file, the file will be split into paragraphs or sentences (depending on tests) strings.
then the length of these temporary lists will be add to the indexes dictionary corresponding to fileName.
then the vectorizer will vectorize the file based on just itself ie. just the given list of split strings.

Files in Class:
For each file in the class folder, the file will be split into paragraphs or sentences (depending on tests) strings.
then the length of these temporary lists will be add to the indexes dictionary corresponding to class/unique fileName.
then the vectorizer will vectorize the file based on a temporary list of all class strings.
"""
@timeit
def test():
    fileVector1 = vectorizer.fit_transform(file1).tocsr().T
    fileVector2 = vectorizer.fit_transform(file2).tocsr().T

    print(fileVector1, '\n')
    print(fileVector2, '\n')
    #will change to corpus vectors

    fileVectors = hstack((fileVector1, fileVector2))
    print(fileVectors, '\n')

    inputVectors = vectorizer.fit_transform(inputSentences).tocsr()
    print(inputVectors)


    scores = inputVectors.dot(fileVectors).todense()
    print(scores)

    #Replace this with np.apply_along_axis, np.argsort and np.where clauses once the threshold values are found. To check multiple indexes.
    # print(np.max(scores.todense()))
    # print(np.apply_along_axis(np.argsort, axis=1, arr=scores))

    scores = scores.tolist()
    for row in scores:
        sortedBySimilarity = enumerateSort(row)
        # print(sortedBySimilarity)
        max_index = sortedBySimilarity[0][0]
        #obtain the value of the indexes, which are returned by 
        # find_ge(indexes.keys(), max_index)

test()

print(fileVectors)
    transform input file sentences to fit the 


print(tfs.todense())

print()

inputVectors = tfidf_vectorizer.transform(inputSentences)

print(inputVectors.todense())

print()
document_distances = cosine_similarity(inputVectors, tfs).T

print(document_distances)
    return (inputString, self.findClosestMatch(document_distances))
