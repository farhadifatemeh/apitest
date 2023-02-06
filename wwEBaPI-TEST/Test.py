import numpy as np
import csv
from gensim.models import word2vec, Word2Vec
from gensim.test.utils import get_tmpfile
from gensim.models import KeyedVectors
from GradyFunction import functionStringdivided
from keras.utils import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.models import load_model
from keras.models import Sequential

DataNoneMotifs = []
DataMotifs = []
motifstrs = [""]
Nonemotifstrs = [""]
resultPatterns1 = []
resultPatterns2 = []
PatternsArray = []
Variant = 'CNN'


#########################################################FUNCTIONS####################
def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1
    ###########################################


#    /////// Read Dataset, input:Paths
Sequences = []
with open('Sequences.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        Sequences.append(row)

for x in range(0, len(Sequences)):
    temp = listToString(Sequences[x])
    DataNoneMotifs.append(temp)

# // Load Weights
Weights = []
with open('WeightsOfPatterns.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        Weights.append(row)

# ////////////////////////////////////////////////////

for s in range(0, len(DataNoneMotifs)):
    x = DataNoneMotifs[s]
    for i in range(0, len(x) - 6):
        PatternsArray.append(x[i:i + 7])

#######################################
# // Break Patterns
strresult = []
print("strresult")
for stri in PatternsArray:
    if len(stri) > 5:
        strresult.append(functionStringdivided(listToString(stri)))
    else:
        strresult.append(listToString(stri))

print(strresult)

# // Match Weights of Patterns
weightsPattern = []
i = 0
for s in PatternsArray:
    for w in Weights:
        if s == w[0]:
            temp = []
            temp.append(w[1])
            temp.append(w[2])
    weightsPattern.append(temp)

#print(PatternsArray)
# // Tokenised
tokenized_seq = [sentence.split() for sentence in strresult]

tokenizer = Tokenizer(num_words=100)
tokenizer.fit_on_texts(tokenized_seq)
sequencesTest = tokenizer.texts_to_sequences(tokenized_seq)
max = 3
strresult1 = pad_sequences(sequencesTest, maxlen=max)

print("Weights", strresult1)
# // Load Word2Vec Dictionary
wv = KeyedVectors.load("word2vecDictionary.wordvectors", mmap='r')

# //
print(len(strresult1))
tempword = []
svector = []
j = 0
for str in strresult1:
    for s in str:
        if s in wv:
            tempword.append(wv[s])
        else:
            strresult1.remove(str)
  #         weightsPattern.remove(weightsPattern[j])
            break
    svector.append(tempword)
    tempword = []
    j = j + 1

svector = np.array(svector)
Al = []
for p in svector:
    A = np.asarray(p).reshape(-1)
    Al.append(A)
Al = np.array(Al)
print(Al.shape)
# // Add weights
temp1 = []
x_train = []
j = 0
for x in weightsPattern:
    temp1 = np.hstack((float(x[0]), float(x[1])))
    temp1 = np.hstack((Al[j], temp1))
    x_train.append(temp1)
    temp1 = []
    j = j + 1
x_train = np.array(x_train)
print(x_train.shape)
# print(svector)
# print(len(svector[5]))
# //
from keras import models

if Variant == 'CNN':
    loaded_CNNModel = Sequential()
    loaded_CNNModel = load_model('Offline/CNNModel.h5')
    Resultprediction = loaded_CNNModel.predict(x_train)
#print(Resultprediction)

c=0
for r in Resultprediction:
    if float(r)>0.434:
        c=c+1
print(c)
print(strresult[79])
print(weightsPattern[79])
#############

# //  output
import csv

with open('t', 'w', newline='') as csv_file:
    for p in PatternsArray:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(p)
