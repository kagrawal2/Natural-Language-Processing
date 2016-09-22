import re
from functools import reduce

def splitkeepsep(s, sep):
    return reduce(lambda acc, elem: acc[:-1] + [acc[-1] + elem] if elem == sep else acc + [elem], re.split("(%s)" % re.escape(sep), s), [])
#Splits the file into words
def splitFileWords(filePath):
    list_of_elements = list()
    with open(filePath) as f:
        for line in f:
            list_of_elements.extend([x for x in line.split()])
# print(list_of_elements[:20])

#splits the file into a list of sentences
def splitFileSentence(filePath):
    with open(filePath, 'r') as myfile:
        data = myfile.read()
        data = splitkeepsep(data, '.')
        # data = [splitkeepsep(x, '?') for x in data]
        # data = [item for sublist in data for item in sublist]
        # data = [splitkeepsep(x, '!') for x in data]
        # data = [item for sublist in data for item in sublist]
        data = [splitkeepsep(x, '\n') for x in data]
        data = [item for sublist in data for item in sublist]
        # data = splitkeepsep(data, '\n')
        return data
        # return [elem.lstrip() + "." for elem in re.split('[.]', data) if elem.lstrip() != '']

def getFileParagraphInstance(filePath):
    with open(filePath, 'r') as myfile:
        data = myfile.read()
        data = splitkeepsep(data, '.')
        data = [splitkeepsep(x, '\n') for x in data]
        data = [item for sublist in data for item in sublist]
        # _sentences = [elem for elem in re.split('[.]', data) if elem != '']
        # print(_sentences[:3])
        indices = [i for i, x in enumerate(data) if "\n" in x]
        return indices

#splits a string into a list of sentences
def splitStringSentence(string):
    data = splitkeepsep(string, '.')
    # data = [splitkeepsep(x, '?') for x in data]
    # data = [item for sublist in data for item in sublist]
    # data = [splitkeepsep(x, '!') for x in data]
    # data = [item for sublist in data for item in sublist]
    data = [splitkeepsep(x, '\n') for x in data]
    data = [item for sublist in data for item in sublist]
    # return [elem.lstrip() for elem in re.split('[.]', string) if elem.lstrip() != '']
    return data

def getFileParagraphSentences(filePath):
    with open(filePath, 'r') as myfile:
        data = myfile.read()
        return [elem for elem in re.split('[.!?]', data) if elem != '']

def keepPunctuation(filePath):
    with open(filePath, 'r') as myfile:
        data = myfile.read()
        return splitkeepsep(data, '.')
        # data = [elem.lstrip() + "." for elem in re.split('[.\n]', data) if elem.lstrip() != '']
        # return data

        # print(data)
        # data = [elem.lstrip() + "?" for elem in re.split('[?]', data) if elem.lstrip() != '']
        # print(data)
        # return [elem.lstrip() + "!" for elem in re.split('[!]', data) if elem.lstrip() != '']
        
# print(getFileParagraphInstance("/Users/kireet/Projects/MyReviewers/PlagiarismDetection/textFiles/test.txt"))

# print(keepPunctuation("/Users/kireet/Projects/MyReviewers/PlagiarismDetection/draftChanges/final2"))

#splits the file into a list of paragraphs
def splitFileParagraph(filePath):
    with open(filePath, 'r') as myfile:
        data = myfile.read()
        # paragraphs = data.split("\n\n")
        paragraphs = data.split("\n")
        paragraphs[:] = (value.lstrip() for value in paragraphs if value != '\t' and value != '')
        return paragraphs


#converts the file into one single string
def longFileString(filePath):
    with open(filePath, 'r') as myfile:
        data = "".join(line.rstrip() for line in myfile)
        return data


#converts the file into a list of characters
def characterFileString(filePath):
    with open(filePath, 'r') as myfile:
        data = myfile.read().replace('\n', '')
        return list(data)

# print(longString('textFiles/chamber.txt'))

# print(splitFileParagraph('testFiles/testParagraph.txt'))